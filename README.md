# ⚡ StackPulse

**StackPulse** is a high-performance Technographic Discovery API. It identifies the underlying software, frameworks, and marketing tools used by any website in real-time.

### 🚀 Features
- **Instant Tech Detection:** Identify 50+ common e-commerce, analytics, and frontend stacks.
- **Lightweight & Fast:** Optimized for sub-second response times.
- **B2B Ready:** Designed for seamless integration into lead enrichment workflows.

### 🛠️ Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Infrastructure:** [Railway](https://railway.app/)
- **Marketplace:** [RapidAPI](https://rapidapi.com/)

### 📖 Usage
`GET /detect?url=google.com`

**Response Example:**
```json
{
  "url": "[https://example.com](https://example.com)",
  "stack": [
    {"technology": "Shopify", "category": "E-commerce"},
    {"technology": "Meta Pixel", "category": "Analytics"}
  ],
  "count": 2
}
