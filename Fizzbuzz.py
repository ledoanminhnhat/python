def fizzbuzz():
    a=int(input("Nhap bat dau:"))
    z=int(input("nhap ket thuc:"))
    if z<a:
        print("diem ket thuc phai lon hon bat dau")
    else:
        for i in range(a,z+1):
            if i%3==0 and i%5==0:
                print('Fizzbuzz')
            elif i%3==0:
                print('Fizz')
            elif i%5==0:
                print('Buzz')
            else:
                print(i)
if __name__=="__main__":
    fizzbuzz()