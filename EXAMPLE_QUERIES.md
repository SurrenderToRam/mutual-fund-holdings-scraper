# 📊 Example Queries - What You Can Do With Your Data

Once you have the CSV file, here are useful things you can find:

---

## 🔍 In Excel/Google Sheets

### 1. Find Which Schemes Hold a Specific Stock

**Example: Find all schemes holding "Reliance Industries"**

1. Open CSV in Excel/Google Sheets
2. Click on `stock_name` column header
3. Click "Filter" button
4. Type "Reliance" in search box
5. See all schemes holding Reliance!

---

### 2. Find Top 10 Most Held Stocks

**Steps:**
1. Create Pivot Table
2. Rows: `stock_name`
3. Values: Count of `scheme_name`
4. Sort descending
5. See which stocks are most popular!

---

### 3. Find Total Money Invested in a Stock

**Example: Total invested in "TCS"**

1. Filter `stock_name` = "TCS"
2. Sum the `market_value` column
3. See total ₹ invested by all MFs!

---

### 4. Find All Stocks Held by a Specific Scheme

**Example: "HDFC Top 100 Fund" holdings**

1. Filter `scheme_name` = "HDFC Top 100"
2. See complete portfolio!

---

### 5. Find Schemes with Highest Exposure to a Stock

**Example: Who holds most % in "Infosys"?**

1. Filter `stock_name` = "Infosys"
2. Sort by `weight_percent` descending
3. See which schemes are most concentrated!

---

## 💻 Using Python (Advanced)

If you know Python, here are some powerful queries:

### Load the Data

```python
import pandas as pd

# Load CSV
df = pd.read_csv('mutual_fund_holdings_latest.csv')

print(f"Total records: {len(df)}")
print(f"Total AMCs: {df['amc'].nunique()}")
print(f"Total schemes: {df['scheme_name'].nunique()}")
print(f"Total stocks: {df['stock_name'].nunique()}")
```

---

### Top 20 Most Held Stocks

```python
top_stocks = df.groupby('stock_name').agg({
    'scheme_name': 'count',
    'market_value': 'sum'
}).rename(columns={
    'scheme_name': 'num_schemes',
    'market_value': 'total_value'
}).sort_values('num_schemes', ascending=False).head(20)

print(top_stocks)
```

---

### Find All Schemes Holding a Stock

```python
stock_name = "Reliance Industries"

schemes = df[df['stock_name'].str.contains(stock_name, case=False, na=False)]

print(f"\n{len(schemes)} schemes hold {stock_name}:")
print(schemes[['amc', 'scheme_name', 'quantity', 'market_value', 'weight_percent']])
```

---

### AMC-wise Stock Concentration

```python
# Which AMC holds most of a specific stock?
stock_name = "HDFC Bank"

amc_holdings = df[df['stock_name'].str.contains(stock_name, case=False, na=False)].groupby('amc').agg({
    'market_value': 'sum',
    'scheme_name': 'count'
}).rename(columns={
    'market_value': 'total_value',
    'scheme_name': 'num_schemes'
}).sort_values('total_value', ascending=False)

print(amc_holdings)
```

---

### Stocks Held by Only One Scheme (Unique Holdings)

```python
stock_counts = df.groupby('stock_name')['scheme_name'].count()
unique_stocks = stock_counts[stock_counts == 1]

print(f"\n{len(unique_stocks)} stocks held by only 1 scheme")
print(df[df['stock_name'].isin(unique_stocks.index)][['stock_name', 'scheme_name', 'amc']])
```

---

### Portfolio Overlap Between Two Schemes

```python
scheme1 = "HDFC Top 100 Fund"
scheme2 = "ICICI Prudential Bluechip Fund"

stocks1 = set(df[df['scheme_name'].str.contains(scheme1, case=False, na=False)]['stock_name'])
stocks2 = set(df[df['scheme_name'].str.contains(scheme2, case=False, na=False)]['stock_name'])

overlap = stocks1.intersection(stocks2)

print(f"\nCommon stocks between {scheme1} and {scheme2}:")
print(f"Total overlap: {len(overlap)} stocks")
print(list(overlap))
```

---

### Sector-wise Analysis (if sector data available)

```python
# If you have sector information
if 'sector' in df.columns:
    sector_summary = df.groupby('sector').agg({
        'market_value': 'sum',
        'stock_name': 'nunique'
    }).rename(columns={
        'market_value': 'total_value',
        'stock_name': 'num_stocks'
    }).sort_values('total_value', ascending=False)
    
    print(sector_summary)
```

---

### Export Specific AMC Data

```python
# Export only SBI MF data
sbi_data = df[df['amc'].str.contains('SBI', case=False, na=False)]
sbi_data.to_csv('sbi_mutual_fund_holdings.csv', index=False)

print(f"Exported {len(sbi_data)} SBI MF holdings")
```

---

### Monthly Comparison (if you have multiple months)

```python
# Load two months of data
df_current = pd.read_csv('mutual_fund_holdings_20250110.csv')
df_previous = pd.read_csv('mutual_fund_holdings_20241210.csv')

# Find new stocks added
current_stocks = set(df_current['stock_name'])
previous_stocks = set(df_previous['stock_name'])

new_stocks = current_stocks - previous_stocks
removed_stocks = previous_stocks - current_stocks

print(f"New stocks added: {len(new_stocks)}")
print(f"Stocks removed: {len(removed_stocks)}")
```

---

## 📈 Visualization Ideas

### Using Python + Matplotlib

```python
import matplotlib.pyplot as plt

# Top 10 stocks by total market value
top_10 = df.groupby('stock_name')['market_value'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_10.plot(kind='barh')
plt.title('Top 10 Stocks by Total MF Holdings')
plt.xlabel('Total Market Value (₹)')
plt.tight_layout()
plt.savefig('top_10_stocks.png')
```

---

## 🎯 Business Intelligence Questions You Can Answer

1. **Which stocks are mutual fund favorites?**
   - Count schemes per stock

2. **Which AMC has most diversified portfolio?**
   - Count unique stocks per AMC

3. **Concentration risk analysis**
   - Find schemes with >10% in single stock

4. **Sector allocation trends**
   - Group by sector, sum market values

5. **Small cap vs Large cap preference**
   - Analyze by market cap (if data available)

6. **SIP-friendly stocks**
   - Stocks held by most schemes = safer for SIP

7. **Hidden gems**
   - Stocks held by only 1-2 schemes

8. **Portfolio overlap**
   - Compare holdings between schemes

---

## 💡 Pro Tips

1. **Use Pivot Tables** in Excel for quick analysis
2. **Create dashboards** in Google Sheets with charts
3. **Track changes** month-over-month
4. **Export subsets** for specific analysis
5. **Combine with price data** for valuation analysis

---

## 🔗 Useful Resources

- **Google Sheets Pivot Tables:** [Tutorial](https://support.google.com/docs/answer/1272900)
- **Excel Data Analysis:** [Guide](https://support.microsoft.com/en-us/office/overview-of-pivottables-and-pivotcharts-527c8fa3-02c0-445a-a2db-7794676bce96)
- **Python Pandas:** [Documentation](https://pandas.pydata.org/docs/)

---

**Happy Analyzing! 📊**
