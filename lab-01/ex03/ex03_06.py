my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Dictionary ban đầu:", my_dict)
key_to_delete = input("Nhập khóa cần xóa: ")
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
    print("Dictionary sau khi xóa phần tử:", my_dict)
else:
    print("Khóa không tồn tại trong dictionary.")
