# 🚀 Automated Crypto News & Market Data Website

A fully automated cryptocurrency news and market data website powered by Jekyll, GitHub Actions, and external APIs. The site automatically fetches real-time market data from Binance and crypto news from various sources, then builds and deploys updates to GitHub Pages.

## 🌟 Features

### 📊 Real-Time Market Data
- Live cryptocurrency prices from Binance API
- 24-hour price changes, volume, and market statistics
- Interactive TradingView charts and widgets
- Market summary and analytics
- Support for 8+ major cryptocurrencies (BTC, ETH, BNB, SOL, XRP, ADA, DOT, LINK)

### 📰 Automated News Feed
- Automatically fetches latest crypto news every 2 hours
- Sources from reputable crypto news outlets
- Categorized articles with search and filter functionality
- Full article previews with source attribution
- Responsive card-based layout

### 🤖 Full Automation
- **GitHub Actions** workflow runs every 2 hours
- **Python scripts** fetch and process data
- **Jekyll** builds static site with new content
- **GitHub Pages** automatically deploys updates
- Zero manual intervention required

### 💻 Modern Web Interface
- Responsive Bootstrap 5 design
- Mobile-friendly interface
- Fast loading static site
- SEO optimized
- Professional cryptocurrency theme

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub Actions│    │   Python Scripts │    │     APIs        │
│   (Scheduler)   │───▶│   Data Fetcher   │───▶│   Binance API   │
│   Every 2hrs    │    │                  │    │   News API      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │
         │                       ▼
         │              ┌──────────────────┐
         │              │   Generated      │
         │              │   Content        │
         │              │   (.md files)    │
         │              └──────────────────┘
         │                       │
         ▼                       │
┌─────────────────┐              │
│     Jekyll      │◀─────────────┘
│  Static Site    │
│   Generator     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  GitHub Pages   │
│   (Live Site)   │
└─────────────────┘
```

## 🚀 Quick Setup

### Prerequisites
- GitHub account
- NewsAPI.org account (free tier available)
- Basic understanding of GitHub repositories

### 1. Repository Setup
```bash
# Clone or fork this repository
git clone https://github.com/Nagesh00/crypto-binance.git
cd crypto-binance

# Or fork via GitHub web interface
```

### 2. Configure API Keys
Go to your GitHub repository → Settings → Secrets and Variables → Actions

Add these repository secrets:
- `NEWS_API_KEY`: Your API key from [NewsAPI.org](https://newsapi.org)
- `BINANCE_API_KEY`: (Optional) For higher rate limits

### 3. Enable GitHub Pages
1. Go to repository Settings → Pages
2. Source: "GitHub Actions"
3. Save

### 4. Trigger First Run
1. Go to Actions tab
2. Select "Update Crypto Data and News" workflow
3. Click "Run workflow"
4. Wait for completion (2-3 minutes)

Your site will be live at: `https://yourusername.github.io/crypto-binance`

## 📁 Project Structure

```
crypto-binance/
├── _config.yml              # Jekyll configuration
├── _layouts/                # Page templates
│   ├── default.html         # Main layout
│   └── post.html           # Article layout
├── _posts/                  # Generated news articles
├── _data/                   # Market data storage
│   └── market_data.json    # Live market data
├── .github/workflows/       # Automation
│   └── main.yml            # GitHub Actions workflow
├── update_content.py        # Data fetching script
├── requirements.txt         # Python dependencies
├── index.html              # Homepage
├── market.html             # Market data page
├── news.html               # News page
├── Gemfile                 # Ruby dependencies
└── README.md               # This file
```

## 🔧 Configuration

### Customize Tracked Cryptocurrencies
Edit `update_content.py`:
```python
COIN_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]
# Add/remove cryptocurrency pairs as needed
```

### Adjust Update Frequency
Edit `.github/workflows/main.yml`:
```yaml
schedule:
  - cron: '0 */2 * * *'  # Every 2 hours
  # Change to '0 * * * *' for hourly updates
```

### Customize News Sources
Edit `update_content.py`:
```python
params = {
    'domains': 'coindesk.com,cointelegraph.com,decrypt.co,theblock.co'
    # Add/modify news domains
}
```

## 🛠️ Local Development

### Prerequisites
- Python 3.8+
- Ruby 2.7+
- Jekyll

### Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Ruby dependencies
bundle install

# Set environment variables
export NEWS_API_KEY="your_api_key_here"

# Run data fetching script
python update_content.py

# Serve Jekyll site locally
bundle exec jekyll serve

# Visit: http://localhost:4000
```

## 📊 Data Sources

### Market Data
- **Binance API**: Real-time cryptocurrency prices
- **Endpoint**: `https://api.binance.com/api/v3/ticker/24hr`
- **Rate Limit**: 1200 requests/minute (no API key required)
- **Data**: Price, volume, 24h change, high/low

### News Data
- **NewsAPI.org**: Cryptocurrency news articles
- **Rate Limit**: 1000 requests/day (free tier)
- **Sources**: CoinDesk, CoinTelegraph, Decrypt, The Block
- **Data**: Title, description, publication date, source

### Charts
- **TradingView**: Interactive price charts
- **Free widgets**: No API key required
- **Real-time**: Live price data and technical indicators

## 🔒 Security & Best Practices

### API Key Management
- Store all API keys in GitHub Secrets
- Never commit API keys to repository
- Use environment variables in scripts
- Regularly rotate API keys

### Rate Limiting
- Respect API rate limits
- Implement proper error handling
- Use caching when appropriate
- Monitor API usage

### Content Moderation
- Automated content from trusted sources only
- Filter inappropriate content
- Source attribution for all articles
- Regular monitoring of generated content

## 🚨 Troubleshooting

### Common Issues

#### Workflow Fails
```bash
# Check GitHub Actions logs
# Verify API keys are set correctly
# Ensure rate limits aren't exceeded
```

#### No Market Data
```bash
# Binance API might be temporarily unavailable
# Check _data/market_data.json exists
# Verify COIN_SYMBOLS are valid trading pairs
```

#### No News Articles
```bash
# Verify NEWS_API_KEY is valid
# Check API quota usage at newsapi.org
# Ensure news domains are accessible
```

#### Site Not Building
```bash
# Check Jekyll build logs in Actions
# Verify _config.yml syntax
# Ensure all required files exist
```

## 📈 Performance Optimization

### Site Speed
- Static site generation for fast loading
- Optimized images and assets
- CDN delivery via GitHub Pages
- Minimal external dependencies

### SEO Optimization
- Semantic HTML structure
- Meta tags and descriptions
- Sitemap generation
- Mobile-responsive design

### Automation Efficiency
- Efficient API calls
- Smart caching strategies
- Error handling and retries
- Minimal resource usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Development Guidelines
- Follow PEP 8 for Python code
- Use semantic HTML and responsive design
- Test all API integrations
- Document new features
- Maintain backward compatibility

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Binance** for providing free market data API
- **NewsAPI.org** for cryptocurrency news feeds
- **TradingView** for interactive chart widgets
- **Jekyll** for the static site generator
- **GitHub** for Actions and Pages hosting
- **Bootstrap** for the responsive UI framework

## 📞 Support

- Create an issue for bugs or feature requests
- Check existing issues before creating new ones
- Provide detailed information for debugging
- Consider contributing fixes yourself

---

**Happy Trading! 📈🚀**

*Remember: This is for informational purposes only. Always do your own research before making investment decisions.*
