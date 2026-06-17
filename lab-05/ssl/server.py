import socket
import ssl
import os

def main():
    # Cấu hình địa chỉ và cổng
    host = '127.0.0.1'
    port = 8443

    # Lấy đường dẫn tuyệt đối tới file chứng chỉ và khóa riêng
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cert_path = os.path.join(current_dir, 'certificates', 'server.crt')
    key_path = os.path.join(current_dir, 'certificates', 'server.key')

    if not os.path.exists(cert_path) or not os.path.exists(key_path):
        print(f"[LỖI] Không tìm thấy file chứng chỉ hoặc khóa riêng.")
        print(f"Vui lòng chạy file certificates/generate_cert.bat trước.")
        return

    print("=== SSL SOCKET SERVER ===")
    
    # Tạo SSL Context cho Server
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    # Tạo socket TCP cơ bản
    bind_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bind_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    bind_socket.bind((host, port))
    bind_socket.listen(5)

    print(f"Server đang lắng nghe kết nối bảo mật tại {host}:{port}...")

    try:
        while True:
            # Chấp nhận kết nối TCP từ client
            client_socket, from_address = bind_socket.accept()
            print(f"\n[+] Có kết nối TCP mới từ: {from_address}")
            
            try:
                # Thiết lập bắt tay SSL/TLS (wrap socket)
                secure_socket = context.wrap_socket(client_socket, server_side=True)
                print("[*] Hoàn tất bắt tay SSL/TLS. Kênh truyền tin đã được mã hóa.")
                
                # Nhận dữ liệu từ client
                data = secure_socket.recv(1024)
                if data:
                    message = data.decode('utf-8')
                    print(f"[Client gửi]: {message}")
                    
                    # Gửi phản hồi lại cho client
                    response = f"Server đã nhận tin nhắn: '{message}' thành công."
                    secure_socket.sendall(response.encode('utf-8'))
                    
            except ssl.SSLError as e:
                print(f"[-] Lỗi bảo mật SSL/TLS trong quá trình bắt tay: {e}")
            except Exception as e:
                print(f"[-] Lỗi xử lý kết nối: {e}")
            finally:
                # Đóng kết nối
                secure_socket.close()
                print("[-] Đã đóng kết nối an toàn.")

    except KeyboardInterrupt:
        print("\nServer đang dừng hoạt động...")
    finally:
        bind_socket.close()
        print("Server đã dừng.")

if __name__ == "__main__":
    main()
