from PIL import Image
import os

def decode_message_from_image(image_path):
    print(f"Đang đọc ảnh để giải mã từ: {image_path}...")
    if not os.path.exists(image_path):
        print(f"[LỖI] Không tìm thấy ảnh tại: {image_path}")
        return None
        
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    pixels = list(img.getdata())
    
    bin_data = ""
    decoded_chars = []
    
    print("Đang tiến hành trích xuất các bit LSB...")
    
    for pixel in pixels:
        r, g, b = pixel
        
        # Đọc LSB từ R, G, B
        bin_data += str(r & 1)
        bin_data += str(g & 1)
        bin_data += str(b & 1)
        
        # Gom đủ 8 bits (1 byte) để chuyển đổi thành ký tự
        while len(bin_data) >= 8:
            byte_str = bin_data[:8]
            bin_data = bin_data[8:]
            
            byte_val = int(byte_str, 2)
            
            # Nếu gặp ký tự Null (\x00) thì dừng việc giải mã vì đây là dấu hiệu kết thúc
            if byte_val == 0:
                return "".join(decoded_chars)
                
            try:
                decoded_chars.append(chr(byte_val))
            except Exception:
                # Bỏ qua nếu có ký tự không thể giải mã
                pass
                
    # Nếu đi hết cả ảnh mà không gặp ký tự Null
    return "".join(decoded_chars)

def main():
    print("=== GIẤU TIN TRONG ẢNH (DECODE) ===")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    encoded_path = os.path.join(current_dir, "encoded_image.png")
    original_path = os.path.join(current_dir, "input_image.png")
    
    print("Vui lòng lựa chọn ảnh để tiến hành trích xuất tin:")
    print("1. Giải mã từ ảnh đã giấu tin (encoded_image.png)")
    print("2. Giải mã từ ảnh gốc (input_image.png) để kiểm tra")
    
    choice = input("Lựa chọn (1 hoặc 2): ").strip()
    
    if choice == '2':
        target_path = original_path
        is_original = True
    else:
        target_path = encoded_path
        is_original = False
        
    decoded_msg = decode_message_from_image(target_path)
    
    if decoded_msg is not None:
        print("\n--- Kết quả trích xuất ---")
        if is_original:
            print(f"Thông điệp trích xuất từ ảnh gốc: {decoded_msg[:100]}... (Rác dữ liệu)")
            print("\n[GIẢI THÍCH] Tại sao không lấy được thông điệp từ ảnh gốc?")
            print("- Trong ảnh gốc (input_image.png), các bit ít quan trọng nhất (LSB) chứa các chi tiết màu sắc tự nhiên của ảnh.")
            print("- Khi giải mã các bit này, chúng ta chỉ nhận được các giá trị ngẫu nhiên (rác dữ liệu) thay vì thông điệp bí mật.")
            print("- Chỉ khi ảnh đã qua quá trình giấu tin (encoded_image.png), các bit LSB mới được sắp xếp có chủ đích để tạo thành các ký tự của thông điệp.")
        else:
            print(f"Thông điệp bí mật trích xuất được: {decoded_msg}")
        print("--------------------------")

if __name__ == "__main__":
    main()
