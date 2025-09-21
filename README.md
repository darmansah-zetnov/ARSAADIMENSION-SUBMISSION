## PROTOTYPE ARSAA V1

This is a code bundle for PROTOTYPE ARSAA V1. The original project is available at 

https://www.figma.com/make/XmtTFvvxHsKvukvb8Lmj0R/PROTOTYPE-ARSAA-V1?fullscreen=1

**ARSAA DIMENSION** Prototype platform real estate yang menghubungkan agen, developer, investor dan pembeli. Menggunakan **AI** untuk analisis cerdas, **AR/VR** untuk visualisasi dan **Web3** untuk transaksi transparan.

Beberapa fitur lanjutan di prototype web termasuk **AR/VR untuk survei properti interaktif** dan **integrasi Web3 untuk transparansi transaksi**, masih dalam pengembangan dan akan diselesaikan pada fase berikutnya.

Running AI melalui terminal code untuk intall backend, Prototype figma sudah terintegrasi dengan API Key Gemini dan bersifat sementara nantinya akan di update kembali.

---

# ARSAA DIMENSION - Backend Overview

Backend **ARSAA DIMENSION** dibangun menggunakan **FastAPI** dan berfungsi sebagai inti dari ekosistem AI & properti yang menggabungkan analisis gambar, geolokasi, dan generative AI. Backend ini menyediakan endpoint untuk query AI, feedback, analisis gambar dan geolokasi properti.

## **Fitur Utama**

### 1. AI Text Generation
• **BytePlus AI**  
  Model utama untuk menjawab pertanyaan terkait properti atau memberikan rekomendasi.  
• **Gemini AI (Google Generative AI)**  
  Digunakan sebagai fallback ketika BytePlus tidak tersedia atau gagal.  
• **Stable Diffusion** (opsional)  
  Digunakan untuk generate gambar atau visual aset properti berbasis AI.

### 2. Analisis & Referensi Gambar Properti
• **OpenCV + NumPy**  
  Digunakan untuk membaca dan menganalisis gambar properti, termasuk dimensi dan channel warna.
• **Unsplash API**  
  Bisa digunakan untuk mengambil referensi gambar properti dari sumber online.

### 3. Geolokasi Properti
• **OpenStreetMap (OSM)**  
  Mengubah alamat properti menjadi koordinat latitude dan longitude untuk integrasi peta atau lokasi.

### 4. Data & Analisis Pasar
• **NewsAPI**  
  Menyediakan konteks berita atau informasi pasar properti yang relevan untuk analisis tambahan.

### 5. Monitoring & Feedback
• Endpoint **health** Memeriksa status sistem dan ketersediaan AI.  
• Endpoint **analytics** Menyediakan statistik interaksi AI.  
• Endpoint **feedback** Menyimpan rating dan komentar pengguna terhadap hasil AI.

Semua dependensi di requirements.txt diinstall agar running (FastAPI, httpx, OpenCV, NumPy, python dotenv, uvicorn).

---

## Backend Setup (Python + FastAPI)

1. Masuk ke folder backend:

cd backend

2. Install dependencies:

pip install -r requirements.txt

3. Setup environment:

cp .env.example .env

Edit .env → masukkan API key dan konfigurasi lain

4. Jalankan backend:

uvicorn main:app --reload --port 8000

Backend berjalan di http://127.0.0.1:8000

Test endpoint:

curl http://127.0.0.1:8000/api/health

---

## Frontend Setup (Node + Vite)

1. Kembali ke folder utama:

cd ..

2. Install dependency frontend:

npm install

3. Jalankan development server:

npm run dev

Buka browser biasanya port 5173

Pastikan frontend bisa request ke backend (http://127.0.0.1:8000)

---

## Menjalankan Project di Semua Device

1. PC / Laptop / VS Code / Editor Lain

Buka project di editor terminal editor bisa pakai semua perintah backend dan frontend di atas.

Backend jalan di http://127.0.0.1:8000

Frontend jalan di http://localhost:5173

2. HP (Termux)

Masuk folder project, buat venv (opsional) :

python -m venv venv
source venv/bin/activate

Install dependencies backend + frontend, jalankan sama seperti di PC

Buka browser HP untuk frontend

## **Catatan Pengembangan:**
Project ini dikembangkan menggunakan **HP dengan Termux, Figma & Firefox mode dekstop** sebagai lingkungan pengembangan utama. Seluruh backend (FastAPI) dan frontend (Vite/Node) dibangun dan diuji di perangkat mobile.
