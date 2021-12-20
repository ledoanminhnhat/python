def bangcuuchuong():
    

    for number in range(1,10):
        for i in range(1,10):
            print(str(number) + ' x ' + str(i) + ' = ' + str(number*i))
def bangcuuchuonghamwhile():
    number=1
    i=1
    while number <10:
        
        while i<10:
             print(str(number) + ' x ' + str(i) + ' = ' + str(number*i))
             i=i+1
        number=number+1
if __name__=="__main__":
    bangcuuchuong()
    bangcuuchuonghamwhile()

