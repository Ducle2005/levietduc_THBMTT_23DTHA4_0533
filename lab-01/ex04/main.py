from student_manager import StudentManager

def show_student_list(students):
    if not students:
        print("\nDanh sách sinh viên trống.")
        return
    print("\n" + "-" * 85)
    print(f"{'ID':<5} | {'Họ và tên':<25} | {'Giới tính':<10} | {'Chuyên ngành':<20} | {'ĐTB':<5} | {'Học lực'}")
    print("-" * 85)
    for s in students:
        print(f"{s.id:<5} | {s.name:<25} | {s.gender:<10} | {s.major:<20} | {s.gpa:<5.1f} | {s.rank}")
    print("-" * 85)

def main():
    manager = StudentManager()
    
    # Seed some sample data for demonstration
    manager.add_student("Nguyen Van A", "Nam", "ATTT", 8.5)
    manager.add_student("Tran Thi B", "Nu", "CNTT", 6.8)
    manager.add_student("Le Van C", "Nam", "KTPM", 4.5)
    
    while True:
        print("\n=== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên bởi ID")
        print("3. Xóa sinh viên bởi ID")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp sinh viên theo Điểm trung bình (GPA)")
        print("6. Sắp xếp sinh viên theo Chuyên ngành (Major)")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-8): ").strip()
        
        if choice == '1':
            print("\n--- THÊM SINH VIÊN MỚI ---")
            name = input("Nhập tên sinh viên: ")
            gender = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            try:
                gpa = float(input("Nhập điểm trung bình (GPA): "))
                if gpa < 0 or gpa > 10:
                    print("Lỗi: Điểm GPA phải nằm trong khoảng từ 0 đến 10.")
                    continue
                manager.add_student(name, gender, major, gpa)
                print("Thêm sinh viên thành công!")
            except ValueError:
                print("Lỗi: Điểm GPA phải là một số thực.")
                
        elif choice == '2':
            print("\n--- CẬP NHẬT THÔNG TIN SINH VIÊN ---")
            try:
                student_id = int(input("Nhập ID sinh viên cần cập nhật: "))
                name = input("Nhập tên mới: ")
                gender = input("Nhập giới tính mới: ")
                major = input("Nhập chuyên ngành mới: ")
                gpa = float(input("Nhập điểm GPA mới: "))
                if gpa < 0 or gpa > 10:
                    print("Lỗi: Điểm GPA phải nằm trong khoảng từ 0 đến 10.")
                    continue
                if manager.update_student(student_id, name, gender, major, gpa):
                    print("Cập nhật thông tin sinh viên thành công!")
                else:
                    print(f"Không tìm thấy sinh viên với ID = {student_id}")
            except ValueError:
                print("Lỗi: ID phải là số nguyên và GPA phải là số thực.")
                
        elif choice == '3':
            print("\n--- XÓA SINH VIÊN ---")
            try:
                student_id = int(input("Nhập ID sinh viên cần xóa: "))
                if manager.delete_student(student_id):
                    print("Xóa sinh viên thành công!")
                else:
                    print(f"Không tìm thấy sinh viên với ID = {student_id}")
            except ValueError:
                print("Lỗi: ID phải là số nguyên.")
                
        elif choice == '4':
            print("\n--- TÌM KIẾM SINH VIÊN THEO TÊN ---")
            name = input("Nhập tên cần tìm kiếm: ")
            results = manager.search_by_name(name)
            show_student_list(results)
            
        elif choice == '5':
            print("\n--- SẮP XẾP SINH VIÊN THEO GPA (GIẢM DẦN) ---")
            manager.sort_by_gpa()
            show_student_list(manager.get_all_students())
            
        elif choice == '6':
            print("\n--- SẮP XẾP SINH VIÊN THEO CHUYÊN NGÀNH ---")
            manager.sort_by_major()
            show_student_list(manager.get_all_students())
            
        elif choice == '7':
            print("\n--- DANH SÁCH SINH VIÊN ---")
            show_student_list(manager.get_all_students())
            
        elif choice == '8':
            print("\nTạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại từ 1 đến 8.")

if __name__ == '__main__':
    main()
