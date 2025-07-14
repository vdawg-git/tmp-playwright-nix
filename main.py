from fastapi import FastAPI, HTTPException
import asyncio
import os
import sys

from browser_use.browser.browser import Browser

app = FastAPI()

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

async def test_browser_immediately():
    """Test browser functionality right away"""
    print("🔍 Testing browser functionality...")
    
    try:
        browser = Browser()
        print(f"✅ Browser initialized. Connected: {browser.is_connected}")
        
        # Test actual page navigation
        page = await browser.get_current_page()
        print("✅ Got current page")
        
        await page.goto("https://example.com")
        print("✅ Navigated to example.com")
        
        title = await page.title()
        print(f"✅ Page title: {title}")
        
        url = page.url
        print(f"✅ Current URL: {url}")
        
        # Close browser
        await browser.close()
        print("✅ Browser closed successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Browser test failed: {e}")
        print(f"❌ Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

@app.get("/")
async def root():
    return {"message": "Browser test API is running"}

if __name__ == "__main__":
    import uvicorn
    
    # Test browser immediately
    print("Starting browser test...")
    success = asyncio.run(test_browser_immediately())
    
    if success:
        print("🎉 Browser test passed! Starting FastAPI server...")
    else:
        print("💥 Browser test failed! Starting server anyway for debugging...")
    
    uvicorn.run(app, host="0.0.0.0", port=9000)