# BÀI 5: ỨNG DỤNG BẢO MẬT - THỰC HÀNH BẢO MẬT THÔNG TIN NÂNG CAO

Dự án này chứa mã nguồn của **Bài 5: Ứng dụng bảo mật** thuộc môn Thực hành Bảo mật thông tin nâng cao, được phát triển bằng ngôn ngữ Python 3.

**Sinh viên thực hiện:** Lê Viết Đức  
**Mã lớp/MSSV:** 23DTHA4 / 0533  

---

## 📁 Cấu Trúc Thư Mục Lab 05
```text
levietduc_THBMTT_23DTHA4_0533/
│
├── README.md               # File hướng dẫn chạy chương trình (đang xem)
├── requirements.txt         # File danh sách thư viện cần cài đặt
│
└── lab-05/
    ├── base64/
    │   ├── encode.py       # Mã hóa chuỗi văn bản bằng Base64
    │   └── decode.py       # Giải mã chuỗi Base64
    │
    ├── ssl/
    │   ├── server.py       # SSL Socket Server
    │   ├── client.py       # SSL Socket Client
    │   └── certificates/
    │       ├── generate_cert.bat    # Script sinh chứng chỉ SSL tự động
    │       ├── generate_cert.py     # Script Python sinh chứng chỉ dự phòng
    │       ├── server.crt           # Chứng chỉ SSL của Server
    │       └── server.key           # Khóa riêng tư SSL của Server
    │
    ├── blockchain/
    │   ├── block.py        # Định nghĩa lớp đối tượng Block
    │   ├── blockchain.py   # Định nghĩa đối tượng Blockchain chính
    │   └── test_blockchain.py # Kịch bản kiểm thử mô phỏng Blockchain
    │
    └── img-hidden/
        ├── encode_image.py # Giấu tin vào ảnh bằng LSB
        ├── decode_image.py # Đọc lại tin đã giấu từ ảnh
        └── input_image.png # Ảnh gốc làm nguyên liệu giấu tin
```

---

## 🛠️ Hướng Dẫn Cài Đặt Môi Trường

### 1. Kiểm tra Python 3
Mở Terminal/PowerShell trong VS Code và gõ lệnh sau để kiểm tra xem máy tính đã cài đặt Python 3 chưa:
```bash
python --version
```
*(Nếu chưa cài đặt, vui lòng tải Python 3 tại [python.org](https://www.python.org/downloads/) và nhớ tích chọn "Add Python to PATH" lúc cài đặt).*

### 2. Cài đặt các thư viện cần thiết
Từ thư mục gốc của dự án (`levietduc_THBMTT_23DTHA4_0533`), chạy lệnh sau để cài đặt các thư viện phụ thuộc (thư viện `Pillow` cho bài giấu tin):
```bash
pip install -r requirements.txt
```

---

## 🚀 Hướng Dẫn Chạy Và Kiểm Thử Từng Bài

### 1. Base64 (Mã hóa và giải mã Base64)
*   **Mã hóa:**
    ```bash
    python lab-05/base64/encode.py
    ```
    *Nhập chuỗi bất kỳ, hệ thống sẽ in ra kết quả đã mã hóa dưới dạng Base64.*

*   **Giải mã:**
    ```bash
    python lab-05/base64/decode.py
    ```
    *Nhập chuỗi Base64 cần giải mã (ví dụ: `SMOqbyBs6oMgbmjDqQ==`). Hệ thống có tích hợp bộ kiểm tra định dạng và sẽ báo lỗi nếu chuỗi nhập vào bị sai padding hoặc chứa ký tự không hợp lệ.*

---

### 2. SSL (Giao tiếp bảo mật Client-Server bằng SSL/TLS)

#### Bước A: Sinh chứng chỉ và khóa bảo mật
Bạn kiểm tra xem máy tính đã có OpenSSL chưa bằng lệnh:
```bash
openssl version
```
*   **Trường hợp 1 (Máy có OpenSSL):** Chạy script `generate_cert.bat` bằng cách nhấp đúp hoặc chạy trong Terminal:
    ```powershell
    cd lab-05/ssl/certificates
    ./generate_cert.bat
    cd ../../..
    ```
*   **Trường hợp 2 (Máy không có OpenSSL):** Script `.bat` ở trên sẽ tự động phát hiện và kích hoạt dự phòng qua file Python `generate_cert.py` (sử dụng thư viện `cryptography` tích hợp sẵn trên máy) để tạo cặp chứng chỉ `server.crt` và khóa `server.key` thành công.

#### Bước B: Chạy Server
Mở một cửa sổ Terminal mới trong VS Code và khởi động SSL Server:
```bash
python lab-05/ssl/server.py
```
*Server sẽ bắt đầu lắng nghe tại cổng `8443`.*

#### Bước C: Chạy Client và gửi tin nhắn
Mở một cửa sổ Terminal thứ hai trong VS Code và khởi động SSL Client:
```bash
python lab-05/ssl/client.py
```
*Nhập thông điệp cần gửi (ví dụ: `Hello Secure Server`). Tin nhắn sẽ được mã hóa trên đường truyền SSL/TLS, gửi tới Server. Server nhận diện, in ra màn hình và phản hồi bảo mật lại cho Client.*

---

### 3. Blockchain (Mô phỏng chuỗi khối & Proof of Work)
Chạy script kiểm thử để kiểm tra cấu trúc chuỗi khối, quá trình đào (mining) bằng Proof of Work và kiểm tra tính toàn vẹn của chuỗi:
```bash
python lab-05/blockchain/test_blockchain.py
```
**Kết quả mong đợi:**
*   Hệ thống đào thành công các khối và in ra thông tin chi tiết từng khối (Index, Timestamp, Proof, Hash, Transactions...).
*   Hệ thống in ra kết quả kiểm định: `Is Blockchain Valid: True`.
*   Tiếp theo, chương trình giả lập một vụ tấn công thay đổi dữ liệu trái phép ở Block 1 và tự động phát hiện lỗi giả mạo để in ra kết quả: `Is Blockchain Valid: False`.

---

### 4. Giấu tin trong ảnh (LSB Steganography)
*   **Giấu tin (Encode):**
    ```bash
    python lab-05/img-hidden/encode_image.py
    ```
    *Nhập thông điệp bí mật bạn muốn giấu. Chương trình sẽ đọc ảnh gốc `input_image.png`, chèn thông điệp vào các bit LSB của các điểm ảnh và lưu lại thành ảnh đầu ra `encoded_image.png`.*

*   **Giải mã/Trích xuất tin (Decode):**
    ```bash
    python lab-05/img-hidden/decode_image.py
    ```
    *   **Lựa chọn 1:** Giải mã từ ảnh `encoded_image.png` -> Trích xuất chính xác thông điệp ban đầu đã giấu.
    *   **Lựa chọn 2:** Giải mã thử từ ảnh gốc `input_image.png` -> Kết quả nhận được chỉ là dữ liệu rác ngẫu nhiên (nhiễu màu tự nhiên của ảnh gốc) và chương trình sẽ in giải thích lý do tại sao không lấy được thông điệp gốc.

---

## 📌 Xử lý lỗi thường gặp
1.  **Lỗi `ModuleNotFoundError`**: Do chưa chạy cài đặt các thư viện ở tệp `requirements.txt`. Vui lòng chạy lệnh `pip install -r requirements.txt` để cài đặt.
2.  **Lỗi SSL Connection Refused**: Đảm bảo rằng bạn đã khởi chạy `server.py` trước khi chạy `client.py`.
