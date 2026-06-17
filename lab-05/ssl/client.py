import socket
import ssl
import sys

def main():
    host = '127.0.0.1'
    port = 8443

    print("=== SSL SOCKET CLIENT ===")
    
    # Tạo SSL Context cho Client
    # Sử dụng Purpose.SERVER_AUTH để xác thực server
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # Bỏ qua xác thực chứng chỉ vì chúng ta dùng chứng chỉ tự ký (Self-signed) cho mục đích thực hành
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Tạo socket TCP kết nối đến server
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bọc socket TCP thường thành socket bảo mật SSL/TLS
        secure_socket = context.wrap_socket(raw_socket, server_hostname=host)
        
        print(f"Đang kết nối bảo mật tới server tại {host}:{port}...")
        secure_socket.connect((host, port))
        print("[+] Kết nối và bắt tay SSL/TLS thành công!")
        
        # Nhập tin nhắn gửi lên server
        message = input("Nhập tin nhắn để gửi đến Server: ")
        if not message:
            message = "Tin nhắn mặc định từ client"
            
        # Gửi dữ liệu đã được mã hóa
        secure_socket.sendall(message.encode('utf-8'))
        print("[*] Tin nhắn đã được mã hóa và gửi đi.")
        
        # Nhận phản hồi bảo mật từ server
        response = secure_socket.recv(1024)
        print(f"\n[Server phản hồi]: {response.decode('utf-8')}")
        
        # Đóng kết nối
        secure_socket.close()
        print("\n[-] Kết nối an toàn đã được đóng.")

    except ConnectionRefusedError:
        print("\n[LỖI] Không thể kết nối tới Server. Hãy đảm bảo Server đang chạy trước.")
    except Exception as e:
        print(f"\n[LỖI] Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
