# 🚀 Setup Instructions

Follow these steps to get your automated crypto news site running:

## ✅ Quick Setup Checklist

### 1. Enable GitHub Pages
- [ ] Go to your repository on GitHub
- [ ] Click **Settings** tab
- [ ] Scroll down to **Pages** section
- [ ] Under **Source**, select **"GitHub Actions"**
- [ ] Click **Save**

### 2. Get NewsAPI Key (Free)
- [ ] Visit [NewsAPI.org](https://newsapi.org/)
- [ ] Click **"Get API Key"**
- [ ] Create a free account
- [ ] Copy your API key

### 3. Add API Keys to GitHub Secrets
- [ ] Go to your repository **Settings**
- [ ] Click **Secrets and variables** → **Actions**
- [ ] Click **New repository secret**
- [ ] Add secret named: `NEWS_API_KEY`
- [ ] Paste your NewsAPI key as the value
- [ ] Click **Add secret**

### 4. Trigger First Run
- [ ] Go to **Actions** tab in your repository
- [ ] Click **"Update Crypto Data and News"** workflow
- [ ] Click **"Run workflow"** button
- [ ] Click **"Run workflow"** (green button)
- [ ] Wait 2-3 minutes for completion

### 5. View Your Live Site
Your site will be available at:
```
https://nagesh00.github.io/crypto-binance
```

## 🔧 Optional Configuration

### Add Binance API Key (Optional)
For higher rate limits, add a Binance API key:
- [ ] Create account at [Binance.com](https://binance.com)
- [ ] Generate API key (read-only permissions)
- [ ] Add as GitHub secret: `BINANCE_API_KEY`

### Customize Update Frequency
Edit `.github/workflows/main.yml` line 8:
```yaml
- cron: '0 */2 * * *'  # Every 2 hours (current)
- cron: '0 * * * *'    # Every hour
- cron: '0 */6 * * *'  # Every 6 hours
```

### Customize Tracked Coins
Edit `update_content.py` line 10:
```python
COIN_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]
# Add more coins like: "LINKUSDT", "ADAUSDT", "DOTUSDT"
```

## 🎯 Expected Results

After setup, your site will automatically:
- ✅ Update market data every 2 hours
- ✅ Fetch latest crypto news articles
- ✅ Generate market analysis posts
- ✅ Display interactive price charts
- ✅ Work on mobile and desktop

## 🚨 Troubleshooting

### Site Not Loading?
1. Check GitHub Pages is enabled
2. Wait 5-10 minutes after first push
3. Check Actions tab for build errors

### No Market Data?
1. Wait for first workflow run to complete
2. Check Actions logs for API errors
3. Binance API might be temporarily down

### No News Articles?
1. Verify `NEWS_API_KEY` is set correctly
2. Check your NewsAPI quota at newsapi.org
3. Free tier has 1000 requests/day limit

### Workflow Failing?
1. Check GitHub Actions logs
2. Verify all secrets are set
3. Fork the repo again if issues persist

## 📞 Need Help?

1. Check the [README.md](README.md) for detailed docs
2. Look at GitHub Actions logs for errors
3. Create an issue in the repository
4. Make sure all prerequisites are met

---

**🎉 Once complete, you'll have a fully automated crypto news and data website!**
