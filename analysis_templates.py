#!/usr/bin/env python3
"""
Financial Market Analysis Templates
Ready-to-use analysis scripts for mutual fund holdings data
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(filepath='mutual_fund_holdings_latest.csv'):
    """Load mutual fund holdings data"""
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} holdings records")
    return df

# ============================================
# 1. MOST HELD STOCKS ANALYSIS
# ============================================

def analyze_most_held_stocks(df, top_n=20):
    """
    Find stocks held by most mutual fund schemes
    Indicates market consensus and institutional confidence
    """
    print("\n" + "="*60)
    print("📊 TOP MOST HELD STOCKS")
    print("="*60)
    
    analysis = df.groupby('stock_name').agg({
        'scheme_name': 'count',
        'market_value': 'sum',
        'weight_percent': 'mean',
        'amc': 'nunique'
    }).rename(columns={
        'scheme_name': 'num_schemes',
        'market_value': 'total_value_cr',
        'weight_percent': 'avg_weight_pct',
        'amc': 'num_amcs'
    })
    
    # Convert to crores
    analysis['total_value_cr'] = analysis['total_value_cr'] / 10000000
    
    # Sort by number of schemes
    analysis = analysis.sort_values('num_schemes', ascending=False).head(top_n)
    
    print(f"\nTop {top_n} stocks by number of schemes holding:\n")
    print(analysis.to_string())
    
    return analysis

# ============================================
# 2. CONCENTRATED BETS ANALYSIS
# ============================================

def analyze_concentrated_bets(df, min_weight=5.0):
    """
    Find high-conviction bets (stocks with >5% portfolio weight)
    Indicates strong conviction by fund managers
    """
    print("\n" + "="*60)
    print("🎯 HIGH CONVICTION BETS (Weight > {}%)".format(min_weight))
    print("="*60)
    
    concentrated = df[df['weight_percent'] > min_weight].copy()
    
    analysis = concentrated.groupby('stock_name').agg({
        'scheme_name': lambda x: ', '.join(x.head(5)),
        'weight_percent': ['count', 'mean', 'max'],
        'amc': lambda x: ', '.join(x.unique()[:3])
    })
    
    analysis.columns = ['schemes_sample', 'num_high_weight', 'avg_weight', 'max_weight', 'amcs_sample']
    analysis = analysis.sort_values('num_high_weight', ascending=False).head(20)
    
    print(f"\nStocks with high portfolio weights (>{min_weight}%):\n")
    print(analysis.to_string())
    
    return analysis

# ============================================
# 3. SECTOR ALLOCATION ANALYSIS
# ============================================

def analyze_sector_allocation(df):
    """
    Analyze sector-wise allocation of mutual funds
    Identifies sector preferences and rotation
    """
    print("\n" + "="*60)
    print("🏭 SECTOR ALLOCATION ANALYSIS")
    print("="*60)
    
    if 'sector' not in df.columns:
        print("⚠️  Sector information not available in data")
        return None
    
    sector_analysis = df.groupby('sector').agg({
        'market_value': 'sum',
        'stock_name': 'nunique',
        'scheme_name': 'count',
        'weight_percent': 'mean'
    }).rename(columns={
        'market_value': 'total_value_cr',
        'stock_name': 'num_stocks',
        'scheme_name': 'num_holdings',
        'weight_percent': 'avg_weight'
    })
    
    # Convert to crores
    sector_analysis['total_value_cr'] = sector_analysis['total_value_cr'] / 10000000
    
    # Calculate percentage
    sector_analysis['pct_of_total'] = (
        sector_analysis['total_value_cr'] / sector_analysis['total_value_cr'].sum() * 100
    )
    
    sector_analysis = sector_analysis.sort_values('total_value_cr', ascending=False)
    
    print("\nSector-wise allocation:\n")
    print(sector_analysis.to_string())
    
    return sector_analysis

# ============================================
# 4. AMC COMPARISON ANALYSIS
# ============================================

def analyze_amc_strategies(df):
    """
    Compare investment strategies across AMCs
    Shows diversification, concentration, and preferences
    """
    print("\n" + "="*60)
    print("🏢 AMC STRATEGY COMPARISON")
    print("="*60)
    
    amc_analysis = df.groupby('amc').agg({
        'scheme_name': 'nunique',
        'stock_name': 'nunique',
        'market_value': 'sum',
        'weight_percent': 'mean'
    }).rename(columns={
        'scheme_name': 'num_schemes',
        'stock_name': 'num_unique_stocks',
        'market_value': 'total_aum_cr',
        'weight_percent': 'avg_stock_weight'
    })
    
    # Convert to crores
    amc_analysis['total_aum_cr'] = amc_analysis['total_aum_cr'] / 10000000
    
    # Calculate average stocks per scheme
    amc_analysis['avg_stocks_per_scheme'] = (
        amc_analysis['num_unique_stocks'] / amc_analysis['num_schemes']
    )
    
    amc_analysis = amc_analysis.sort_values('total_aum_cr', ascending=False)
    
    print("\nAMC-wise comparison:\n")
    print(amc_analysis.to_string())
    
    return amc_analysis

# ============================================
# 5. PORTFOLIO OVERLAP ANALYSIS
# ============================================

def analyze_portfolio_overlap(df, scheme1, scheme2):
    """
    Calculate overlap between two schemes
    Helps avoid redundant investments
    """
    print("\n" + "="*60)
    print(f"🔄 PORTFOLIO OVERLAP ANALYSIS")
    print("="*60)
    
    # Get holdings for each scheme
    holdings1 = set(df[df['scheme_name'].str.contains(scheme1, case=False, na=False)]['stock_name'])
    holdings2 = set(df[df['scheme_name'].str.contains(scheme2, case=False, na=False)]['stock_name'])
    
    if not holdings1 or not holdings2:
        print(f"⚠️  One or both schemes not found")
        return None
    
    # Calculate overlap
    common_stocks = holdings1.intersection(holdings2)
    overlap_pct = len(common_stocks) / len(holdings1) * 100
    
    print(f"\nScheme 1: {scheme1}")
    print(f"Total stocks: {len(holdings1)}")
    print(f"\nScheme 2: {scheme2}")
    print(f"Total stocks: {len(holdings2)}")
    print(f"\nCommon stocks: {len(common_stocks)}")
    print(f"Overlap: {overlap_pct:.1f}%")
    
    if common_stocks:
        print(f"\nCommon holdings (sample):")
        for stock in list(common_stocks)[:10]:
            print(f"  - {stock}")
    
    return {
        'scheme1': scheme1,
        'scheme2': scheme2,
        'holdings1': len(holdings1),
        'holdings2': len(holdings2),
        'common': len(common_stocks),
        'overlap_pct': overlap_pct,
        'common_stocks': list(common_stocks)
    }

# ============================================
# 6. HIDDEN GEMS FINDER
# ============================================

def find_hidden_gems(df, max_holders=5, min_value=100):
    """
    Find quality stocks held by few schemes
    Potential undervalued opportunities
    """
    print("\n" + "="*60)
    print(f"💎 HIDDEN GEMS (Held by ≤{max_holders} schemes)")
    print("="*60)
    
    stock_counts = df.groupby('stock_name').agg({
        'scheme_name': 'count',
        'market_value': 'sum',
        'weight_percent': 'mean',
        'amc': lambda x: ', '.join(x.unique())
    }).rename(columns={
        'scheme_name': 'num_holders',
        'market_value': 'total_value_cr',
        'weight_percent': 'avg_weight',
        'amc': 'held_by_amcs'
    })
    
    # Convert to crores
    stock_counts['total_value_cr'] = stock_counts['total_value_cr'] / 10000000
    
    # Filter for hidden gems
    hidden_gems = stock_counts[
        (stock_counts['num_holders'] <= max_holders) &
        (stock_counts['total_value_cr'] >= min_value)
    ].sort_values('total_value_cr', ascending=False)
    
    print(f"\nStocks held by ≤{max_holders} schemes but with ≥₹{min_value}Cr investment:\n")
    print(hidden_gems.head(20).to_string())
    
    return hidden_gems

# ============================================
# 7. MONTH-OVER-MONTH CHANGE ANALYSIS
# ============================================

def analyze_mom_changes(df_current, df_previous):
    """
    Compare current month vs previous month
    Identifies buying/selling trends
    """
    print("\n" + "="*60)
    print("📈 MONTH-OVER-MONTH CHANGES")
    print("="*60)
    
    # Aggregate by stock
    current = df_current.groupby('stock_name').agg({
        'scheme_name': 'count',
        'market_value': 'sum'
    }).rename(columns={'scheme_name': 'holders_current', 'market_value': 'value_current'})
    
    previous = df_previous.groupby('stock_name').agg({
        'scheme_name': 'count',
        'market_value': 'sum'
    }).rename(columns={'scheme_name': 'holders_previous', 'market_value': 'value_previous'})
    
    # Merge
    comparison = current.join(previous, how='outer').fillna(0)
    
    # Calculate changes
    comparison['holder_change'] = comparison['holders_current'] - comparison['holders_previous']
    comparison['value_change_cr'] = (comparison['value_current'] - comparison['value_previous']) / 10000000
    comparison['value_change_pct'] = (
        (comparison['value_current'] - comparison['value_previous']) / 
        comparison['value_previous'] * 100
    ).replace([np.inf, -np.inf], 0)
    
    # Top bought
    print("\n🟢 TOP BOUGHT STOCKS (by number of schemes):\n")
    top_bought = comparison.sort_values('holder_change', ascending=False).head(10)
    print(top_bought[['holders_current', 'holders_previous', 'holder_change', 'value_change_cr']].to_string())
    
    # Top sold
    print("\n🔴 TOP SOLD STOCKS (by number of schemes):\n")
    top_sold = comparison.sort_values('holder_change', ascending=True).head(10)
    print(top_sold[['holders_current', 'holders_previous', 'holder_change', 'value_change_cr']].to_string())
    
    return comparison

# ============================================
# 8. COMPREHENSIVE REPORT GENERATOR
# ============================================

def generate_monthly_report(df, output_file='monthly_analysis_report.txt'):
    """
    Generate comprehensive monthly analysis report
    """
    print("\n" + "="*60)
    print("📄 GENERATING COMPREHENSIVE REPORT")
    print("="*60)
    
    with open(output_file, 'w') as f:
        f.write("="*60 + "\n")
        f.write("MUTUAL FUND HOLDINGS ANALYSIS REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")
        
        # Summary statistics
        f.write("SUMMARY STATISTICS\n")
        f.write("-"*60 + "\n")
        f.write(f"Total AMCs: {df['amc'].nunique()}\n")
        f.write(f"Total Schemes: {df['scheme_name'].nunique()}\n")
        f.write(f"Total Unique Stocks: {df['stock_name'].nunique()}\n")
        f.write(f"Total Holdings Records: {len(df)}\n")
        f.write(f"Total Market Value: ₹{df['market_value'].sum()/10000000:.0f} Cr\n")
        f.write("\n")
        
        # Most held stocks
        f.write("TOP 20 MOST HELD STOCKS\n")
        f.write("-"*60 + "\n")
        most_held = analyze_most_held_stocks(df, top_n=20)
        f.write(most_held.to_string())
        f.write("\n\n")
        
        # Sector allocation
        if 'sector' in df.columns:
            f.write("SECTOR ALLOCATION\n")
            f.write("-"*60 + "\n")
            sector_alloc = analyze_sector_allocation(df)
            if sector_alloc is not None:
                f.write(sector_alloc.to_string())
            f.write("\n\n")
        
        # AMC comparison
        f.write("AMC STRATEGY COMPARISON\n")
        f.write("-"*60 + "\n")
        amc_comp = analyze_amc_strategies(df)
        f.write(amc_comp.to_string())
        f.write("\n\n")
    
    print(f"\n✅ Report saved to: {output_file}")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("🚀 MUTUAL FUND HOLDINGS ANALYSIS")
    print("="*60)
    
    # Load data
    df = load_data()
    
    # Run all analyses
    print("\n1️⃣  Running Most Held Stocks Analysis...")
    analyze_most_held_stocks(df)
    
    print("\n2️⃣  Running Concentrated Bets Analysis...")
    analyze_concentrated_bets(df)
    
    print("\n3️⃣  Running Sector Allocation Analysis...")
    analyze_sector_allocation(df)
    
    print("\n4️⃣  Running AMC Strategy Comparison...")
    analyze_amc_strategies(df)
    
    print("\n5️⃣  Finding Hidden Gems...")
    find_hidden_gems(df)
    
    print("\n6️⃣  Generating Comprehensive Report...")
    generate_monthly_report(df)
    
    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETE!")
    print("="*60)
    print("\nCheck 'monthly_analysis_report.txt' for detailed report")
