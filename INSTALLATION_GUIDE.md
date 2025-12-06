# 📖 Complete Installation Guide

**Follow these steps exactly - takes only 10 minutes!**

---

## ✅ Step 1: Get Free Groq API Key (2 minutes)

1. **Open this link:** https://groq.com
2. Click **"Sign Up"** (top right)
3. Sign up with Google/Email (FREE - no credit card needed)
4. After login, click your profile → **"API Keys"**
5. Click **"Create API Key"**
6. **Copy the key** (looks like: `gsk_xxxxxxxxxxxxxxxxxxxxxx`)
7. **Save it somewhere** - you'll need it in Step 3

✅ **Done!** You now have your free API key.

---

## ✅ Step 2: Fork This Repository (1 minute)

1. **You're already here!** (on GitHub)
2. Click the **"Fork"** button (top right of this page)
3. Click **"Create fork"**
4. Wait 5 seconds - you now have your own copy!

✅ **Done!** You now have your own repository.

---

## ✅ Step 3: Add API Key to GitHub (2 minutes)

**IMPORTANT: Do this in YOUR forked repository, not the original!**

1. In **YOUR** repository, click **"Settings"** tab (top menu)
2. In left sidebar, click **"Secrets and variables"** → **"Actions"**
3. Click green **"New repository secret"** button
4. Fill in:
   - **Name:** `GROQ_API_KEY` (exactly like this, all caps)
   - **Secret:** Paste your Groq API key from Step 1
5. Click **"Add secret"**

✅ **Done!** Your API key is now securely stored.

---

## ✅ Step 4: Enable GitHub Actions (1 minute)

1. Click **"Actions"** tab (top menu)
2. You'll see a message about workflows
3. Click **"I understand my workflows, go ahead and enable them"**

✅ **Done!** Automation is now enabled.

---

## ✅ Step 5: Run Your First Scrape (2 minutes)

1. Still in **"Actions"** tab
2. Click **"Monthly MF Scraper"** (in left sidebar)
3. Click **"Run workflow"** button (right side)
4. Click green **"Run workflow"** button in popup
5. **Wait 5-10 minutes** (refresh page to see progress)
6. When done, you'll see a green checkmark ✅

✅ **Done!** Your first scrape is complete!

---

## ✅ Step 6: Download Your Data (2 minutes)

1. Click on the completed workflow run (green checkmark)
2. Scroll down to **"Artifacts"** section
3. Click **"mutual-fund-holdings"** to download ZIP file
4. Extract the ZIP file
5. Open the CSV file in Excel/Google Sheets

✅ **Done!** You now have your mutual fund data!

---

## 🎉 Congratulations!

You've successfully set up your automated mutual fund scraper!

### What Happens Now?

- ✅ Scraper runs **automatically on 10th of every month**
- ✅ You get fresh data without doing anything
- ✅ Data is stored for 90 days in GitHub
- ✅ You can run it manually anytime from Actions tab

---

## 📊 Understanding Your Data

The CSV file contains these columns:

| Column | What It Means |
|--------|---------------|
| `amc` | Mutual fund company name |
| `scheme_name` | Name of the mutual fund scheme |
| `stock_name` | Company whose stock is held |
| `isin` | Unique stock identifier |
| `quantity` | Number of shares held |
| `market_value` | Total value in ₹ |
| `weight_percent` | % of total portfolio |
| `scraped_date` | When data was collected |

---

## 🔧 Customization (Optional)

### Add More AMCs

1. Edit `amc_urls.json` file
2. Add new AMC with format:
```json
"AMC Name": "https://amc-website.com/portfolio"
```
3. Commit changes
4. Next run will include new AMC

### Change Schedule

1. Edit `.github/workflows/scraper.yml`
2. Change cron schedule:
```yaml
- cron: '0 3 10 * *'  # 10th of month at 3 AM
```
To run on 1st: `'0 3 1 * *'`
To run weekly: `'0 3 * * 1'` (every Monday)

---

## ❓ Troubleshooting

### "Workflow failed" ❌

**Possible reasons:**
1. **API key not set correctly**
   - Go to Settings → Secrets → Check `GROQ_API_KEY` exists
   - Make sure you copied the full key

2. **AMC website is down**
   - Normal - some AMCs may fail
   - Check which AMC failed in logs
   - Will work next time

3. **Rate limit exceeded**
   - Groq free tier: 14,400 requests/day
   - Wait 24 hours and try again

### "No artifacts" 📦

- Workflow must complete successfully (green ✅)
- If workflow failed (red ❌), fix error first
- Artifacts appear only after successful run

### "Empty CSV file" 📄

- Some AMCs may not have data available
- Try running again in a few days
- Check `amc_urls.json` for correct URLs

---

## 💡 Pro Tips

1. **Run manually first** before waiting for monthly schedule
2. **Download data immediately** - artifacts expire after 90 days
3. **Star this repo** ⭐ to find it easily later
4. **Check Actions tab** on 10th of each month to verify it ran

---

## 🆘 Need Help?

1. Check [Issues](../../issues) tab for similar problems
2. Create new issue with:
   - What you tried
   - Error message (screenshot)
   - Which step failed
3. Community will help!

---

## 🎯 Next Steps

Now that you have the data, you can:

1. **Analyze in Excel/Google Sheets**
   - Find which stocks are most held
   - Track changes month-over-month
   - Identify investment trends

2. **Upload to Database** (Advanced)
   - Use PostgreSQL/MySQL
   - Build dashboards with Tableau/PowerBI
   - Create automated reports

3. **Share with Others**
   - Export specific data
   - Create visualizations
   - Help the investment community

---

**Happy Investing! 📈**
