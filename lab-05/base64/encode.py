import base64

def main():
    print("=== BASE64 ENCODE ===")
    try:
        user_input = input("Nhập chuỗi văn bản cần mã hóa: ")
        
        # Chuyển chuỗi thành bytes
        input_bytes = user_input.encode('utf-8')
        
        # Mã hóa Base64
        encoded_bytes = base64.b64encode(input_bytes)
        
        # Chuyển bytes kết quả thành chuỗi để hiển thị
        encoded_str = encoded_bytes.decode('utf-8')
        
        print("\n--- Kết quả mã hóa ---")
        print(f"Chuỗi ban đầu: {user_input}")
        print(f"Chuỗi Base64: {encoded_str}")
        print("----------------------")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
