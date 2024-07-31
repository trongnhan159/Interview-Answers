# Bai 1
for i in range(1, 11):
    print (i)

# Bai 2
for i in range(1, 11):
    if i % 2 == 0:
        print ("a")
    else: 
        print(i)

# Bai 3
for i in range(1, 11):
    if i % 2 == 0:
        print ("a")
    elif i % 3 == 0:
        print("b")
    else: 
        print(i)

# Bai 4
for i in range(1, 11):
    if (i % 2 == 0 and i % 3 == 0):
        print("ab")
    elif i % 2 == 0:
        print ("a")
    elif i % 3 == 0:
        print("b")
    else: 
        print(i)

# Bai 5
thoigian = input("Moi ban nhap thoi gian: ")
def chuyenDoiThoiGian(thoigian):
    gio, phut = map(int, thoigian.split(":"))
    if gio > 12:
        buoi = "PM"
    else:
        buoi = "AM"
    gio = gio % 12
    if gio == 0:
        gio = 12
    return f"{gio}:{phut:02d} {buoi}"

print(chuyenDoiThoiGian(thoigian))

    