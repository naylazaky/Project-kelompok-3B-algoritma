# This is my simple project
# Motipy

Motipy adalah paket Python yang digunakan untuk menyesuaikan kecerahan gambar. Paket ini memudahkan pengguna dalam mengubah kecerahan gambar sesuai kebutuhan.

## Fitur

- Menyesuaikan kecerahan gambar
- Mendukung berbagai format gambar

## Instalasi

Untuk menginstal Motipy, jalankan perintah berikut:

```bash
pip install .

#cara penggunaan
from motipy import adjust_brightness
from PIL import Image

# Memuat gambar
image = Image.open('path/to/image.jpg')

# Menyesuaikan kecerahan
bright_image = adjust_brightness(image, factor=1.5)

# Menyimpan gambar hasil
bright_image.save('path/to/bright_image.jpg')


