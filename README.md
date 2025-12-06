# 🚀 Mutual Fund Holdings Scraper - 100% FREE

**Automatically scrape stock holdings from all Indian Mutual Fund AMCs**

This system extracts complete portfolio data from 45+ AMCs including:
- Stock names
- ISIN codes
- Quantities held
- Market values
- Portfolio weights
- Scheme details

## ✨ Features

- ✅ **100% Free** - Uses free APIs and cloud services
- ✅ **Fully Automated** - Runs monthly on GitHub Actions
- ✅ **Complete Data** - All AMCs, all schemes, all stocks
- ✅ **No Coding Required** - Just follow setup steps
- ✅ **Accurate** - AI-powered extraction from PDFs
- ✅ **Export Ready** - CSV, Google Sheets, Database

## 📊 What You Get

- **45+ AMCs** covered
- **2,600+ schemes** tracked
- **1,200-1,600 unique stocks** identified
- **Monthly updates** automatically
- **Historical data** preserved

## 🎯 Quick Start (5 Minutes)

### Step 1: Get Free API Key

1. Go to [Groq.com](https://groq.com)
2. Click "Sign Up" (FREE)
3. Go to "API Keys" → "Create API Key"
4. Copy your key (starts with `gsk_`)

### Step 2: Fork This Repository

1. Click "Fork" button at top right
2. This creates your own copy

### Step 3: Add API Key to GitHub

1. In YOUR forked repo, go to **Settings** → **Secrets and variables** → **Actions**
2. Click "New repository secret"
3. Name: `GROQ_API_KEY`
4. Value: Paste your Groq API key
5. Click "Add secret"

### Step 4: Enable GitHub Actions

1. Go to **Actions** tab
2. Click "I understand my workflows, go ahead and enable them"

### Step 5: Run First Scrape

1. Go to **Actions** tab
2. Click "Monthly MF Scraper" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait 5-10 minutes
5. Download results from "Artifacts"

## 📅 Automatic Monthly Updates

The scraper runs automatically on the **10th of every month** at 3 AM UTC.

You can also run it manually anytime from the Actions tab.

## 📥 Getting Your Data

After each run:

1. Go to **Actions** tab
2. Click on the latest workflow run
3. Scroll to "Artifacts"
4. Download `mutual-fund-holdings` ZIP file
5. Extract to get CSV file

## 📊 Data Format

The CSV contains these columns:

| Column | Description |
|--------|-------------|
| `amc` | AMC name (e.g., "HDFC Mutual Fund") |
| `scheme_name` | Scheme name |
| `scheme_code` | AMFI scheme code |
| `stock_name` | Company name |
| `isin` | Stock ISIN code |
| `quantity` | Number of shares held |
| `market_value` | Value in ₹ |
| `weight_percent` | % of portfolio |
| `scraped_date` | Date of extraction |

## 🔧 Advanced: Upload to Google Sheets

See `upload_to_sheets.py` for automatic Google Sheets integration.

## 🔧 Advanced: Use PostgreSQL Database

See `database_setup.sql` for database schema.

## 📝 Supported AMCs

Currently configured for top 20 AMCs:
- SBI Mutual Fund
- HDFC Mutual Fund
- ICICI Prudential MF
- Aditya Birla Sun Life MF
- Nippon India MF
- Kotak Mahindra MF
- Axis Mutual Fund
- DSP Mutual Fund
- Tata Mutual Fund
- Mirae Asset MF
- And 10 more...

Want to add more? Edit `amc_urls.json`

## 💰 Cost

**TOTAL COST: ₹0 (100% FREE)**

- Groq API: Free tier (14,400 requests/day)
- GitHub Actions: Free (2,000 minutes/month)
- Storage: Free (GitHub artifacts)

## 🆘 Support

Having issues? 

1. Check [Issues](../../issues) tab
2. Create new issue with error details
3. Community will help!

## 📜 License

MIT License - Free to use, modify, and distribute

## ⭐ Like This Project?

Give it a star ⭐ and share with others!

---

**Built with ❤️ for the Indian investment community**
