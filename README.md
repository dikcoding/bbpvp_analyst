# Analisis Efektivitas Program Pelatihan Vokasi BBPVP Medan

Proyek ini bertujuan untuk menganalisis data kegiatan pelatihan vokasi di BBPVP Medan. Fokus utamanya adalah menilai efektivitas program, mengukur dampaknya terhadap produktivitas peserta, dan memberikan rekomendasi berbasis data untuk peningkatan kinerja di masa depan.

---

## 🎯 1. Business Understanding

### Tujuan Bisnis
Menganalisis data kegiatan pelatihan vokasi di BBPVP Medan untuk menilai efektivitas program pelatihan terhadap produktivitas peserta.

### Fokus Utama
* Mengukur tingkat kehadiran dan kelulusan peserta pelatihan.
* Menganalisis hubungan antara jenis pelatihan, durasi, dan hasil produktivitas.
* Memberikan rekomendasi berbasis data untuk peningkatan kinerja pelatihan.

### Pertanyaan Bisnis (Business Questions)
1.  Jenis pelatihan apa yang paling efektif meningkatkan produktivitas peserta?
2.  Bagaimana tren kehadiran dan kelulusan peserta selama periode tertentu?
3.  Apakah terdapat hubungan antara durasi pelatihan dan hasil evaluasi peserta?

---

## 📊 2. Data Collection

### Sumber Data
Dataset yang digunakan adalah data sintetis yang dibuat menggunakan Python (Faker Library) untuk mensimulasikan data peserta pelatihan. Strukturnya adalah sebagai berikut:

* `participant_id`: ID unik peserta
* `nama_peserta`: Nama peserta
* `jenis_pelatihan`: Contoh: Teknologi Informasi, Manufaktur, Tata Boga, Otomotif
* `durasi_pelatihan`: Lama pelatihan (jam)
* `kehadiran (%)`: Persentase kehadiran peserta
* `nilai_ujian`: Nilai hasil ujian akhir
* `status_kelulusan`: Lulus / Tidak Lulus
* `produktivitas_setelah_pelatihan`: Skor produktivitas (skala 1–100)
* `tanggal_mulai`
* `tanggal_selesai`

### Tools
* **Python**: `Faker`, `Pandas` (untuk pembuatan dan penyimpanan data)
* **Format**: Dataset disimpan sebagai `.csv` untuk analisis.

---

## 🧹 3. Data Preparation & Cleaning

### Tujuan
Membersihkan dan mempersiapkan data agar konsisten, akurat, dan siap untuk dianalisis serta divisualisasikan.

### Langkah
* Memeriksa dan menghapus data duplikat.
* Memeriksa dan menangani data kosong (*missing values*) jika ada.
* Memastikan format data konsisten (mengubah kolom tanggal ke `datetime`, numerik ke `int/float`).
* Menstandardisasi data kategorikal (misal: kapitalisasi pada `jenis_pelatihan` dan `status_kelulusan`).
* Membuat kolom baru (*Feature Engineering*) untuk analisis lebih lanjut, seperti:
    * `lama_pelatihan_hari`: (turunan dari `tanggal_selesai` - `tanggal_mulai`)
    * `efektivitas_skor`: (misal: `produktivitas_setelah_pelatihan` / `durasi_pelatihan`)

### Tools
* `Pandas`
* `NumPy`
* `Datetime`

---

## 📈 4. Exploratory Data Analysis (EDA)

### Tujuan
Menemukan pola, tren, anomali, dan *insight* awal dari data pelatihan untuk menjawab pertanyaan bisnis.

### Analisis yang Dilakukan
* **Analisis Univariat**: Distribusi peserta berdasarkan `jenis_pelatihan` dan `status_kelulusan`.
* **Analisis Bivariat**:
    * Hubungan antara `kehadiran` dan `status_kelulusan`.
    * Korelasi antara `durasi_pelatihan` dan `produktivitas`.
    * Perbandingan `rata-rata nilai_ujian` per `jenis_pelatihan`.
* **Analisis Multivariat**: Melihat korelasi antar semua variabel numerik (Heatmap).
* **Outlier Detection**: Mengidentifikasi peserta dengan nilai ekstrem (misal: kehadiran sangat rendah namun produktivitas tinggi).

### Tools
* `Matplotlib`
* `Seaborn`
* `Pandas Profiling` (Opsional untuk gambaran cepat)

---

## 🤖 5. Data Modeling / Analysis

### Tujuan
Menganalisis secara statistik faktor-faktor utama yang memengaruhi keberhasilan dan produktivitas peserta.

### Langkah
* **Analisis Korelasi**: Mengukur kekuatan hubungan antar variabel.
* **Regresi Linear**: Membuat model sederhana untuk memprediksi produktivitas, contoh:
    `produktivitas ~ durasi_pelatihan + kehadiran + nilai_ujian`
* **Segmentasi Peserta**: Mengelompokkan peserta berdasarkan performa (misal: Produktivitas Tinggi, Sedang, Rendah) untuk menemukan karakteristik bersama.

### Tools
* `Scikit-learn`
* `Statsmodels`
* `Pandas`

---

## 🖥️ 6. Visualization & Reporting

### Tujuan
Menyajikan hasil analisis dan temuan kunci dalam bentuk *dashboard* yang mudah dipahami dan interaktif.

### Langkah
1.  Ekspor dataset yang sudah bersih dan dianalisis (`data_clean.csv`) ke Tableau.
2.  Buat *dashboard* yang menjawab pertanyaan bisnis, berisi:
    * KPI utama: Total Peserta, Tingkat Kelulusan (%), Rata-rata Produktivitas.
    * Tren kehadiran dan kelulusan dari waktu ke waktu.
    * Distribusi jenis pelatihan dan efektivitasnya (produktivitas rata-rata).
    * Visualisasi hubungan antara durasi pelatihan, kehadiran, dan produktivitas.
    * Rekomendasi strategis untuk perbaikan program pelatihan.

### Tools
* **Tableau**: (Untuk *dashboard* interaktif utama)
* **Python**: `Matplotlib`, `Seaborn` (Untuk visualisasi pendukung selama proses analisis)
