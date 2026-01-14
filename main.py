from fastapi import FastAPI, HTTPException, Header, Depends
import httpx
import re
import os

app = FastAPI(title="StackPulse API")

# Security: Set this in Railway Environment Variables
RAPIDAPI_PROXY_SECRET = os.getenv("RAPIDAPI_PROXY_SECRET")

# signature database
SIGNATURES = {
    "E-commerce": {"Shopify": r"cdn\.shopify\.com", "WooCommerce": r"woocommerce", "Magento": r"static/frontend/Magento"},
    "Analytics": {"Google Analytics": r"googletagmanager\.com/gtag/js", "Meta Pixel": r"connect\.facebook\.net", "Hotjar": r"static\.hotjar\.com"},
    "Frontend": {"WordPress": r"wp-content|wp-includes", "Next.js": r"_next/static", "React": r"data-reactroot", "Webflow": r"uploads\.ssl\.webflow\.com"}
}

async def verify_rapidapi(x_rapidapi_proxy_secret: str = Header(None)):
    if x_rapidapi_proxy_secret != RAPIDAPI_PROXY_SECRET:
        raise HTTPException(status_code=403, detail="Direct access restricted")

@app.get("/detect")
async def detect_stack(url: str, _ = Depends(verify_rapidapi)):
    if not url.startswith("http"):
        url = f"https://{url}"
        
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        try:
            res = await client.get(url)
            content = res.text + str(res.headers)
            
            found = []
            for category, techs in SIGNATURES.items():
                for name, pattern in techs.items():
                    if re.search(pattern, content, re.IGNORECASE):
                        found.append({"technology": name, "category": category})
            
            return {"url": url, "stack": found, "count": len(found)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
