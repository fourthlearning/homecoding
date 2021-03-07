"""
โจทย์ : ให้แสดงผลดังนี้ โดยที่รับค่า input ตัว ชื่อจริง ชื่อเล่น เบอร์ เงินที่ตัวเองมี ราคาผัก และราคาที่เหลือ
My name is xxxxxxxxx
Nickname is xxxxxxxx
Tel : xxxxxxx
xxxxx มีเงิน xxxx ได้ซื้อผัก ราคา xxx.xx จะเหลือเงิน xxx.xxเท่าไหร่
"""
def main():
    name = input() # รับค่าชื่อจริงที่เป็น String
    n_name = input() # รับค่่าชื่อเล่นที่เป็น String
    tel = int(input()) # รับค่าเบอร์ที่เป็น int
    money = int(input()) # รับค่าเงินที่ตัวเองมี เป็นค่า String
    veg = float(input()) # รับค่าเงินที่จ่ายผักทั้งหมด เป็นค่า float

    total = float(money-veg) #ค่าเงินที่เหลือ

    print("My name is %s" %name)
    print("Nickname is %s" %n_name)
    print("Tel : %d" %tel)
    print("%s มีเงิน %d ได้ซื้อผัก ราคา %.2f จะเหลือเงิน %.2f" %(n_name,money,veg,total))

main()
