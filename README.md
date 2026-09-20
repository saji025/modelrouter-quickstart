# ModelRouter AI Gateway - Panduan Integrasi & Setup Cepat (Indonesia)

[![ModelRouter](https://img.shields.io/badge/Platform-ModelRouter-7c5cff.svg)](https://modelrouter.id)
[![Base URL](https://img.shields.io/badge/OpenAI--Compatible-https%3A%2F%2Fmodelrouter.id%2Fv1-22d3ee.svg)](https://modelrouter.id)
[![Payment](https://img.shields.io/badge/Deposit-QRIS%2024%2F7-4ade80.svg)](https://modelrouter.id/billing)
[![Bansos AI](https://img.shields.io/badge/Bansos%20AI-Free%20Tier-f59e0b.svg)](https://modelrouter.id/bansos-ai)

Panduan resmi integrasi developer untuk **[ModelRouter](https://modelrouter.id)** — Universal AI API Gateway di Indonesia yang kompatibel penuh dengan OpenAI SDK untuk mengakses puluhan model frontier dunia seperti Claude Opus 5, Claude Sonnet 4.6, GPT-6 Astra, DeepSeek V4.1, dan Gemini 3.8 Flash menggunakan satu saldo Rupiah.

---

## 🎁 Program Bansos AI (Free Tier 100 Request)

ModelRouter menyediakan kuota uji coba gratis (Bansos AI) bagi para developer, programmer, dan mahasiswa di Indonesia:
- **100 Request Uji Coba Gratis:** Langsung aktif begitu mendaftar tanpa syarat kartu kredit.
- **Model yang Didukung:** DeepSeek V4.1 Flash, MiMo V2.5, Qwen 3.8 Flash, dan TH Orchestra.
- **Klaim Sekarang:** Buka **[https://modelrouter.id/bansos-ai](https://modelrouter.id/bansos-ai)** untuk panduan klaim instan.

---

## ⚡ Kenapa Memilih ModelRouter?

- **Tanpa Kartu Kredit Internasional:** Akses API Claude, GPT, dan DeepSeek tanpa terhalang pembayaran debit/kredit luar negeri.
- **Top-Up Instan Otomatis via QRIS 24/7:** Pengisian saldo instan mulai dari **Rp 5.000** via GoPay, OVO, DANA, ShopeePay, BCA, Mandiri, BRI, BNI, dan seluruh bank.
- **Login 1-Tap Cepat:** Masuk langsung dengan **Google**, **GitHub**, atau email aktif di [https://modelrouter.id/login](https://modelrouter.id/login).
- **Prompt Caching Diskon hingga 95%:** Hemat biaya token secara drastis untuk coding agent (Cursor, Cline, Roo Code, Aider).
- **Satu Endpoint untuk Semua Model:** Cukup arahkan Base URL ke `https://modelrouter.id/v1`.

---

## 🚀 Quickstart (Python)

Instal SDK resmi OpenAI:

```bash
pip install openai
```

Buat file script Python (misal `main.py`):

```python
from openai import OpenAI

# 1. Daftar dan buat API Key di: https://modelrouter.id/keys
client = OpenAI(
    api_key="sk-mod...",  # Masukkan API Key ModelRouter kamu
    base_url="https://modelrouter.id/v1"
)

# 2. Panggil model pilihan kamu
response = client.chat.completions.create(
    model="deepseek-v4.1-flash",  # Pilihan: claude-sonnet-4.6, gemini-3.8-flash, mimo-v2.5, dll
    messages=[
        {"role": "system", "content": "Kamu adalah asisten programmer yang cerdas dan to the point."},
        {"role": "user", "content": "Jelaskan arsitektur API Gateway modern dalam 2 paragraf!"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

---

## 💻 Panduan Setup di Cursor & Cline

### 1. Konfigurasi di Cursor AI
1. Buka menu **Settings** di Cursor -> pilih tab **Models**.
2. Masukkan API Key dari ModelRouter pada kolom **OpenAI API Key**.
3. Aktifkan opsi **Override OpenAI Base URL** dan masukkan:
   ```text
   https://modelrouter.id/v1
   ```
4. Tambahkan model yang ingin digunakan:
   - `claude-sonnet-4.6`
   - `deepseek-v4.1-flash`
   - `gemini-3.8-flash`
   - `mimo-v2.5`

### 2. Konfigurasi di Cline / Roo Code (VS Code)
- **API Provider:** Pilih `OpenAI Compatible`
- **Base URL:** `https://modelrouter.id/v1`
- **API Key:** Masukkan token ModelRouter kamu
- **Model ID:** Masukkan ID model pilihan (misal: `deepseek-v4.1-flash`)

---

## 📚 Tautan Resmi & Bantuan

- **Website Resmi:** [https://modelrouter.id](https://modelrouter.id)
- **Program Bansos AI:** [https://modelrouter.id/bansos-ai](https://modelrouter.id/bansos-ai)
- **Katalog & Tarif Model:** [https://modelrouter.id/models](https://modelrouter.id/models)
- **Dokumentasi Lengkap:** [https://modelrouter.id/docs](https://modelrouter.id/docs)
- **Bantuan & Customer Support:** [https://modelrouter.id/support](https://modelrouter.id/support)
- **Channel Update Telegram:** [https://t.me/modelrouter_info](https://t.me/modelrouter_info)
