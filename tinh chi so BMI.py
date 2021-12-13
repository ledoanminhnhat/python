def BMI():

    import math
    w= int(input("can nang:"))
    h=int(input("chieu cao:"))


    num=  int(h)/int(math.sqrt(h))
    if num <16:
        print("gay cap do 3")
    elif 16<=num<17:
        print("Gay cap do 2")
    elif 17<= num <18.5:
        print("gay cap do 1")
    elif 18.5<= num <25:
        print("Binh thuong")
    elif 25<= num <30:
        print("thua can")
    elif 30<= num < 35:
        print("Beo phi cap do 1")
    elif 35<= num < 40:
        print("Beo phi cap do 2")
    elif num >40:
        print("Beo phi cap do 3")
    else:
        print("no value") 
if __name__=="__main__":
    BMI()