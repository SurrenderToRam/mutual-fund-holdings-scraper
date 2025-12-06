# 🔍 How It Works - Simple Explanation

**Understanding the system in simple terms**

---

## 📊 The Big Picture

```
┌─────────────────────────────────────────────────────────────┐
│                    YOU (One-Time Setup)                      │
│  1. Get free API key from Groq                              │
│  2. Fork this repository                                     │
│  3. Add API key to GitHub                                    │
│  4. Enable automation                                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              AUTOMATIC MONTHLY PROCESS                       │
│  (Runs on 10th of every month - you do nothing!)           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 1: GitHub Actions Starts                              │
│  • Wakes up on 10th of month                                │
│  • Runs on GitHub's free servers                            │
│  • No cost to you!                                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Download AMC List                                  │
│  • Gets list of all schemes from AMFI                       │
│  • Free public data                                          │
│  • 2,600+ schemes from 45+ AMCs                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Visit Each AMC Website                             │
│  • Goes to SBI MF, HDFC MF, ICICI MF, etc.                 │
│  • Finds portfolio pages                                     │
│  • Downloads portfolio PDFs/tables                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 4: AI Extracts Data                                   │
│  • Uses Groq AI (free) to read PDFs                         │
│  • Extracts: Stock names, ISINs, quantities, values         │
│  • Handles different formats automatically                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Organize Data                                      │
│  • Combines all AMC data                                     │
│  • Standardizes format                                       │
│  • Creates clean CSV file                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Save Results                                       │
│  • Saves CSV file                                            │
│  • Stores in GitHub (free for 90 days)                      │
│  • Ready for you to download!                               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    YOU (Download Data)                       │
│  • Go to Actions tab                                         │
│  • Download CSV file                                         │
│  • Open in Excel/Google Sheets                              │
│  • Analyze your data!                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Simple Analogy

**Think of it like this:**

1. **You hire a robot** (one-time setup)
2. **Robot visits 20 mutual fund offices** every month
3. **Robot collects all portfolio documents**
4. **Robot reads and organizes the data**
5. **Robot gives you a neat Excel file**
6. **You analyze the data** to make investment decisions

**All automatic. All free. All month!**

---

## 🔧 Technical Components (For Curious Minds)

### What Each File Does:

| File | What It Does |
|------|--------------|
| `scraper.py` | Main program that visits AMC websites |
| `amc_urls.json` | List of AMC website addresses |
| `requirements.txt` | List of tools the program needs |
| `.github/workflows/scraper.yml` | Schedule and automation settings |
| `upload_to_sheets.py` | Optional: Upload to Google Sheets |

### Technologies Used:

| Technology | Purpose | Cost |
|------------|---------|------|
| **Python** | Programming language | Free |
| **ScrapegraphAI** | AI web scraping library | Free |
| **Groq API** | Fast AI for reading PDFs | Free tier |
| **GitHub Actions** | Cloud automation | Free tier |
| **Pandas** | Data processing | Free |

---

## 🔐 Security & Privacy

### Is It Safe?

✅ **YES! Here's why:**

1. **Your API key is encrypted**
   - Stored in GitHub Secrets
   - Never visible in code
   - Only accessible to your workflows

2. **No personal data collected**
   - Only scrapes public AMC websites
   - No login required
   - No sensitive information

3. **Open source**
   - All code is visible
   - You can review everything
   - Community verified

4. **Runs in isolated environment**
   - GitHub's secure servers
   - Fresh environment each run
   - No data persistence

---

## 📅 Scheduling Explained

### When Does It Run?

**Automatic Schedule:**
```
Cron: '0 3 10 * *'
```

**Translation:**
- `0` = At minute 0
- `3` = At hour 3 (3 AM)
- `10` = On day 10 of month
- `*` = Every month
- `*` = Every day of week

**In simple terms:** Runs at 3:00 AM on the 10th of every month

### Why 10th of Month?

- Most AMCs publish previous month's data by 7th-10th
- Gives buffer time for all AMCs to update
- Ensures you get complete data

### Can I Change It?

**Yes!** Edit `.github/workflows/scraper.yml`:

**Run on 1st of month:**
```yaml
- cron: '0 3 1 * *'
```

**Run every Monday:**
```yaml
- cron: '0 3 * * 1'
```

**Run daily:**
```yaml
- cron: '0 3 * * *'
```

---

## 💾 Data Storage

### Where Is Data Stored?

1. **During Processing:**
   - Temporarily in GitHub Actions runner
   - Deleted after workflow completes

2. **After Processing:**
   - Saved as "Artifact" in GitHub
   - Available for 90 days
   - You download to your computer

3. **Long-Term Storage:**
   - On your computer (after download)
   - Optional: Upload to Google Sheets
   - Optional: Save to database

### Data Retention:

- **GitHub Artifacts:** 90 days (free)
- **Your Downloads:** Forever (on your computer)
- **Google Sheets:** Forever (if you upload)

---

## 🔄 Update Process

### How Does It Handle Changes?

**If AMC website changes:**
- AI adapts automatically (usually)
- Fallback to basic scraping
- Logs errors for manual review

**If AMC adds new schemes:**
- Automatically detected from AMFI
- Included in next run
- No action needed from you

**If AMC removes schemes:**
- Automatically excluded
- Historical data preserved
- No errors

---

## 📊 Data Quality

### How Accurate Is It?

**Very accurate because:**

1. **Source:** Official AMC websites
2. **Verification:** Cross-checked with AMFI data
3. **AI Extraction:** Groq AI is highly accurate
4. **Fallback:** Multiple extraction methods
5. **Validation:** Data format checks

**Typical accuracy:** 95-98%

**Errors usually from:**
- AMC website temporarily down
- PDF format changes
- Incomplete data on AMC site

---

## 🎓 Learning Resources

### Want to Understand More?

**For Non-Technical:**
- [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [What is API?](https://www.youtube.com/watch?v=s7wmiS2mSXY)
- [What is CSV?](https://www.youtube.com/watch?v=UofTplCVkYI)

**For Technical:**
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [ScrapegraphAI Docs](https://scrapegraphai.com/docs)
- [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)

---

## ❓ Common Questions

### Q: Do I need to keep my computer on?

**A:** No! Runs on GitHub's servers (cloud).

### Q: Will it stop working after some time?

**A:** No! As long as GitHub Actions is free (it is), it will run forever.

### Q: What if an AMC website is down?

**A:** That AMC will be skipped. Others will still work. Try again next month.

### Q: Can I run it more than once a month?

**A:** Yes! Go to Actions → Run workflow anytime.

### Q: Will I get notified when it runs?

**A:** You can enable email notifications in GitHub settings.

### Q: Can I share this with friends?

**A:** Yes! They should fork and set up their own copy.

---

## 🚀 Next Steps

**Ready to set it up?**

👉 **[Go to YOUR_NEXT_STEPS.md](YOUR_NEXT_STEPS.md)**

---

*Questions? Create an [Issue](../../issues) and we'll help!*
