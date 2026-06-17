# Lab 04 - Socket, WebSocket, Key Exchange & Hash Functions

## Thông tin sinh viên
- **Họ tên:** Lê Việt Đức
- **Lớp:** 23DTHA4
- **MSSV:** 0533
- **Môn học:** Thực hành Bảo mật thông tin nâng cao

## Cấu trúc thư mục
```text
lab-04/
├── requirements.txt (tổng hợp các thư viện)
├── aes_rsa_socket/
│   ├── server.py
│   ├── client.py
│   ├── client2.py
│   └── requirements.txt
│
├── dh_key_pair/
│   ├── server.py
│   ├── client.py
│   ├── server_public_key.pem (được sinh ra sau khi chạy server)
│   └── requirements.txt
│
├── hash/
│   ├── md5_hash.py
│   ├── md5_library.py
│   ├── sha256_hash.py
│   ├── sha3_hash.py
│   └── blake2_hash.py
│
└── websocket/
    ├── server.py
    ├── client.py
    ├── client2.py
    └── requirements.txt
```

## Cài đặt thư viện
Bạn có thể cài đặt tất cả các thư viện từ thư mục gốc của `lab-04`:
```powershell
pip install -r requirements.txt
```
Hoặc cài đặt riêng lẻ theo từng bài thực hành. Các thư viện chính gồm:
- `pycryptodome` (cho AES, RSA, SHA-3)
- `cryptography` (cho Diffie-Hellman)
- `tornado` (cho WebSocket)

## Hướng dẫn chạy các bài thực hành

Xem chi tiết hướng dẫn chạy, các lệnh test và kết quả đầu ra dự kiến trong file [test_guide.md](test_guide.md).
