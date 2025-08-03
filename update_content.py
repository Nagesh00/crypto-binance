import os
import requests
import json
from datetime import datetime
import re

# --- CONFIGURATION ---
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/24hr"
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # Get key from GitHub Secrets
COIN_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "ADAUSDT", "DOTUSDT", "LINKUSDT"]
POSTS_DIR = "_posts"
DATA_DIR = "_data"

# --- 1. FETCH AND SAVE CRYPTO MARKET DATA ---
def fetch_market_data():
    """Fetches 24hr ticker data from Binance for specified coins."""
    print("Fetching market data from Binance...")
    try:
        params = {'symbols': json.dumps(COIN_SYMBOLS)}
        response = requests.get(BINANCE_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        market_data = response.json()

        # Save data to a file for the website to use
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        # Add timestamp to the data
        enriched_data = {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "coins": market_data
        }
        
        with open(os.path.join(DATA_DIR, 'market_data.json'), 'w') as f:
            json.dump(enriched_data, f, indent=4)
        print(f"Successfully saved market data for {len(market_data)} coins.")
        return market_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Binance API: {e}")
        return None

# --- 2. FETCH AND CREATE NEWS ARTICLE POSTS ---
def create_news_posts():
    """Fetches crypto news and creates Markdown post files."""
    print("Fetching news articles...")
    if not NEWS_API_KEY:
        print("Warning: NEWS_API_KEY is not set. Skipping news posts.")
        return

    try:
        params = {
            'q': 'crypto OR bitcoin OR ethereum OR "digital currency" OR blockchain',
            'sortBy': 'publishedAt',
            'pageSize': 5,  # Fetch the 5 latest articles
            'apiKey': NEWS_API_KEY,
            'language': 'en',
            'domains': 'coindesk.com,cointelegraph.com,decrypt.co,theblock.co'  # Reputable crypto news sources
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get('articles', [])

        if not os.path.exists(POSTS_DIR):
            os.makedirs(POSTS_DIR)

        for article in articles:
            # Skip articles without proper content
            if not article.get('title') or not article.get('description'):
                continue
                
            # Create a unique, filesystem-friendly filename
            title_slug = re.sub(r'[^\w\s-]', '', article['title']).strip()
            title_slug = re.sub(r'[-\s]+', '-', title_slug)
            
            # Parse the published date
            pub_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            filename_date = pub_date.strftime('%Y-%m-%d')
            filename = f"{filename_date}-{title_slug[:50].lower()}.md"  # Limit filename length
            filepath = os.path.join(POSTS_DIR, filename)

            # Avoid creating duplicate posts
            if os.path.exists(filepath):
                print(f"Skipping existing article: {filename}")
                continue

            # Clean up the content
            title = article['title'].replace('"', "'")
            description = article.get('description', '').replace('"', "'")
            author = article.get('source', {}).get('name', 'Unknown')
            image_url = article.get('urlToImage', '')
            
            # Create the Markdown content for the Jekyll post
            content = f"""---
layout: post
title: "{title}"
date: {article['publishedAt']}
author: "{author}"
categories: [crypto, news]
tags: [cryptocurrency, bitcoin, ethereum, blockchain]
image: "{image_url}"
source_url: "{article['url']}"
excerpt: "{description}"
---

{description}

<!--more-->

This article was automatically fetched from {author}. 

[Read the full article at the source]({article['url']})

---
*This post was automatically generated from crypto news sources.*
"""
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Successfully created news post: {filename}")
            except Exception as e:
                print(f"Error creating post {filename}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching from News API: {e}")

# --- 3. CREATE MARKET SUMMARY POST ---
def create_market_summary():
    """Creates a daily market summary post."""
    print("Creating market summary...")
    
    market_data_file = os.path.join(DATA_DIR, 'market_data.json')
    if not os.path.exists(market_data_file):
        print("No market data found, skipping market summary.")
        return
    
    with open(market_data_file, 'r') as f:
        data = json.load(f)
    
    coins = data.get('coins', [])
    if not coins:
        return
    
    # Create market summary
    today = datetime.utcnow().strftime('%Y-%m-%d')
    filename = f"{today}-market-summary.md"
    filepath = os.path.join(POSTS_DIR, filename)
    
    # Don't create duplicate summaries
    if os.path.exists(filepath):
        print("Market summary already exists for today.")
        return
    
    # Calculate some basic stats
    gainers = [coin for coin in coins if float(coin.get('priceChangePercent', 0)) > 0]
    losers = [coin for coin in coins if float(coin.get('priceChangePercent', 0)) < 0]
    
    top_gainer = max(coins, key=lambda x: float(x.get('priceChangePercent', 0)))
    top_loser = min(coins, key=lambda x: float(x.get('priceChangePercent', 0)))
    
    content = f"""---
layout: post
title: "Daily Market Summary - {today}"
date: {datetime.utcnow().isoformat()}Z
author: "Automated Market Analysis"
categories: [crypto, market, analysis]
tags: [market-summary, daily, analysis]
excerpt: "Daily cryptocurrency market summary with price movements and trends"
---

## Market Overview for {today}

**Market Statistics:**
- Gainers: {len(gainers)} coins
- Losers: {len(losers)} coins
- Total tracked: {len(coins)} coins

**Top Performer:** {top_gainer.get('symbol', 'N/A')} (+{float(top_gainer.get('priceChangePercent', 0)):.2f}%)

**Biggest Decline:** {top_loser.get('symbol', 'N/A')} ({float(top_loser.get('priceChangePercent', 0)):.2f}%)

<!--more-->

### Detailed Market Data

| Symbol | Price (USD) | 24h Change | 24h Volume |
|--------|-------------|------------|------------|
"""
    
    # Add table rows for each coin
    for coin in coins:
        symbol = coin.get('symbol', 'N/A')
        price = float(coin.get('lastPrice', 0))
        change = float(coin.get('priceChangePercent', 0))
        volume = float(coin.get('quoteVolume', 0))
        
        change_symbol = "+" if change >= 0 else ""
        content += f"| {symbol} | ${price:.4f} | {change_symbol}{change:.2f}% | ${volume:,.0f} |\n"
    
    content += f"""

---
*Market data provided by Binance API. Last updated: {data.get('last_updated', 'Unknown')}*
"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully created market summary: {filename}")
    except Exception as e:
        print(f"Error creating market summary: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("Starting crypto data update...")
    fetch_market_data()
    create_news_posts()
    create_market_summary()
    print("Script finished successfully!")
