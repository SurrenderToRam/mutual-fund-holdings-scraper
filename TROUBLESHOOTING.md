# 🔧 Troubleshooting Guide

**Having problems? Find solutions here!**

---

## ❌ Common Errors & Solutions

### 1. "Workflow Failed" - Red X

**Possible Causes:**

#### A) API Key Not Set

**Symptoms:**
- Error message mentions `GROQ_API_KEY`
- Workflow fails immediately

**Solution:**
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Check if `GROQ_API_KEY` exists
3. If not, add it:
   - Name: `GROQ_API_KEY` (exactly, all caps)
   - Value: Your Groq API key
4. Run workflow again

---

#### B) Invalid API Key

**Symptoms:**
- Error: "Invalid API key" or "Authentication failed"

**Solution:**
1. Go to https://groq.com
2. Login → API Keys
3. Create NEW API key
4. Update in GitHub Secrets
5. Run workflow again

---

#### C) Rate Limit Exceeded

**Symptoms:**
- Error: "Rate limit exceeded"
- Workflow runs for a while then fails

**Solution:**
- **Wait 24 hours** - Groq free tier resets daily
- Or upgrade to Groq paid tier (optional)
- Or reduce number of AMCs in `amc_urls.json`

---

### 2. "No Artifacts" - Can't Download Data

**Possible Causes:**

#### A) Workflow Still Running

**Symptoms:**
- Yellow circle icon (in progress)
- No artifacts section yet

**Solution:**
- **Wait!** Workflow takes 5-10 minutes
- Refresh page every minute
- Artifacts appear only after completion

---

#### B) Workflow Failed

**Symptoms:**
- Red X icon
- Artifacts section doesn't appear

**Solution:**
- Fix the error first (see error message)
- Re-run workflow
- Artifacts only created on successful run

---

### 3. "Empty CSV File" or "No Data"

**Possible Causes:**

#### A) AMC Websites Down

**Symptoms:**
- CSV file exists but has few/no rows
- Logs show "Error scraping [AMC Name]"

**Solution:**
- **Normal!** Some AMCs may be temporarily down
- Check which AMCs failed in workflow logs
- Run again in 1-2 days
- Most AMCs should work

---

#### B) Wrong URLs

**Symptoms:**
- All AMCs fail
- Logs show 404 errors

**Solution:**
1. Check `amc_urls.json`
2. Verify URLs are correct
3. Update if AMC changed their website
4. Commit changes
5. Run workflow again

---

### 4. "Actions Not Enabled"

**Symptoms:**
- Can't see "Run workflow" button
- Actions tab shows message

**Solution:**
1. Go to **Actions** tab
2. Click **"I understand my workflows, go ahead and enable them"**
3. Refresh page
4. Try again

---

### 5. "Permission Denied" Errors

**Symptoms:**
- Error about permissions
- Can't commit or push

**Solution:**
1. Make sure you **forked** the repo (not just viewing original)
2. Check you're in YOUR fork (URL should have your username)
3. If in original repo, click "Fork" button
4. Work in your fork

---

## 🐛 Debugging Steps

### Step 1: Check Workflow Logs

1. Go to **Actions** tab
2. Click on failed workflow run
3. Click on "scrape" job
4. Expand each step to see errors
5. Look for red error messages

### Step 2: Verify Setup

**Checklist:**
- [ ] Forked repository (not original)
- [ ] API key added to Secrets
- [ ] API key name is exactly `GROQ_API_KEY`
- [ ] Actions enabled
- [ ] Workflow file exists in `.github/workflows/`

### Step 3: Test API Key

**Verify your Groq API key works:**

1. Go to https://groq.com
2. Login
3. Go to Playground
4. Try a simple query
5. If it works, key is valid

### Step 4: Check AMC URLs

**Verify URLs are accessible:**

1. Open `amc_urls.json`
2. Copy a URL
3. Paste in browser
4. Check if page loads
5. If 404, URL needs updating

---

## 📊 Understanding Error Messages

### "ModuleNotFoundError: No module named 'scrapegraphai'"

**Meaning:** Required library not installed

**Solution:**
- Should auto-install from `requirements.txt`
- If persists, check `requirements.txt` exists
- Re-run workflow

---

### "HTTPError: 404 Not Found"

**Meaning:** AMC website URL is wrong or page moved

**Solution:**
1. Find which AMC from logs
2. Google: "[AMC Name] portfolio download"
3. Update URL in `amc_urls.json`
4. Commit and re-run

---

### "Timeout Error"

**Meaning:** AMC website too slow or down

**Solution:**
- **Normal!** Some sites are slow
- Will be skipped automatically
- Try again next run
- Other AMCs will still work

---

### "JSONDecodeError"

**Meaning:** AI response format issue

**Solution:**
- Usually temporary
- Re-run workflow
- If persists, that AMC may need manual URL update

---

## 🔍 Advanced Troubleshooting

### Enable Debug Mode

**Add debug logging:**

1. Edit `scraper.py`
2. Add at top:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
3. Commit changes
4. Run workflow
5. Check logs for detailed output

---

### Test Locally (For Developers)

**Run on your computer:**

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mutual-fund-holdings-scraper.git
cd mutual-fund-holdings-scraper

# Install dependencies
pip install -r requirements.txt

# Set API key
export GROQ_API_KEY="your_key_here"

# Run scraper
python scraper.py
```

---

### Check Individual AMC

**Test one AMC at a time:**

1. Edit `amc_urls.json`
2. Keep only 1 AMC
3. Run workflow
4. Check if it works
5. Add more AMCs one by one

---

## 💡 Prevention Tips

### Avoid Common Mistakes

1. **Don't share your API key**
   - Keep it in GitHub Secrets only
   - Never commit to code

2. **Don't edit original repo**
   - Always work in your fork
   - Original repo is read-only for you

3. **Don't run too frequently**
   - Respect rate limits
   - Once a month is enough
   - Manual runs: max 2-3 per day

4. **Don't ignore errors**
   - Check logs after each run
   - Fix issues promptly
   - Some errors are normal (AMC down)

---

## 📞 Still Stuck?

### Before Creating Issue:

**Gather this information:**

1. **What you tried:**
   - Exact steps you followed
   - Which guide you used

2. **Error message:**
   - Full error text
   - Screenshot of error
   - Which step failed

3. **Your setup:**
   - Did you fork the repo?
   - Is API key set?
   - Are Actions enabled?

4. **Workflow logs:**
   - Copy relevant error lines
   - Include full stack trace

### Create Issue:

1. Go to [Issues](../../issues)
2. Click "New Issue"
3. Title: Brief description
4. Body: Include all info above
5. Add screenshots if helpful

**We'll help you within 24 hours!**

---

## 🎯 Quick Fixes

### "Just want it to work!"

**Nuclear option (start fresh):**

1. Delete your fork
2. Fork again from original
3. Follow [YOUR_NEXT_STEPS.md](YOUR_NEXT_STEPS.md) exactly
4. Don't skip any steps
5. Should work!

---

### "Worked before, now broken"

**Possible causes:**

1. **AMC website changed**
   - Update URLs in `amc_urls.json`

2. **API key expired**
   - Create new key on Groq
   - Update in GitHub Secrets

3. **GitHub Actions issue**
   - Check GitHub status: https://www.githubstatus.com
   - Wait and try again

---

## 📚 Additional Resources

### Helpful Links:

- **GitHub Actions Status:** https://www.githubstatus.com
- **Groq Status:** https://status.groq.com
- **GitHub Docs:** https://docs.github.com/en/actions
- **Python Errors:** https://docs.python.org/3/library/exceptions.html

### Video Tutorials:

- [GitHub Actions Basics](https://www.youtube.com/results?search_query=github+actions+tutorial)
- [Debugging Workflows](https://www.youtube.com/results?search_query=debug+github+actions)

---

## ✅ Success Checklist

**If everything works, you should see:**

- [ ] Green checkmark ✅ on workflow
- [ ] "Artifacts" section appears
- [ ] Can download ZIP file
- [ ] CSV file has data (rows > 0)
- [ ] Data looks correct (stock names, values, etc.)

**If all checked, you're good to go!** 🎉

---

*Still having issues? [Create an Issue](../../issues/new) - we're here to help!*
