# PROTOTYPE ARSAA DIMENSION V1

**ARSAA DIMENSION** adalah prototipe platform real estate yang menghubungkan **agen, pengembang, investor, dan pembeli**. Platform ini memanfaatkan:
• **AI** untuk analisis cerdas dan rekomendasi properti,
• **AR/VR** untuk visualisasi properti interaktif,  
• **Web3** untuk transparansi transaksi.  

Prototipe ini masih dalam pengembangan; beberapa fitur lanjutan seperti AR/VR dan integrasi Web3 akan diselesaikan di fase berikutnya.

[🔗 Prototype Figma ARSAA V1](https://www.figma.com/make/XmtTFvvxHsKvukvb8Lmj0R/PROTOTYPE-ARSAA-V1?fullscreen=1)

---

## Backend Overview

Backend **ARSAA DIMENSION** dibangun menggunakan **FastAPI** dan berfungsi sebagai inti dari ekosistem AI & properti. Backend menyediakan endpoint untuk:
• **Query AI** (analisis dan rekomendasi properti),
• **Feedback pengguna**,
• **Analisis gambar properti**,
• **Geolokasi properti**.  

### Fitur Utama

#### 1. AI Text Generation
• **BytePlus AI** model utama untuk menjawab pertanyaan properti.  
• **Gemini AI (Google Generative AI)** fallback jika BytePlus gagal.  
• **Stable Diffusion (opsional)** generate visual aset properti berbasis AI.  

#### 2. Analisis & Referensi Gambar Properti
• **OpenCV + NumPy** membaca dan menganalisis gambar (dimensi, channel warna).  
- **Unsplash API** mengambil referensi gambar properti online (opsional).  

#### 3. Geolokasi Properti
• **OpenStreetMap (OSM)** mengubah alamat properti menjadi koordinat latitude & longitude.  

#### 4. Data & Analisis Pasar
• **NewsAPI** memberikan konteks berita atau informasi pasar properti untuk analisis tambahan.  

#### 5. Pemantauan & Feedback
- **Health endpoint** `/api/arsaa/health` memeriksa status backend dan AI.  
- **Analytics endpoint** `/api/arsaa/analytics` menampilkan statistik interaksi AI.  
- **Feedback endpoint** `/api/arsaa/feedback` menyimpan rating dan komentar pengguna.  

---

## Cara Menjalankan Backend (PC / Laptop / Mac)

### 1. Persiapan
• Pastikan **Python 3.10+** sudah terinstal.
• Clone repository ARSAA DIMENSION.
• Masuk ke folder backend:

cd ARSAADIMENSION-SUBMISSION/backend

2. Buat Virtual Environment (opsional)

python -m venv venv

Aktifkan venv:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3. Instal Dependensi

pip install -r requirements.txt

Pastikan semua API key (BytePlus, Gemini, Stable Diffusion, Unsplash, NewsAPI) valid.

5. Jalankan Backend

uvicorn main:app --reload --host 0.0.0.0 --port 8000

Backend akan berjalan di http://127.0.0.1:8000

Endpoint test:

Health check: http://127.0.0.1:8000/api/arsaa/health

Analytics: http://127.0.0.1:8000/api/arsaa/analytics

Cara Menjalankan Frontend (Node + Vite)

1. Masuk Folder Frontend (Figma)

cd ARSAA-DIMENSION

2. Instal Dependensi Frontend

npm install

3. Jalankan Development Server

npm run dev

Biasanya frontend berjalan di http://localhost:5173

Pastikan frontend bisa melakukan request ke backend http://127.0.0.1:8000

## Catatan

Prototipe ini dikembangkan dan diuji di HP dengan Termux, Figma & Firefox mode desktop.

Backend sudah mendukung AI, analisis gambar dan geolokasi, tapi fitur prototype figma AR/VR dan Web3 masih dalam pengembangan.

Disarankan menjalankan backend sebelum frontend agar request API berjalan tanpa error.

---

Summary

Backend ARSAA DIMENSION adalah AI untuk platform real estate nantinya.

Menangani query AI, feedback, analisis gambar, geolokasi.

Siap dijalankan di PC, Laptop, atau Mac dengan Python & FastAPI.

Frontend Vite/Node akan terhubung langsung ke backend untuk demo interaktif.
