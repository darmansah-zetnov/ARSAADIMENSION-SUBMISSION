## PROTOTYPE ARSAA V1

This is a code bundle for PROTOTYPE ARSAA V1. The original project is available at 

https://www.figma.com/make/XmtTFvvxHsKvukvb8Lmj0R/PROTOTYPE-ARSAA-V1?fullscreen=1

**ARSAA DIMENSION** Prototype platform real estate yang menghubungkan agen, developer, investor dan pembeli. Menggunakan **AI** untuk analisis cerdas, **AR/VR** untuk visualisasi dan **Web3** untuk transaksi transparan.

Beberapa fitur lanjutan di prototype web termasuk **AR/VR untuk survei properti interaktif** dan **integrasi Web3 untuk transparansi transaksi**, masih dalam pengembangan dan akan diselesaikan pada fase berikutnya.

Running AI melalui terminal code intall backend, Prototype figma sudah terintegrasi dengan API Key Gemini dan bersifat sementara nantinya akan di update kembali.

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
