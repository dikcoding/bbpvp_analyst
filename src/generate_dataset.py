import pandas as pd
from faker import Faker
import random
from datetime import timedelta
from pathlib import Path

fake = Faker('id_ID')

list_pelatihan = ['Teknologi Informasi', 'Manufaktur', 'Tataboga', 'Kesehatan', 'Pariwisata', 'Pertanian', 'Konstruksi', 'Desain Grafis']

JUMLAH_DATA = 1000

data = []

print("Membuat {JUMLAH_DATA} data sintesis...")
for i in range(1, JUMLAH_DATA + 1):
    participant_id = f'PART-{i:05d}'
    nama_peserta = fake.name()
    jenis_pelatihan = random.choice(list_pelatihan)
    durasi_pelatihan = random.choice([40, 80, 120, 160, 200, 240])
    kehadiran = random.randint(70, 100)
    nilai_ujian = random.randint(45, 100)

    # Logic kelulusan
    if kehadiran >= 80 and nilai_ujian >= 70:
        status_kelulusan = 'Lulus'
    else:
        status_kelulusan = 'Tidak Lulus'

    # Logic produktivitas
    if status_kelulusan == 'Lulus':
        produktivitas = random.randint(75, 100)
    else:
        produktivitas = random.randint(50, 74)

    # Tanggal mulai dan selesai pelatihan
    tanggal_mulai = fake.date_between(start_date='-2y', end_date='-1m')

    # Tanggal selesai pelatihan
    durasi_hari = durasi_pelatihan / 8
    tanggal_selesai = tanggal_mulai + timedelta(days=int(durasi_hari))

    data.append({
        'participant_id': participant_id,
        'nama_peserta': nama_peserta,
        'jenis_pelatihan': jenis_pelatihan,
        'durasi_pelatihan': durasi_pelatihan,
        'kehadiran (%)': kehadiran,
        'nilai_ujian': nilai_ujian,
        'status_kelulusan': status_kelulusan,
        'produktivitas_setelah_pelatihan': produktivitas,
        'tanggal_mulai': tanggal_mulai,
        'tanggal_selesai': tanggal_selesai
    })

df = pd.DataFrame(data)
name_file = 'dataset_pelatihan_sintesis.csv'
Path('data/raw').mkdir(parents=True, exist_ok=True)

# Simpan dataset ke file CSV
df.to_csv(f'data/raw/{name_file}', index=False, encoding='utf-8')

print(f'Dataset sintesis berhasil dibuat dan disimpan di data/raw/{name_file}')