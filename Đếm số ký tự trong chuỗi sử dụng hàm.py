# #Đếm số ký tự trong chuỗi sử dụng hàm
# def dem():
#     input_str = input(str('Nhập chuỗi: '))
   

#     result = 0
#     for i in input_str:
#         if i in result:
#             result[i]+=1
#         else:
#             result[i]=1
#     for i in sorted(result, key=result.get, reserve=False):
#         print(i,result[i])
#     return result 
# if __name__=="__main__":
#     dem()

def _Demkytu():
    letters = 'abcabcdefghi'
    frequences = {}
    for c in letters:
        # lặp các ký tự trong chuỗi ký tự . lấy giá trị ban đầu 0
        # ... tăng lên 1
        # ... sau đó tăng lên 2, 3
        frequences[c] = frequences.get(c, 0) + 1
    for f in frequences.items():
        print(f)


if __name__ == "__main__":
    _Demkytu()

     


