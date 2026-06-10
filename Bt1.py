# Danh sách chẩn đoán hiện tại của bệnh nhân
patient_diagnoses = ["Sốt Xuất Huyết"]


def add_diagnosis(raw_diagnosis, current_list):
    """
    Chuẩn hóa tên chẩn đoán và thêm vào hồ sơ bệnh án.
    """
    # Chuẩn hóa chuỗi: xóa khoảng trắng thừa + viết hoa chữ cái đầu mỗi từ
    cleaned = raw_diagnosis.strip().title()
    
    # Thêm chuỗi đã chuẩn hóa vào list (dùng append thay vì extend)
    current_list.append(cleaned)
    
    return current_list


# ====================== CHẠY CHƯƠNG TRÌNH ======================
new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)


# (1) PHÂN TÍCH LỖI
# 1. Tại sao hai dòng raw_diagnosis.strip() và raw_diagnosis.title() không làm thay đổi giá trị của biến raw_diagnosis?
# Vì String trong Python là immutable (bất biến). Các hàm strip(), title(), upper(), replace()... không thay đổi chuỗi gốc, mà trả về một chuỗi mới. Nếu không gán lại giá trị trả về vào biến, chuỗi cũ vẫn giữ nguyên.
# 2. Cách sửa để các hàm xử lý chuỗi có tác dụng?
# Phải gán lại kết quả vào biến:
# Pythoncleaned_diagnosis = raw_diagnosis.strip().title()
# 3. Phương thức extend() hoạt động như thế nào khi truyền vào một chuỗi?
# Khi truyền string vào extend(), Python coi chuỗi đó như một iterable (có thể duyệt từng ký tự). Do đó nó thêm từng ký tự riêng lẻ vào list thay vì thêm cả chuỗi làm một phần tử. Đó là lý do xuất hiện 'v', 'i', 'E', 'm', ...
# 4. Thay extend() bằng phương thức nào?
# Thay bằng append() — phương thức này thêm nguyên vẹn một phần tử vào cuối list.