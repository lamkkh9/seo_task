# Đường dẫn của tệp tin ban đầu
import os
input_file_path = os.getcwd() + "\\data\\hotmail.txt"

# Đường dẫn của tệp tin mới
output_file_path = "done.txt"

# Mở tệp tin đầu vào để đọc và tạo tệp tin đầu ra để ghi
with open(input_file_path, "r", encoding="utf-8") as input_file, open(output_file_path, "w") as output_file:
    # Đọc từng dòng từ tệp tin đầu vào
    for line in input_file:
        # Tách các phần tử trong dòng bằng ký tự "|"
        elements = line.strip().split("|")
        # Lấy hai phần tử đầu tiên
        first_two_elements = elements[:2]
        # Ghi hai phần tử vào tệp tin đầu ra, ngăn cách bằng "|"
        output_file.write("|".join(first_two_elements) + "\n")
