# Nhập danh sách từ người dùng
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(',')]
sum_even = sum(x for x in numbers if x % 2 == 0)
print("Tổng các số chẵn trong danh sách là:", sum_even)
