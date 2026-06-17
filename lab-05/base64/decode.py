import base64
import binascii

def validate_base64(s):
    """Kiểm tra sơ bộ tính hợp lệ của chuỗi Base64"""
    # Loại bỏ các ký tự khoảng trắng nếu có
    s = s.strip()
    
    # Độ dài chuỗi Base64 phải chia hết cho 4 (kể cả phần bù = nếu có)
    if len(s) % 4 != 0:
        return False, "Độ dài chuỗi Base64 không hợp lệ (phải chia hết cho 4)."
        
    # Tập ký tự hợp lệ trong Base64
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    if not all(char in valid_chars for char in s):
        return False, "Chuỗi chứa ký tự không hợp lệ trong bảng mã Base64."
        
    return True, ""

def main():
    print("=== BASE64 DECODE ===")
    try:
        user_input = input("Nhập chuỗi Base64 cần giải mã: ").strip()
        
        # Kiểm tra tính hợp lệ trước khi giải mã
        is_valid, err_msg = validate_base64(user_input)
        if not is_valid:
            print(f"\n[Lỗi Định Dạng] {err_msg}")
            return
            
        # Giải mã Base64
        # Chuyển chuỗi đầu vào thành bytes
        encoded_bytes = user_input.encode('utf-8')
        
        # Giải mã
        decoded_bytes = base64.b64decode(encoded_bytes)
        
        # Chuyển bytes kết quả thành chuỗi utf-8
        decoded_str = decoded_bytes.decode('utf-8')
        
        print("\n--- Kết quả giải mã ---")
        print(f"Chuỗi Base64: {user_input}")
        print(f"Chuỗi ban đầu: {decoded_str}")
        print("----------------------")
        
    except (binascii.Error, ValueError) as e:
        print(f"\n[Lỗi Giải Mã] Chuỗi Base64 không hợp lệ hoặc sai định dạng padding: {e}")
    except UnicodeDecodeError:
        print("\n[Lỗi Giải Mã] Chuỗi giải mã thành công dạng bytes nhưng không thể hiển thị dưới dạng văn bản UTF-8 (có thể đây là dữ liệu nhị phân).")
    except Exception as e:
        print(f"\n[Lỗi] Có lỗi hệ thống xảy ra: {e}")

if __name__ == "__main__":
    main()
