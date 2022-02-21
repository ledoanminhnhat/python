def sapxepsonguyen():
    # SẮP XẾP TĂNG DẦN
    
    num = [3,45,2,46,5,25,65,8,57,67]
    lenth = len(num)
    
    # Lặp từ phần tử đầu đến kế cuối,
    # Vì khi đến phần tử cuối là đã sắp xếp thànhcông
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (num[i] > num[j]):
                # Hoán đổi vị trí
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
    
    print(num)
if __name__=="__main__":
    sapxepsonguyen()
