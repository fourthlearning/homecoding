"""
 โดยกำหนดข้อมูลให้ดังนี้ ["Toyota","Isuzu","Honda","Mitsubishi","Ford","Nissan","Mazda","Suzuki","MG","Chevrolet"]
"""

def main():
    cars = ["Toyota","Isuzu","Honda","Mitsubishi","Ford","Nissan","Mazda","Suzuki","MG","Chevrolet"]
    print(cars) 
    print("----------") 
    print(cars[2])
    print("----------") 
    print(cars[-3])
    print("----------") 
    print(cars[2:5])
    print("----------") 
    cars[3] = "BMW"
    print(cars) 
    print("----------") 
    print(cars[3])
    print("----------")
    cars.insert(4,"Volvo")
    print(cars) 
    cars.remove("Nissan")
    print("----------")
    print("จำนวนชนิดรถมี :",len(cars),"ชนิด ดังนี้")
    for x in cars:
        print(x)


main()

"""
โดยกำหนดข้อมูลให้ดังนี้ ("Toyota","Isuzu","Honda","Mitsubishi","Ford","Nissan","Mazda","Suzuki","MG","Chevrolet")
                        มีการใช้ Condition (If-else) และต้องใช้ทั้ง If และ Else โดยถามว่า BMW มีอยู่ใน Tuple มั้ย</p>
"""

def main():
    cars = ("Toyota","Isuzu","Honda","Mitsubishi","Ford","Nissan","Mazda","Suzuki","MG","Chevrolet")
    print(cars)
    print("----------")
    y = list(cars)
    y[2] = "BMW"
    cars = tuple(y)
    print(cars)
    print("----------")
    if "BMW" in cars:
        print("Yes, 'BMW' is in the cars tuple")
    else:
        print("No")
main()

"""
กำหนดให้
a = {1,4,3,2,5,7,6,8,9}
b = {2,5,8,0}
c = {0}
Output : ตัวแรกคือ การ Union กัน ทั้ง 3 ตัว
Output : ตัวสองคือ การ Intersection กัน ทั้ง 3 ตัว
Output : ตัวสามคือ ค่า c เป็นsubset ของ A มั้ย โดยใช้ สูตร issubset และใช้ If - else เข้ามาเป็นเงื่อนไขด้วย
"""

def main():
    a = {1,4,3,2,5,7,6,8,9}
    b = {2,5,8,0}
    c = {0}
    d = a.union(b,c)
    print(d)
    e = a.intersection(b,c)
    print(e)
    f  = c.issubset(a)
    if (f == True):
        print("c issubset a")
    else:
        print("c isnotsubset a")

main()
"""
no.4
"""

def main():
    mobile1 = {
        "name" : "Nokia",
        "year" : 2004
    }
    mobile2 = {
        "name" : "Samsung",
        "year" : 2007
    }
    mobile3 = {
        "name" : "Vivo",
        "year" : 2011
    }
    mobile4 = {
        "name" : "iPhone",
        "year" : 2004
    }
    mobile5 = {
        "name" : "Google Pixel",
        "year" : 2004
    }

    big = {
        "mobile1" : mobile1,
        "mobile2" : mobile2,
        "mobile3" : mobile3,
        "mobile4" : mobile4,
        "mobile5" : mobile5
    }
    for x,y in big.items():
        print(x,y)
main()
