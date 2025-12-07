#!/usr/bin/env python3
"""
Mutual Fund Holdings Scraper
Automatically extracts stock holdings from Indian AMC websites
"""

import os
import json
import pandas as pd
import requests
from datetime import datetime
from io import StringIO
import time

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded configuration from .env file")
except ImportError:
    print("ℹ️  python-dotenv not installed, using environment variables")

# Try to import scrapegraphai, fallback to basic scraping if not available
try:
    from scrapegraphai.graphs import SmartScraperGraph
    USE_AI = True
except ImportError:
    print("⚠️  ScrapegraphAI not available, using basic scraping")
    USE_AI = False

def get_groq_config():
    """Get Groq API configuration"""
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable not set!\n"
            "For local setup: Create a .env file with your API key\n"
            "For GitHub Actions: Add GROQ_API_KEY to repository secrets"
        )
    
    return {
        "llm": {
            "api_key": api_key,
            "model": "groq/llama-3.1-70b-versatile",
        },
    }

def load_amc_urls():
    """Load AMC URLs from configuration file"""
    try:
        with open('amc_urls.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default URLs if file doesn't exist
        return {
            "SBI Mutual Fund": "https://www.sbimf.com/en-us/scheme-performance",
            "HDFC Mutual Fund": "https://www.hdfcfund.com/schemes-performance/portfolio",
            "ICICI Prudential MF": "https://www.icicipruamc.com/downloads/portfolio",
        }

def get_amfi_scheme_master():
    """Download complete scheme master list from AMFI"""
    print("\n📥 Downloading scheme master list from AMFI...")
    
    try:
        url = "https://portal.amfiindia.com/DownloadSchemeData_Po.aspx?mf=0"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Parse CSV
        df = pd.read_csv(StringIO(response.text), sep=';')
        
        print(f"✅ Found {len(df)} schemes from {df['AMC Name'].nunique()} AMCs")
        return df
    
    except Exception as e:
        print(f"❌ Error downloading AMFI data: {e}")
        return pd.DataFrame()

def scrape_amc_portfolio_ai(amc_name, url, config):
    """Scrape portfolio using AI (ScrapegraphAI)"""
    print(f"\n🤖 AI-scraping {amc_name}...")
    
    try:
        smart_scraper = SmartScraperGraph(
            prompt="""Extract all stock holdings from this mutual fund portfolio. 
            For each stock, extract:
            - Scheme Name (name of the mutual fund scheme)
            - Stock Name (company name)
            - ISIN code (12-character code)
            - Quantity (number of shares held)
            - Market Value (in rupees)
            - Weight or Percentage of portfolio
            
            Return as a structured list of dictionaries.
            If data is in PDF, extract from tables.
            """,
            source=url,
            config=config
        )
        
        result = smart_scraper.run()
        
        if isinstance(result, dict) and 'stocks' in result:
            result = result['stocks']
        
        if isinstance(result, list) and len(result) > 0:
            print(f"✅ Extracted {len(result)} holdings from {amc_name}")
            return result
        else:
            print(f"⚠️  No data extracted from {amc_name}")
            return []
    
    except Exception as e:
        print(f"❌ Error scraping {amc_name}: {e}")
        return []

def scrape_amc_portfolio_basic(amc_name, url):
    """Basic scraping fallback (without AI)"""
    print(f"\n📄 Basic scraping {amc_name}...")
    
    try:
        # Try to get HTML tables
        tables = pd.read_html(url)
        
        if tables:
            print(f"✅ Found {len(tables)} tables from {amc_name}")
            # Return first table that looks like portfolio data
            for table in tables:
                if len(table) > 5 and len(table.columns) >= 3:
                    return table.to_dict('records')
        
        print(f"⚠️  No suitable tables found in {amc_name}")
        return []
    
    except Exception as e:
        print(f"❌ Error scraping {amc_name}: {e}")
        return []

def main():
    """Main scraping function"""
    print("="*60)
    print("🚀 MUTUAL FUND HOLDINGS SCRAPER")
    print("="*60)
    print(f"📅 Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get AMFI scheme master
    schemes_df = get_amfi_scheme_master()
    
    # Load AMC URLs
    amc_urls = load_amc_urls()
    print(f"\n📋 Configured to scrape {len(amc_urls)} AMCs")
    
    # Get AI config if available
    config = None
    if USE_AI:
        try:
            config = get_groq_config()
            print("✅ AI scraping enabled (using Groq)")
        except ValueError as e:
            print(f"⚠️  {e}")
            print("⚠️  Falling back to basic scraping")
    
    # Scrape all AMCs
    all_holdings = []
    
    for amc_name, url in amc_urls.items():
        try:
            # Use AI scraping if available, otherwise basic
            if USE_AI and config:
                holdings = scrape_amc_portfolio_ai(amc_name, url, config)
            else:
                holdings = scrape_amc_portfolio_basic(amc_name, url)
            
            # Add metadata to each holding
            for holding in holdings:
                holding['amc'] = amc_name
                holding['scraped_date'] = datetime.now().strftime('%Y-%m-%d')
                holding['source_url'] = url
            
            all_holdings.extend(holdings)
            
            # Rate limiting - be nice to servers
            time.sleep(2)
        
        except Exception as e:
            print(f"❌ Failed to scrape {amc_name}: {e}")
            continue
    
    # Create DataFrame
    if all_holdings:
        df = pd.DataFrame(all_holdings)
        
        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('%', 'percent')
        
        # Summary statistics
        print("\n" + "="*60)
        print("📊 SCRAPING COMPLETE!")
        print("="*60)
        print(f"✅ Total AMCs scraped: {df['amc'].nunique()}")
        print(f"✅ Total holdings records: {len(df)}")
        
        if 'scheme_name' in df.columns:
            print(f"✅ Total schemes: {df['scheme_name'].nunique()}")
        
        if 'stock_name' in df.columns:
            print(f"✅ Total unique stocks: {df['stock_name'].nunique()}")
        
        # Save to CSV
        output_file = f"mutual_fund_holdings_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\n💾 Data saved to: {output_file}")
        
        # Also save as latest
        df.to_csv('mutual_fund_holdings_latest.csv', index=False)
        print(f"💾 Latest copy saved to: mutual_fund_holdings_latest.csv")
        
        # Display sample
        print("\n📋 Sample data (first 5 rows):")
        print(df.head())
        
        return df
    
    else:
        print("\n❌ No data extracted from any AMC")
        return None

if __name__ == "__main__":
    main()
