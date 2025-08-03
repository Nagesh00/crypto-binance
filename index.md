---
layout: default
title: "Crypto News & Market Data"
---

# 🪙 Crypto News & Market Data

Welcome to your automated cryptocurrency tracking website!

## 📊 Market Overview

<div id="market-data">
  <p>Loading market data...</p>
</div>

## 📈 Live Chart

<div style="height: 400px; width: 100%;">
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <div id="tradingview_widget"></div>
  <script type="text/javascript">
  new TradingView.widget({
    "autosize": true,
    "symbol": "BINANCE:BTCUSDT",
    "interval": "1H",
    "timezone": "Etc/UTC",
    "theme": "light",
    "style": "1",
    "locale": "en",
    "enable_publishing": false,
    "container_id": "tradingview_widget"
  });
  </script>
</div>

<script>
// Load market data if available
fetch('./_data/market_data.json')
  .then(response => response.json())
  .then(data => {
    if (data.coins) {
      let html = '<table border="1"><tr><th>Symbol</th><th>Price</th><th>Change %</th></tr>';
      data.coins.forEach(coin => {
        html += `<tr><td>${coin.symbol}</td><td>$${coin.lastPrice}</td><td>${coin.priceChangePercent}%</td></tr>`;
      });
      html += '</table>';
      document.getElementById('market-data').innerHTML = html;
    }
  })
  .catch(error => {
    document.getElementById('market-data').innerHTML = '<p>Market data will load after first automation run.</p>';
  });
</script>

---

## 🔧 Site Status

- **Last Updated**: Auto-updated every 2 hours
- **Data Source**: Binance API + News APIs  
- **Hosting**: GitHub Pages
- **URL**: [https://nagesh00.github.io/crypto-binance](https://nagesh00.github.io/crypto-binance)
