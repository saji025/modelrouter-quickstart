# ModelRouter AI Gateway - Quickstart & Integration Guide

[![ModelRouter](https://img.shields.io/badge/Platform-ModelRouter-7c5cff.svg)](https://modelrouter.web.id)
[![Base URL](https://img.shields.io/badge/OpenAI--Compatible-https%3A%2F%2Fmodelrouter.web.id%2Fv1-22d3ee.svg)](https://modelrouter.web.id)
[![Payment](https://img.shields.io/badge/Deposit-QRIS%2024%2F7-4ade80.svg)](https://modelrouter.web.id/wallet)

Official quickstart guide and developer configurations for [ModelRouter](https://modelrouter.web.id) — Unified OpenAI-compatible API Gateway for 90+ flagship LLMs (DeepSeek V4, Claude Sonnet/Fable, Gemini 3.8 Flash, GPT-5, Qwen, GLM-5).

---

## ⚡ Highlights

- **Unified OpenAI SDK Endpoint:** Point any client or coding agent directly to `https://modelrouter.web.id/v1`.
- **Instant 1-Tap Login:** Sign in with Google Account, GitHub, or Telegram at [https://modelrouter.web.id/login](https://modelrouter.web.id/login).
- **Official Prompt Caching:** Up to 90% cost savings for Cursor, Cline, and Roo Code agent loops.
- **QRIS Auto Top-Up:** Instant deposit 24/7 starting from $1 (Rp 17.800) via GoPay, OVO, DANA, BCA, Mandiri, etc.
- **Free Tier Available:** Limited free models for prototyping (`hy3-free`, `glm-5.3-free`, `deepseek-v4-flash-free`).

---

## 🚀 Quickstart (Python)

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MODELROUTER_API_KEY", # Get at https://modelrouter.web.id/token
    base_url="https://modelrouter.web.id/v1"
)

response = client.chat.completions.create(
    model="deepseek-v4-flash", # or claude-sonnet-4.6, gemini-3.8-flash, hy3-free
    messages=[
        {"role": "system", "content": "You are an elite coding assistant."},
        {"role": "user", "content": "Explain how prompt caching saves token costs."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

---

## 💻 Cursor / Cline / Roo Code Setup

### Cursor Configuration
1. Open Cursor Settings -> **Models**
2. Enable **OpenAI API Key**
3. Override Base URL:
   ```text
   https://modelrouter.web.id/v1
   ```
4. Paste your ModelRouter Token from [https://modelrouter.web.id/token](https://modelrouter.web.id/token)
5. Add your favorite models:
   - `claude-sonnet-4.6`
   - `deepseek-v4-flash`
   - `gemini-3.8-flash`
   - `gpt-5.4-mini`

---

## 📚 Resources & Support

- **Website & Dashboard:** [https://modelrouter.web.id](https://modelrouter.web.id)
- **API Documentation:** [https://modelrouter.web.id/docs](https://modelrouter.web.id/docs)
- **Model Pricing:** [https://modelrouter.web.id/pricing](https://modelrouter.web.id/pricing)
- **Telegram Updates:** [https://t.me/modelrouter_info](https://t.me/modelrouter_info)
