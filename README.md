# WhatsApp Spammer

Alat sederhana untuk mengirim pesan spam di WhatsApp menggunakan Python dan `pyautogui`. Alat ini memungkinkan Anda untuk mengotomatiskan pengiriman pesan berulang dengan opsi yang dapat disesuaikan.

## Fitur

- Teks yang dapat dikustomisasi untuk spam
- Atur jumlah pengulangan pesan
- Konfigurasi interval antar pesan
- Opsional menyalin teks yang dihasilkan ke clipboard
- Pilih format teks (Uppercase, Lowercase, Title Case, atau None)
- GUI transparan dan modern dengan pengaturan yang dapat disesuaikan

## Persyaratan

- Python 3.x
- Pustaka `pyautogui`
- Pustaka `pyperclip`

Anda dapat menginstal pustaka yang dibutuhkan menggunakan pip:

```bash
pip install pyautogui pyperclip
```
## Penggunaan
Jalankan Skrip

Eksekusi skrip Python untuk membuka GUI:

```bash
py spam.py
```
## Konfigurasi Pengaturan

- Teks: Masukkan teks yang ingin Anda spam.
- Jumlah Pengulangan: Atur jumlah kali pesan akan dikirim.
- Interval (detik): Tentukan interval antara setiap pesan (dalam detik).
- Delay Between Messages (detik): Tentukan delay antara pengiriman setiap pesan (dalam detik).
- Panjang Teks Acak (0 untuk none): Atur panjang teks acak yang akan disertakan (masukkan 0 untuk tanpa teks acak).
- Format Teks: Pilih format teks (Uppercase, Lowercase, Title Case, atau None).
- Copy to Clipboard: Centang opsi ini jika Anda ingin menyalin teks yang dihasilkan ke clipboard.
- Kirim Pesan

### Klik tombol Kirim untuk mulai mengirim pesan di WhatsApp. Pastikan Anda telah membuka WhatsApp Web dan memilih kontak yang benar sebelum memulai.

### Penampilan GUI
Latar Belakang: Gelap dengan transparansi 70%
Teks dan Kontrol: Putih untuk kontras yang baik dengan latar belakang gelap

Modified / Forked from @madelang/python-project/spamProject
Update Version : Added GUI + More Feature
