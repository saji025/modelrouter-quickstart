# ModelRouter AI Gateway - Panduan Integrasi & Setup Cepat (Indonesia)

[![ModelRouter](https://img.shields.io/badge/Platform-ModelRouter-7c5cff.svg)](https://modelrouter.web.id)
[![Base URL](https://img.shields.io/badge/OpenAI--Compatible-https%3A%2F%2Fmodelrouter.web.id%2Fv1-22d3ee.svg)](https://modelrouter.web.id)
[![Payment](https://img.shields.io/badge/Deposit-QRIS%2024%2F7-4ade80.svg)](https://modelrouter.web.id/wallet)

Panduan resmi integrasi dan konfigurasi developer untuk **[ModelRouter](https://modelrouter.web.id)** — AI API Gateway Indonesia yang kompatibel penuh dengan format OpenAI SDK untuk mengakses 90+ model AI flagship (DeepSeek V4, Claude Sonnet 4.6 / Fable 5.1, Gemini 3.8 Flash, GPT-5, Qwen, GLM-5).

---

## ⚡ Kenapa Pakai ModelRouter?

- **Tanpa Kartu Kredit:** Solusi buat developer, builder, dan mahasiswa di Indonesia yang ingin akses API Claude, GPT, dan DeepSeek tanpa ribet kartu kredit luar negeri.
- **Top-Up Otomatis via QRIS 24/7:** Deposit saldo instan mulai dari **$1 (Rp 17.800)** via GoPay, OVO, DANA, ShopeePay, BCA, Mandiri, BRI, dan seluruh bank.
- **Login Instan 1-Tap:** Masuk langsung menggunakan **Akun Google**, **GitHub**, atau **Telegram** di [https://modelrouter.web.id/login](https://modelrouter.web.id/login).
- **Prompt Caching Resmi Aktif:** Hemat biaya token hingga **80% - 90%** untuk coding agent (Cursor, Cline, Roo Code, dll).
- **Satu Endpoint untuk Semua Model:** Cukup arahkan Base URL ke `https://modelrouter.web.id/v1`.
- **Tersedia Free Tier:** Akses model gratis untuk prototyping dan riset (`hy3-free`, `glm-5.3-free`, `deepseek-v4-flash-free`).

---

## 🚀 Quickstart (Python)

Instal library resmi OpenAI:

```bash
pip install openai
```

Buat file script Python (misal `main.py`):

```python
from openai import OpenAI

# 1. Daftar dan ambil API Key kamu di: https://modelrouter.web.id/token
client = OpenAI(
    api_key="API_KEY_MODELROUTER_KAMU",
    base_url="https://modelrouter.web.id/v1"
)

# 2. Panggil model pilihan kamu
response = client.chat.completions.create(
    model="deepseek-v4-flash", # Pilihan lain: claude-sonnet-4.6, gemini-3.8-flash, hy3-free
    messages=[
        {"role": "system", "content": "Kamu adalah asisten programmer yang cerdas dan to the point."},
        {"role": "user", "content": "Jelaskan cara kerja Prompt Caching dalam menghemat token!"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

---

## 💻 Panduan Setup Cursor / Cline / Roo Code

Buat kamu yang pakai AI coding assistant di VS Code atau Cursor:

### 1. Konfigurasi di Cursor
1. Buka menu **Settings (Pengaturan)** di Cursor -> pilih menu **Models**.
2. Di bagian **OpenAI API Key**, masukkan API Key dari ModelRouter.
3. Klik opsi **Override OpenAI Base URL** lalu isi:
   ```text
   https://modelrouter.web.id/v1
   ```
4. Tambahkan nama model yang ingin kamu pakai:
   - `claude-sonnet-4.6`
   - `claude-fable-5.1`
   - `deepseek-v4-flash`
   - `gemini-3.8-flash`
   - `gpt-5.4-mini`

### 2. Konfigurasi di Cline / Roo Code
- **API Provider:** Pilih `OpenAI Compatible`
- **Base URL:** `https://modelrouter.web.id/v1`
- **API Key:** Masukkan token ModelRouter kamu
- **Model ID:** Masukkan model pilihan kamu (misal: `deepseek-v4-flash`)

---

## 📚 Tautan Resmi & Bantuan

- **Website Dashboard:** [https://modelrouter.web.id](https://modelrouter.web.id)
- **Dokumentasi API:** [https://modelrouter.web.id/docs](https://modelrouter.web.id/docs)
- **Daftar Tarif Model:** [https://modelrouter.web.id/pricing](https://modelrouter.web.id/pricing)
- **Top-Up Saldo (QRIS):** [https://modelrouter.web.id/wallet](https://modelrouter.web.id/wallet)
- **Channel Update Telegram:** [https://t.me/modelrouter_info](https://t.me/modelrouter_info)
