# ModelRouter AI Gateway - Panduan Integrasi & Setup Cepat (Indonesia)

[![ModelRouter](https://img.shields.io/badge/ModelRouter-Official_Website-indigo?style=for-the-badge)](https://modelrouter.id)
[![Bansos AI](https://img.shields.io/badge/Bansos_AI-Free_100_Req-amber?style=for-the-badge)](https://modelrouter.id/bansos-ai)
[![Models](https://img.shields.io/badge/Models-Frontier_Catalog-emerald?style=for-the-badge)](https://modelrouter.id/models)
[![Billing](https://img.shields.io/badge/Topup-QRIS_Instant-blue?style=for-the-badge)](https://modelrouter.id/billing)

Dokumentasi resmi dan panduan cepat integrasi **[ModelRouter](https://modelrouter.id)** — Universal AI API Gateway di Indonesia. Satu endpoint terpadu untuk mengakses puluhan model AI frontier dunia (Claude Opus 5, Claude Sonnet 4.6, GPT-6 Astra, DeepSeek V4.1, Gemini 3.8 Flash, MiMo V2.5) menggunakan **satu saldo Rupiah (QRIS otomatis 24/7)** tanpa perlu kartu kredit luar negeri.

---

## 🎁 Program Bansos AI (Free Tier 100 Request)

ModelRouter menyediakan kuota uji coba gratis (Bansos AI) bagi para developer, programmer, dan mahasiswa di Indonesia:
- **100 Request Uji Coba Gratis:** Langsung aktif begitu mendaftar tanpa syarat kartu kredit.
- **Model yang Didukung:** DeepSeek V4.1 Flash, MiMo V2.5, Qwen 3.8 Flash, dan Atria Dawn.
- **Klaim Sekarang:** Buka **[https://modelrouter.id/bansos-ai](https://modelrouter.id/bansos-ai)** untuk panduan klaim instan.

---

## ⚡ Kenapa Memilih ModelRouter?

- **Tanpa Kartu Kredit Internasional:** Akses API Claude, GPT, dan DeepSeek tanpa terhalang pembayaran debit/kredit luar negeri.
- **Top-Up Instan Otomatis via QRIS 24/7:** Pengisian saldo instan mulai dari **Rp 5.000** via GoPay, OVO, DANA, ShopeePay, BCA, Mandiri, BRI, BNI, dan seluruh bank.
- **Login 1-Tap Cepat:** Masuk langsung dengan **Google**, **GitHub**, atau email aktif di [https://modelrouter.id/login](https://modelrouter.id/login).
- **100% OpenAI & Anthropic SDK Compatible:** Cukup ganti `base_url` ke `https://modelrouter.id/v1`.
- **Hemat Biaya hingga 95%:** Didukung otomatis prompt caching untuk model reasoning dan coding.

---

## 💻 Panduan Integrasi Tool & Coding Agent

### 1. Cursor AI Editor
1. Buka **Cursor Settings** (`Ctrl + Shift + J` / `Cmd + ,`).
2. Pilih menu **Models**.
3. Di bagian **OpenAI API Key**, masukkan API Key ModelRouter kamu (`sk-mod...`).
4. Pada kolom **Override OpenAI Base URL**, masukkan:
   ```
   https://modelrouter.id/v1
   ```
5. Tambahkan model yang ingin digunakan: `deepseek-v4.1-flash`, `claude-sonnet-4.6`, `claude-opus-5`, dll.

### 2. Hermes Agent (Nous Research)
1. Buka konfigurasi Hermes di `~/.hermes/config.yaml`:
   ```yaml
   model: "deepseek-v4.1-flash"
   provider: "openai-api"
   openai_api:
     base_url: "https://modelrouter.id/v1"
     api_key: "sk-mod..."
   ```
2. Jalankan `hermes` di terminal. Semua tool-calling dan workflow akan langsung berjalan melalui ModelRouter.

### 3. OpenCode
1. Di konfigurasi provider OpenCode, pilih **OpenAI Compatible**.
2. Masukkan Base URL: `https://modelrouter.id/v1`.
3. Masukkan API Key ModelRouter kamu (`sk-mod...`).
4. Pilih model: `deepseek-v4.1-flash` atau `claude-sonnet-4.6`.

### 4. OpenClaw
1. Buka pengaturan LLM OpenClaw.
2. Konfigurasikan provider OpenAI Compatible:
   - **Base URL:** `https://modelrouter.id/v1`
   - **API Key:** `sk-mod...`
   - **Model:** `deepseek-v4.1-flash`

---

## 🚀 Quickstart Python SDK

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://modelrouter.id/v1",
    api_key="sk-mod-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Ganti dengan API Key kamu
)

response = client.chat.completions.create(
    model="deepseek-v4.1-flash", # atau "claude-sonnet-4.6", "gemini-3.8-flash"
    messages=[
        {"role": "system", "content": "Kamu adalah asisten AI handal untuk developer Indonesia."},
        {"role": "user", "content": "Jelaskan arsitektur event-driven microservices secara ringkas."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

---

## 🌐 Endpoint & Spesifikasi

- **Base URL:** `https://modelrouter.id/v1`
- **Chat Endpoint:** `https://modelrouter.id/v1/chat/completions`
- **Models Catalog:** `https://modelrouter.id/v1/models`
- **Header Autentikasi:** `Authorization: Bearer sk-mod...`

---

## 📚 Tautan Resmi

- 🌐 Website: [https://modelrouter.id](https://modelrouter.id)
- 🎁 Bansos AI: [https://modelrouter.id/bansos-ai](https://modelrouter.id/bansos-ai)
- 🔀 Alternatif OpenRouter: [https://modelrouter.id/alternatif-openrouter](https://modelrouter.id/alternatif-openrouter)
- 📋 Katalog Model Lengkap: [https://modelrouter.id/models](https://modelrouter.id/models)
- 📖 Dokumentasi Lengkap: [https://modelrouter.id/docs](https://modelrouter.id/docs)
- 💻 Panduan Setup Cursor AI: [https://modelrouter.id/docs/cursor](https://modelrouter.id/docs/cursor)
- 🤖 Panduan Setup Hermes Agent: [https://modelrouter.id/docs/hermes-agent](https://modelrouter.id/docs/hermes-agent)
- 💬 Bantuan & CS: [https://modelrouter.id/support](https://modelrouter.id/support)
- 📢 Komunitas & Update: [Telegram Channel](https://t.me/modelrouter_info) | [Grup Diskusi](https://t.me/modelroutergrup)
