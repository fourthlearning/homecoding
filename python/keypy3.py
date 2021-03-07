"""
อาจารย์ประกาศนักเรียนคนนึง โดยบอกแค่คะแนนอย่างเดียว ให้นักเรียนประเมินเกรดตัวเองโดยมีเกณฑ์ ดังนี้
คะแนน 80 - 100 จะได้เกรด A
คะแนน 75 - 79 จะได้เกรด B+
คะแนน 70 - 74 จะได้เกรด B
คะแนน 65 - 69 จะได้เกรด C+
คะแนน 60 - 64 จะได้เกรด C
คะแนน 55 - 59 จะได้เกรด D+
คะแนน 50 - 54 จะได้เกรด D
นอกเงื่อนไข จะได้เกรด F 
***** ให้ input รับค่าคะแนนนักเรียน
"""
def main():
    score = float(input())
    print("คะแนนของนักเรียน : %.2f" %score)
    if(score >= 80 and score <= 100):    
        print("Grade : A")
    elif(score >= 75 and score <= 79.99):
        print("Grade : B+")
    elif(score >= 70 and score <= 74.99):
        print("Grade : B")
    elif(score >= 65 and score <= 69.99):
        print("Grade : C+")
    elif(score >= 60 and score <= 64.99):
        print("Grade : C")
    elif(score >= 55 and score <= 59.99):
        print("Grade : D+")
    elif(score >= 50 and score <= 54.99):
        print("Grade : D")
    elif(score >= 0 and score <= 49.99):
        print("Grade : F")
    else:
        print("นอกเงื่อนไข")
main()
