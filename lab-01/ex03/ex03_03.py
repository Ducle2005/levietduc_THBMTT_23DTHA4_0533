input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(',')]
my_tuple = tuple(numbers)
print("List:", numbers)
print("Tuple tạo từ List:", my_tuple)
