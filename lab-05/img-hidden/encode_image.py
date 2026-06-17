from PIL import Image
import os

def msg_to_bin(msg):
    """Chuyển đổi chuỗi thông điệp thành chuỗi bit nhị phân (có ký tự Null \x00 kết thúc)"""
    bin_data = []
    for char in msg:
        bin_data.append(format(ord(char), '08b'))
    bin_data.append('00000000')  # Ký tự phân tách Null dùng để đánh dấu kết thúc thông điệp khi giải mã
    return ''.join(bin_data)

def encode_message_in_image(image_path, message, output_path):
    print(f"Đang đọc ảnh gốc từ: {image_path}...")
    if not os.path.exists(image_path):
        print(f"[LỖI] Không tìm thấy ảnh đầu vào tại: {image_path}")
        return False
        
    img = Image.open(image_path)
    # Đảm bảo ảnh ở định dạng RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    pixels = list(img.getdata())
    width, height = img.size
    
    # Chuyển thông điệp thành nhị phân
    bin_message = msg_to_bin(message)
    message_len = len(bin_message)
    
    # Kiểm tra xem ảnh có đủ dung lượng chứa thông điệp không
    # Mỗi pixel có 3 kênh màu (R, G, B), chứa được tối đa 3 bits
    capacity = len(pixels) * 3
    if message_len > capacity:
        print(f"[LỖI] Thông điệp quá dài ({message_len} bits). Ảnh chỉ chứa được tối đa {capacity} bits.")
        return False
        
    print(f"Dung lượng ảnh: {capacity} bits. Kích thước thông điệp cần giấu: {message_len} bits.")
    print("Đang tiến hành giấu tin vào các bit ít quan trọng nhất (LSB)...")
    
    new_pixels = []
    bit_idx = 0
    
    for pixel in pixels:
        r, g, b = pixel
        
        # Giấu bit vào kênh Red
        if bit_idx < message_len:
            r = (r & ~1) | int(bin_message[bit_idx])
            bit_idx += 1
            
        # Giấu bit vào kênh Green
        if bit_idx < message_len:
            g = (g & ~1) | int(bin_message[bit_idx])
            bit_idx += 1
            
        # Giấu bit vào kênh Blue
        if bit_idx < message_len:
            b = (b & ~1) | int(bin_message[bit_idx])
            bit_idx += 1
            
        new_pixels.append((r, g, b))
        
    # Tạo ảnh mới với dữ liệu pixel đã sửa đổi và lưu lại
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
    print(f"[SUCCESS] Đã giấu tin thành công và lưu ảnh mới tại: {output_path}")
    
    # Tự động mở ảnh vừa tạo ngay trong VS Code
    try:
        import subprocess
        subprocess.run(f'code -r "{output_path}"', shell=True)
        print("[*] Đã tự động mở ảnh đã giấu tin làm 1 tab trong VS Code.")
    except Exception as e:
        try:
            new_img.show()
            print("[*] Đã mở ảnh bằng trình xem ảnh mặc định của máy.")
        except Exception:
            print(f"[-] Không thể tự động mở ảnh: {e}")
        
    return True

def main():
    print("=== GIẤU TIN TRONG ẢNH (ENCODE) ===")
    
    # Thiết lập đường dẫn mặc định
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, "input_image.png")
    output_path = os.path.join(current_dir, "encoded_image.png")
    
    message = input("Nhập thông điệp bí mật muốn giấu vào ảnh: ")
    if not message:
        message = "Day la thong diep mat tu Le Viet Duc 0533"
        print(f"Sử dụng thông điệp mặc định: '{message}'")
        
    encode_message_in_image(input_path, message, output_path)

if __name__ == "__main__":
    main()
