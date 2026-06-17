# Lab 03 - RSA & ECC Security Application

## Thông tin
- **Họ tên:** Lê Việt Đức
- **Lớp:** 23DTHA4
- **MSSV:** 0533
- **Môn học:** Thực hành Bảo mật thông tin nâng cao

## Công nghệ sử dụng
- Python
- PyQt5
- PyCryptodome
- Flask (cho API Server)
- Visual Studio Code

## Chức năng
### RSA
- Tạo khóa RSA 2048-bit.
- Mã hóa plaintext bằng public key (PKCS1_OAEP).
- Giải mã ciphertext bằng private key (PKCS1_OAEP).

### ECC
- Tạo khóa ECC P-256 (curve P-256 / secp256r1).
- Ký message bằng private key (DSS/ECDSA + SHA256).
- Xác minh chữ ký bằng public key.
- Nếu message bị thay đổi sau khi ký, chương trình báo chữ ký không hợp lệ.

---

## Cách chạy trên Visual Studio Code
1. Mở VS Code.
2. Chọn **File -> Open Folder**.
3. Chọn thư mục **lab03**.
4. Mở **Terminal** trong VS Code.
5. Tạo môi trường ảo:
   ```powershell
   python -m venv .venv
   ```
6. Kích hoạt môi trường ảo trên Windows PowerShell:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
7. Nếu bị lỗi quyền PowerShell (Execution Policy), chạy lệnh:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
   Sau đó chạy lại lệnh kích hoạt:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
8. Cài đặt các thư viện phụ thuộc:
   ```powershell
   pip install -r requirements.txt
   ```
9. Chạy chương trình giao diện GUI:
   ```powershell
   python main.py
   ```

---

## Cách test RSA trên Giao diện GUI
1. Chạy chương trình bằng lệnh `python main.py`.
2. Chọn **RSA Encryption / Decryption**.
3. Bấm nút **Generate RSA Key** để sinh cặp khóa công khai và bí mật 2048-bit.
4. Nhập chuỗi văn bản cần mã hóa vào ô **Plaintext (Bản rõ)**.
5. Bấm nút **Encrypt (Mã hóa)**. Kết quả bản mã Base64 sẽ hiển thị ở ô **Ciphertext (Base64)**.
6. Bấm nút **Decrypt (Giải mã)** để giải mã bản mã trở lại văn bản ban đầu, kết quả hiển thị ở ô **Decrypted Text**.

## Cách test ECC trên Giao diện GUI
1. Chạy chương trình bằng lệnh `python main.py`.
2. Chọn **ECC Digital Signature**.
3. Bấm nút **Generate ECC Key** để sinh cặp khóa ECC P-256.
4. Nhập thông điệp cần ký vào ô **Message (Thông điệp)**.
5. Bấm nút **Sign Message (Ký chữ ký)**. Chữ ký số dạng Base64 sẽ xuất hiện tại ô **Signature (Base64)**.
6. Bấm nút **Verify Signature (Xác minh)**. Trạng thái xác minh sẽ chuyển sang **Chữ ký HỢP LỆ** màu xanh.
7. Thử thay đổi nội dung ô **Message** sau khi đã ký, rồi bấm nút **Verify Signature**. Trạng thái sẽ chuyển thành **Chữ ký KHÔNG HỢP LỆ** màu đỏ.

---

## Test bằng Postman

### Chạy API server
Để test các chức năng mã hóa và ký bằng Postman, hãy chạy máy chủ API:
```powershell
python api_server.py
```
Server chạy tại địa chỉ: `http://127.0.0.1:5000`

### Danh sách các API Endpoint để test trên Postman

#### 1. Kiểm tra trạng thái Server
- **Method:** `GET`
- **URL:** `http://127.0.0.1:5000/`
- **Response mẫu (200 OK):**
  ```json
  {
    "message": "Lab03 RSA ECC API is running"
  }
  ```

#### 2. Sinh khóa RSA
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/rsa/generate-key`
- **Response mẫu (200 OK):**
  ```json
  {
    "message": "RSA key generated successfully",
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\n...",
    "public_key": "-----BEGIN PUBLIC KEY-----\n..."
  }
  ```

#### 3. Mã hóa RSA
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/rsa/encrypt`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "plaintext": "Hello RSA"
  }
  ```
- **Response mẫu (200 OK):**
  ```json
  {
    "plaintext": "Hello RSA",
    "ciphertext": "T3BlbnNzaA..."
  }
  ```

#### 4. Giải mã RSA
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/rsa/decrypt`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "ciphertext": "T3BlbnNzaA..."
  }
  ```
- **Response mẫu (200 OK):**
  ```json
  {
    "decrypted_text": "Hello RSA"
  }
  ```

#### 5. Sinh khóa ECC
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/ecc/generate-key`
- **Response mẫu (200 OK):**
  ```json
  {
    "message": "ECC key generated successfully",
    "private_key": "-----BEGIN EC PRIVATE KEY-----\n...",
    "public_key": "-----BEGIN PUBLIC KEY-----\n..."
  }
  ```

#### 6. Ký số ECC (ECDSA)
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/ecc/sign`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "message": "Hello ECC"
  }
  ```
- **Response mẫu (200 OK):**
  ```json
  {
    "message": "Hello ECC",
    "signature": "MEQCIF..."
  }
  ```

#### 7. Xác minh chữ ký số ECC
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/ecc/verify`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "message": "Hello ECC",
    "signature": "MEQCIF..."
  }
  ```
- **Response mẫu khi chữ ký hợp lệ (200 OK):**
  ```json
  {
    "valid": true,
    "message": "Signature is valid"
  }
  ```
- **Response mẫu khi chữ ký sai/bản tin bị thay đổi (200 OK):**
  ```json
  {
    "valid": false,
    "message": "Signature is invalid"
  }
  ```

#### Xử lý lỗi (Mẫu):
Nếu gọi mã hóa/ký/giải mã/xác minh trước khi sinh khóa, server sẽ trả về lỗi:
- **Status code:** `400 Bad Request`
- **Response:**
  ```json
  {
    "error": "Khóa công khai RSA chưa được tạo. Vui lòng gọi /rsa/generate-key trước."
  }
  ```
Nếu gửi thiếu trường thông tin bắt buộc:
- **Status code:** `400 Bad Request`
- **Response:**
  ```json
  {
    "error": "Thiếu tham số bắt buộc 'plaintext' trong JSON body."
  }
  ```
