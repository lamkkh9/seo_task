import requests

def check(hotmail, pass_mail):
    url = f"https://tools.dongvanfb.net/api/get_messages?mail={hotmail}&pass={pass_mail}"
    payload = {}
    headers = {}
    try:
        # Thiết lập thời gian chờ tối đa là 10 giây
        response = requests.get(url, headers=headers, data=payload, timeout=10)
        
        # Kiểm tra xem yêu cầu có thành công không (status code 200)
        if response.status_code == 200:
            try:
                # Giải mã nội dung JSON từ phản hồi
                data = response.json()
                print("["+data["email"] +"] : "+ data["content"])
            except ValueError as e:
                print(f"Failed to decode JSON: {e}")
        else:
            # Nếu yêu cầu không thành công, in ra mã lỗi
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.Timeout:
        # Xử lý trường hợp thời gian chờ vượt quá
        print("Request timed out.")

input_file_path = "done.txt"
with open(input_file_path, "r", encoding="utf-8") as input_file:
    # Đọc từng dòng từ tệp tin đầu vào
    for line in input_file:
        # Tách các phần tử trong dòng bằng ký tự "|"
        hotmail, pass_mail = line.strip().split("|")
        check(hotmail, pass_mail)
