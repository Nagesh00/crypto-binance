#!/usr/bin/env python3
"""
Debug script to check all components of the crypto site
"""
import os
import json
import sys

def check_file(filepath, description):
    """Check if a file exists and show its status"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"✅ {description}: {filepath} ({size} bytes)")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_directory(dirpath, description):
    """Check if a directory exists and list its contents"""
    if os.path.exists(dirpath):
        files = os.listdir(dirpath)
        print(f"✅ {description}: {dirpath} ({len(files)} files)")
        for f in files[:5]:  # Show first 5 files
            print(f"   - {f}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more")
        return True
    else:
        print(f"❌ {description}: {dirpath} - NOT FOUND")
        return False

def check_json_file(filepath, description):
    """Check if a JSON file is valid"""
    if check_file(filepath, description):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            print(f"   📊 JSON is valid, contains {len(data.get('coins', []))} coins")
            return True
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON is invalid: {e}")
            return False
    return False

def main():
    print("🔍 DEBUGGING CRYPTO SITE PROJECT")
    print("=" * 50)
    
    issues = []
    
    # Check core files
    print("\n📁 CORE FILES:")
    if not check_file("index.html", "Main page"):
        issues.append("Missing index.html")
    if not check_file("_config.yml", "Jekyll config"):
        issues.append("Missing Jekyll config")
    if not check_file("update_content.py", "Data update script"):
        issues.append("Missing update script")
    
    # Check directories
    print("\n📂 DIRECTORIES:")
    if not check_directory("_data", "Data directory"):
        issues.append("Missing _data directory")
    if not check_directory("_layouts", "Layout templates"):
        issues.append("Missing _layouts directory")
    if not check_directory(".github/workflows", "GitHub Actions"):
        issues.append("Missing workflows directory")
    
    # Check data files
    print("\n📊 DATA FILES:")
    if not check_json_file("_data/market_data.json", "Market data"):
        issues.append("Invalid or missing market data")
    
    # Check workflow files
    print("\n⚙️ WORKFLOWS:")
    workflow_files = []
    if os.path.exists(".github/workflows"):
        for f in os.listdir(".github/workflows"):
            if f.endswith('.yml') and not f.endswith('.disabled'):
                workflow_files.append(f)
                check_file(f".github/workflows/{f}", f"Workflow: {f}")
    
    if not workflow_files:
        issues.append("No active workflow files found")
    
    # Check environment variables (simulation)
    print("\n🔑 ENVIRONMENT VARIABLES:")
    binance_key = os.environ.get("BINANCE_API_KEY")
    news_key = os.environ.get("NEWS_API_KEY")
    
    if binance_key:
        print(f"✅ BINANCE_API_KEY: Set (ends with ...{binance_key[-4:]})")
    else:
        print("⚠️  BINANCE_API_KEY: Not set (GitHub Secrets required)")
    
    if news_key:
        print(f"✅ NEWS_API_KEY: Set (ends with ...{news_key[-4:]})")
    else:
        print("⚠️  NEWS_API_KEY: Not set (GitHub Secrets required)")
    
    # Summary
    print("\n" + "=" * 50)
    if issues:
        print("❌ ISSUES FOUND:")
        for issue in issues:
            print(f"   - {issue}")
        print(f"\n🔧 {len(issues)} issue(s) need to be fixed.")
        return 1
    else:
        print("✅ ALL CHECKS PASSED!")
        print("\n🚀 Your crypto site should deploy successfully!")
        print("\nNext steps:")
        print("1. Add API keys to GitHub Secrets")
        print("2. Push changes to trigger deployment")
        print("3. Check GitHub Actions for deployment status")
        return 0

if __name__ == "__main__":
    sys.exit(main())
