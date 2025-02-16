# TG-Automate-Whatsaap

# TG-Automate-Whatsaap 📩🤖

Bot ini adalah bot Telegram yang memungkinkan Anda mengirim pesan WhatsApp secara otomatis ke banyak kontak menggunakan file CSV! 🎯🚀

## 📌 Fitur Utama
- 📂 Menggunakan file CSV untuk mengirim pesan secara massal.
- 🔗 Terintegrasi dengan WhatsApp melalui `pywhatkit`.
- 🤖 Respon otomatis di Telegram dengan status pengiriman.
- 📝 Log aktivitas tersimpan untuk monitoring.

## 📜 Persyaratan
Sebelum menjalankan bot ini, pastikan Anda memiliki:
- Python 3.x
- Pandas (`pip install pandas`)
- PyWhatKit (`pip install pywhatkit`)
- Python Telegram Bot (`pip install python-telegram-bot`)

## 🚀 Cara Menggunakan
1. **Jalankan bot** dengan perintah:
   ```bash
   python main.py
   ```
2. **Mulai bot** di Telegram dengan perintah `/start`.
3. **Unggah file CSV** dengan format:
   ```csv
   name,phone_number,message
   abi,111111,"✨🔥 PROMO DISKON SPESIAL! 🔥✨\n\nHalo, {Nama}! Kami punya penawaran menarik untuk Anda..."
   ika,22222,"🎁✨ PROMO BELI 1 GRATIS 1! ✨🎁\n\nHai, {Nama}! Segera manfaatkan promo eksklusif kami..."
   ```
4. Bot akan otomatis mengirim pesan WhatsApp ke nomor yang terdaftar. 🎉

## ⚠️ Catatan Penting
- Bot ini hanya dapat mengirim pesan ke nomor dengan kode negara `+62` (Indonesia).
- WhatsApp Web harus dalam keadaan login di perangkat Anda.
- Ada jeda waktu (`sleep`) agar tidak terkena pembatasan dari WhatsApp.

## 📌 Logging
Semua aktivitas bot akan dicatat dalam `log/bot.log`, termasuk pesan yang berhasil dan gagal terkirim.

## 🛠 Pengembangan
Untuk pengembang yang ingin menyesuaikan bot, Anda dapat mengedit `main.py` sesuai kebutuhan.

## 📧 Dukungan
Jika ada masalah atau pertanyaan, jangan ragu untuk menghubungi saya. Selamat mencoba! 🚀

## 📜 Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Silakan lihat file `LICENSE` untuk detail lebih lanjut.

