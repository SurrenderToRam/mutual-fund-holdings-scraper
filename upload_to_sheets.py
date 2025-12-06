#!/usr/bin/env python3
"""
Upload mutual fund holdings data to Google Sheets
Optional script for automatic Google Sheets integration
"""

import pandas as pd
import os
from datetime import datetime

try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    SHEETS_AVAILABLE = True
except ImportError:
    print("⚠️  Google Sheets libraries not installed")
    print("Run: pip install gspread oauth2client")
    SHEETS_AVAILABLE = False

def upload_to_google_sheets(csv_file, sheet_name="Mutual Fund Holdings"):
    """
    Upload CSV data to Google Sheets
    
    Prerequisites:
    1. Create Google Cloud Project
    2. Enable Google Sheets API
    3. Create Service Account
    4. Download credentials JSON
    5. Share your Google Sheet with service account email
    """
    
    if not SHEETS_AVAILABLE:
        print("❌ Google Sheets libraries not available")
        return False
    
    # Check for credentials
    creds_file = os.environ.get('GOOGLE_SHEETS_CREDENTIALS', 'credentials.json')
    
    if not os.path.exists(creds_file):
        print(f"❌ Credentials file not found: {creds_file}")
        print("\nTo set up Google Sheets integration:")
        print("1. Go to https://console.cloud.google.com")
        print("2. Create new project")
        print("3. Enable Google Sheets API")
        print("4. Create Service Account")
        print("5. Download JSON credentials")
        print("6. Save as 'credentials.json'")
        return False
    
    try:
        # Read CSV
        df = pd.read_csv(csv_file)
        print(f"📊 Loaded {len(df)} rows from {csv_file}")
        
        # Authenticate
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)
        
        # Get sheet name from environment or use default
        sheet_id = os.environ.get('GOOGLE_SHEET_ID')
        
        if sheet_id:
            # Open existing sheet by ID
            spreadsheet = client.open_by_key(sheet_id)
        else:
            # Create new sheet
            spreadsheet = client.create(f"MF Holdings - {datetime.now().strftime('%Y-%m-%d')}")
            print(f"✅ Created new spreadsheet: {spreadsheet.url}")
        
        # Get or create worksheet
        try:
            worksheet = spreadsheet.worksheet(sheet_name)
            worksheet.clear()  # Clear existing data
        except:
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=len(df)+1, cols=len(df.columns))
        
        # Upload data
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        
        print(f"✅ Uploaded {len(df)} rows to Google Sheets")
        print(f"🔗 Sheet URL: {spreadsheet.url}")
        
        return True
    
    except Exception as e:
        print(f"❌ Error uploading to Google Sheets: {e}")
        return False

def main():
    """Main function"""
    # Find latest CSV file
    csv_files = [f for f in os.listdir('.') if f.startswith('mutual_fund_holdings') and f.endswith('.csv')]
    
    if not csv_files:
        print("❌ No CSV files found")
        return
    
    # Use latest file
    latest_csv = 'mutual_fund_holdings_latest.csv' if 'mutual_fund_holdings_latest.csv' in csv_files else sorted(csv_files)[-1]
    
    print(f"📁 Using file: {latest_csv}")
    upload_to_google_sheets(latest_csv)

if __name__ == "__main__":
    main()
