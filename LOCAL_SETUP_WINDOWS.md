# 💻 Local Setup for Windows PC

**Run the scraper directly on your Windows computer**

---

## 📋 What You Need

- Windows 10 or 11
- Internet connection
- 30 minutes for first-time setup

---

## 🚀 Step-by-Step Installation

### Step 1: Install Python (5 minutes)

1. **Download Python:**
   - Go to: https://www.python.org/downloads/
   - Click "Download Python 3.11" (big yellow button)
   - Save the file

2. **Install Python:**
   - Double-click the downloaded file
   - ⚠️ **IMPORTANT:** Check ✅ "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation
   - Click "Close"

3. **Verify Installation:**
   - Press `Windows + R`
   - Type: `cmd`
   - Press Enter
   - Type: `python --version`
   - Should show: `Python 3.11.x`

✅ **Python installed!**

---

### Step 2: Download the Code (2 minutes)

1. **Download from GitHub:**
   - Go to: https://github.com/SurrenderToRam/mutual-fund-holdings-scraper
   - Click green "Code" button
   - Click "Download ZIP"
   - Save to your Desktop

2. **Extract Files:**
   - Right-click the ZIP file
   - Click "Extract All"
   - Choose location: `C:\MutualFundScraper`
   - Click "Extract"

✅ **Code downloaded!**

---

### Step 3: Get Free API Key (2 minutes)

1. **Sign up for Groq:**
   - Go to: https://groq.com
   - Click "Sign Up" (FREE)
   - Sign up with Google or Email
   - Verify your email

2. **Get API Key:**
   - After login, click your profile
   - Click "API Keys"
   - Click "Create API Key"
   - **Copy the key** (starts with `gsk_`)
   - Save it in Notepad temporarily

✅ **API key obtained!**

---

### Step 4: Configure the Scraper (3 minutes)

1. **Open Folder:**
   - Go to: `C:\MutualFundScraper`
   - You should see files like `scraper.py`, `requirements.txt`, etc.

2. **Create Config File:**
   - Right-click in folder → New → Text Document
   - Name it: `.env` (yes, just `.env` with the dot)
   - If Windows complains, name it `.env.txt` first, then rename to `.env`

3. **Add API Key:**
   - Right-click `.env` → Open with → Notepad
   - Type exactly:
   ```
   GROQ_API_KEY=your_key_here
   ```
   - Replace `your_key_here` with your actual Groq API key
   - Save and close

✅ **Configuration done!**

---

### Step 5: Install Required Libraries (5 minutes)

1. **Open Command Prompt:**
   - Press `Windows + R`
   - Type: `cmd`
   - Press Enter

2. **Navigate to Folder:**
   ```cmd
   cd C:\MutualFundScraper
   ```

3. **Install Libraries:**
   ```cmd
   pip install -r requirements.txt
   ```
   - Wait 2-5 minutes
   - You'll see lots of text scrolling
   - Wait for "Successfully installed..."

✅ **Libraries installed!**

---

### Step 6: Run Your First Scrape (2 minutes)

1. **Still in Command Prompt:**
   ```cmd
   python scraper.py
   ```

2. **Watch It Work:**
   - You'll see messages like:
     - "📥 Downloading scheme master list..."
     - "🤖 AI-scraping HDFC Mutual Fund..."
     - "✅ Extracted 150 holdings from SBI MF..."
   - Takes 5-10 minutes

3. **Get Your Data:**
   - When done, you'll see: "💾 Data saved to: mutual_fund_holdings_YYYYMMDD.csv"
   - File is in `C:\MutualFundScraper`
   - Open with Excel!

✅ **First scrape complete!**

---

## 📅 Schedule Automatic Monthly Runs

### Option 1: Windows Task Scheduler (Recommended)

1. **Create Batch File:**
   - In `C:\MutualFundScraper`, create new text file
   - Name it: `run_scraper.bat`
   - Right-click → Edit
   - Add these lines:
   ```batch
   @echo off
   cd C:\MutualFundScraper
   python scraper.py
   pause
   ```
   - Save and close

2. **Open Task Scheduler:**
   - Press `Windows + R`
   - Type: `taskschd.msc`
   - Press Enter

3. **Create New Task:**
   - Click "Create Basic Task"
   - Name: "Mutual Fund Scraper"
   - Description: "Monthly MF holdings scraper"
   - Click "Next"

4. **Set Trigger:**
   - Select "Monthly"
   - Click "Next"
   - Day: 10
   - Time: 3:00 AM
   - Click "Next"

5. **Set Action:**
   - Select "Start a program"
   - Click "Next"
   - Browse to: `C:\MutualFundScraper\run_scraper.bat`
   - Click "Next"
   - Click "Finish"

✅ **Automatic monthly runs configured!**

---

### Option 2: Manual Run (Easiest)

**Just double-click `run_scraper.bat` whenever you want fresh data!**

---

## 📊 View Your Data

### In Excel:

1. Go to `C:\MutualFundScraper`
2. Find file: `mutual_fund_holdings_latest.csv`
3. Double-click to open in Excel
4. Analyze your data!

### In Google Sheets:

1. Go to: https://sheets.google.com
2. File → Import
3. Upload → Select your CSV file
4. Click "Import data"

---

## 🔧 Troubleshooting

### "Python is not recognized"

**Solution:**
1. Uninstall Python
2. Reinstall and CHECK ✅ "Add Python to PATH"
3. Restart computer
4. Try again

---

### "pip is not recognized"

**Solution:**
```cmd
python -m pip install -r requirements.txt
```

---

### "ModuleNotFoundError"

**Solution:**
```cmd
cd C:\MutualFundScraper
pip install scrapegraphai pandas requests beautifulsoup4
```

---

### "No data extracted"

**Possible causes:**
1. **No internet connection** - Check WiFi
2. **API key wrong** - Check `.env` file
3. **AMC websites down** - Try again later

---

### "Error: GROQ_API_KEY not found"

**Solution:**
1. Make sure `.env` file exists in `C:\MutualFundScraper`
2. Open `.env` in Notepad
3. Should contain: `GROQ_API_KEY=gsk_xxxxx`
4. No spaces around `=`
5. Save and try again

---

## 🎯 Quick Reference

### Run Scraper Manually:
```cmd
cd C:\MutualFundScraper
python scraper.py
```

### Update Code:
1. Download new ZIP from GitHub
2. Extract to `C:\MutualFundScraper`
3. Overwrite files
4. Keep your `.env` file

### Add More AMCs:
1. Open `amc_urls.json` in Notepad
2. Add new AMC:
   ```json
   "AMC Name": "https://amc-website.com/portfolio"
   ```
3. Save
4. Run scraper

---

## 💡 Pro Tips

1. **Keep PC on during scheduled run**
   - Or run manually when convenient

2. **Backup your data**
   - Copy CSV files to another folder monthly

3. **Check for updates**
   - Visit GitHub repo occasionally
   - Download new version if available

4. **Monitor first few runs**
   - Make sure everything works
   - Check data quality

---

## 📞 Need Help?

**Common issues solved in:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**Still stuck?** Create an issue on GitHub with:
- Error message
- Screenshot
- What you tried

---

## ✅ Success Checklist

After setup, you should have:

- [ ] Python installed
- [ ] Code downloaded to `C:\MutualFundScraper`
- [ ] `.env` file with API key
- [ ] Libraries installed
- [ ] First scrape completed successfully
- [ ] CSV file with data
- [ ] (Optional) Task Scheduler configured

**All checked? You're done!** 🎉

---

*Enjoy your automated mutual fund data!* 📊
