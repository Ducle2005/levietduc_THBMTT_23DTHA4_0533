input_list = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ")
elements = input_list.split(',')
frequency = {}
for item in elements:
    item = item.strip()
    frequency[item] = frequency.get(item, 0) + 1
print("Số lần xuất hiện của các phần tử:", frequency)
