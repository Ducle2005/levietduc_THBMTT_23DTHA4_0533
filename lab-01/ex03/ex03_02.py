input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(',')]
numbers.reverse()
print("Danh sách sau khi đảo ngược:", numbers)
