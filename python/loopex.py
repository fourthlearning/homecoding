"""
โจทย์ เรื่อง while loop ให้ มีจำนวน 1 - 50 โดยแสดงผลที่หาร 3 ลงตัว

def main():
    i = 0
    while (i<50):
        i += 1
        if (i%3):
            continue
        print(i)  
main()


โจทย์ เรื่อง for loop ให้ มีจำนวน 1 - 50 โดยแสดงผลที่หาร 3 ลงตัว 
และ แสดงออกมาในบรรทัดเดียวกัน

def main():
    #for i in range (50):
    for i in range (1, 50):
        i += 1
        if (i%3):
            continue
        print(i) 
main()
"""
def main():
    num1 = ["1", "2", "3"]
    num2 = ["4", "5", "6"]
    num3 = ["7", "8", "9"]

    for x in num1:
        for y in num2:
            #print(x,y)
            for z in num3:
                print(x, y, z)
main()