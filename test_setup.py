#!/usr/bin/env python3
"""
Simple test script to validate the site setup without external API calls
"""
import os
import json
from datetime import datetime, timezone

def create_test_data():
    """Create test data files to ensure Jekyll can build"""
    
    # Ensure directories exist
    os.makedirs('_data', exist_ok=True)
    os.makedirs('_posts', exist_ok=True)
    
    # Create test market data
    test_market_data = {
        "last_updated": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "coins": [
            {
                "symbol": "BTCUSDT",
                "lastPrice": "65000.00",
                "priceChangePercent": "2.50",
                "highPrice": "66000.00",
                "lowPrice": "64000.00",
                "quoteVolume": "1500000000"
            },
            {
                "symbol": "ETHUSDT",
                "lastPrice": "3200.00",
                "priceChangePercent": "1.80",
                "highPrice": "3250.00",
                "lowPrice": "3150.00",
                "quoteVolume": "800000000"
            }
        ]
    }
    
    with open('_data/market_data.json', 'w') as f:
        json.dump(test_market_data, f, indent=2)
    
    print("✅ Created test market data")

if __name__ == "__main__":
    create_test_data()
    print("✅ Test setup complete!")
