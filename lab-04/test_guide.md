# Hướng dẫn Kiểm thử & Chạy Lab 04

Tài liệu này hướng dẫn chi tiết các lệnh chạy và kết quả đầu ra mong đợi cho từng phần của Bài thực hành 4.

---

## 1. Socket kết hợp AES và RSA

Đảm bảo đã kích hoạt môi trường ảo và cài đặt `pycryptodome`.

### Các bước chạy thử:
Mở 3 terminal riêng biệt trong VS Code:

**Terminal 1 (Server):**
```powershell
cd lab-04/aes_rsa_socket
python server.py
```
*Kết quả đầu ra dự kiến:*
Server sẽ bắt đầu chạy và lắng nghe kết nối tại `localhost:12345`. Không in gì cho đến khi có client kết nối.

**Terminal 2 (Client 1):**
```powershell
cd lab-04/aes_rsa_socket
python client.py
```
*Kết quả đầu ra dự kiến:*
- Kết nối thành công tới Server.
- In ra prompt nhập tin nhắn:
  `Enter message ('exit' to quit): `

**Terminal 3 (Client 2):**
```powershell
cd lab-04/aes_rsa_socket
python client2.py
```
*Kết quả đầu ra dự kiến:*
- Kết nối thành công tới Server.
- In ra prompt nhập tin nhắn:
  `Enter message ('exit' to quit): `

### Kiểm thử truyền tin nhắn:
- Tại **Terminal 2 (Client 1)**, nhập `"Hello Client 2"` và nhấn Enter.
- Tại **Terminal 3 (Client 2)**, bạn sẽ thấy xuất hiện dòng chữ:
  `Received: Hello Client 2`
- Tại **Terminal 1 (Server)**, bạn sẽ thấy log giải mã tin nhắn:
  `Connected with ('127.0.0.1', <port_client1>)`
  `Connected with ('127.0.0.1', <port_client2>)`
  `Received from ('127.0.0.1', <port_client1>): Hello Client 2`
- Nhập `"exit"` ở bất kỳ client nào để ngắt kết nối.

---

## 2. Diffie-Hellman Key Pair

Đảm bảo đã cài đặt `cryptography`.

### Các bước chạy thử:
Chạy lần lượt server và client trong Terminal:

**Bước 1: Chạy Server để tạo và xuất khóa công khai của server:**
```powershell
cd lab-04/dh_key_pair
python server.py
```
*Kết quả đầu ra dự kiến:*
Tạo ra một file PEM chứa khóa công khai của server tên là `server_public_key.pem` trong thư mục `dh_key_pair/`. Không in gì ra màn hình console.

**Bước 2: Chạy Client để tải khóa server và thực hiện trao đổi khóa:**
```powershell
python client.py
```
*Kết quả đầu ra dự kiến:*
Client đọc khóa công khai của Server, tự tạo cặp khóa của mình, tính toán khóa bí mật dùng chung (Shared Secret) và in ra mã Hex của khóa đó:
```text
Shared Secret: <chuỗi_hex_64_ký_tự>
```

---

## 3. Các hàm băm (Hash Functions)

### Các lệnh chạy thử:

```powershell
cd lab-04/hash
```

#### a. Custom MD5 (Tự triển khai bằng thuật toán chính thức):
```powershell
python md5_hash.py
```
*Đầu vào mẫu:*
`Nhập chuỗi cần băm: HUTECH`
*Kết quả đầu ra dự kiến:*
`Mã băm MD5 của chuỗi 'HUTECH' là: b5d7ba620e746a58a9dcf111666ff051` (hoặc tương ứng tùy chuỗi nhập).

#### b. MD5 Library (Sử dụng thư viện `hashlib`):
```powershell
python md5_library.py
```
*Đầu vào mẫu:*
`Nhập chuỗi cần băm: HUTECH`
*Kết quả đầu ra dự kiến:*
`Mã băm MD5 của chuỗi 'HUTECH' là: b5d7ba620e746a58a9dcf111666ff051` (phải khớp hoàn toàn với kết quả tự code ở trên).

#### c. SHA-256 (Sử dụng thư viện `hashlib`):
```powershell
python sha256_hash.py
```
*Đầu vào mẫu:*
`Nhập chuỗi để hash bằng SHA-256: HUTECH`
*Kết quả đầu ra dự kiến:*
`Giá trị hash SHA-256: 4b29bb88ff593415cf2fa942c7e0c8de22e0a29f8c6ebf262db6624cf40df7bb`

#### d. SHA-3 (SHA3-256 sử dụng thư viện `pycryptodome`):
```powershell
python sha3_hash.py
```
*Đầu vào mẫu:*
`Nhập chuỗi văn bản: HUTECH`
*Kết quả đầu ra dự kiến:*
```text
Chuỗi văn bản đã nhập: HUTECH
SHA-3 Hash: <chuỗi_hex_64_ký_tự_SHA3>
```

#### e. BLAKE2 (BLAKE2b sử dụng thư viện `hashlib`):
```powershell
python blake2_hash.py
```
*Đầu vào mẫu:*
`Nhập chuỗi văn bản: HUTECH`
*Kết quả đầu ra dự kiến:*
```text
Chuỗi văn bản đã nhập: HUTECH
BLAKE2 Hash: <chuỗi_hex_128_ký_tự_BLAKE2b>
```

---

## 4. WebSocket với Tornado

Đảm bảo đã cài đặt `tornado`.

### Các bước chạy thử:
Mở 3 terminal riêng biệt trong VS Code:

**Terminal 1 (Server):**
```powershell
cd lab-04/websocket
python server.py
```
*Kết quả đầu ra dự kiến:*
Server WebSocket khởi tạo và lắng nghe tại cổng `8888`. Mỗi khi có client kết nối hoặc sau mỗi 3 giây phát tin, server sẽ hiển thị log:
`Sending message to 1 client(s).` hoặc `Sending message to 2 client(s).`

**Terminal 2 (Client 1):**
```powershell
cd lab-04/websocket
python client.py
```
*Kết quả đầu ra dự kiến:*
- Client kết nối tới server và in ra log `Reading...`
- Mỗi 3 giây, client nhận được một từ ngẫu nhiên từ server:
  `Received word from server: apple`
  `Received word from server: orange`

**Terminal 3 (Client 2):**
```powershell
cd lab-04/websocket
python client2.py
```
*Kết quả đầu ra dự kiến:*
Tương tự như Client 1, sẽ bắt đầu nhận các từ ngẫu nhiên đồng thời cùng Client 1:
  `Received word from server: banana`
  `Received word from server: grape`
