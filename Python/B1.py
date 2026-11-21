import random
ma_da_dung = set()
name = input("Nhập tên bệnh nhân:")
sex = input("Nhập giới tính:")
date_of_birth = int(input("Nhập năm sinh:"))
numbers_phone = input("Nhập số điện thoại:")
email =input("Nhập email:")
initial_symptoms = input("Nhập triệu chứng ban đầu:")
examination_fee = float(input("Nhập chi phí khám:"))

def tao_ma_benh_nhan(nam_sinh):
    ma_con_trong = []
    for so in range (100,1000):
        ma = f"BN{nam_sinh}{so}"
        if ma not in ma_da_dung :
            ma_con_trong.append(ma)
    if not ma_con_trong:
        raise ValueError("Đã hết mã cho năm sinh này")
    ma = random.choice(ma_con_trong)
    ma_da_dung.add(ma)
    return ma
ma_benh_nhan= tao_ma_benh_nhan(date_of_birth)
print("--- THẺ BỆNH NHÂN ---")
print(f"Mã BN       : {ma_benh_nhan}")
print("\n")
print(f"Tên         : {name} ({type(name).__name__})")
print(f"Giới tính   : {sex} ({type(sex).__name__})")
print(f"Năm sinh    : {date_of_birth} ({type(date_of_birth).__name__})")
print(f"Điện thoại  : {numbers_phone} ({type(numbers_phone).__name__})")
print(f"Email       : {email} ({type(email).__name__})  ")
print(f"Triệu chứng : {initial_symptoms} ({type(initial_symptoms).__name__})")
print(f"Chi phí     : {examination_fee} VND ({type(examination_fee).__name__})")