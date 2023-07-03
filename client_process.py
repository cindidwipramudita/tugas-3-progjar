import sys
import socket
import logging
from multiprocessing import Process
import time

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("Membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"Opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Mengirim data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] Sending {message}")
        sock.sendall(message.encode())

        # Mencari respon dari server
        data = sock.recv(32)
        logging.warning(f"[RECEIVED FROM SERVER] {data}")
    finally:
        logging.warning("Closing")
        sock.close()


if __name__ == '__main__':
    process_count = 0  # Tambahkan counter
    start_time = time.time()  # Simpan waktu mulai
    while time.time() - start_time < 10:  # Hanya jalankan loop selama 10 detik
        p = Process(target=kirim_data)  # Buat proses baru
        p.start()  # Mulai proses
        p.join()  # Tunggu proses selesai
        process_count += 1  # Update counter di sini
    # Cetak jumlah proses yang telah dibuat
    logging.warning(f"Total processes created: {process_count}")
