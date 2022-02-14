def tudien():
    a= input("Nhap tu tieng anh:")
    Dict= {'dog':'cho','cat':'meo','monkey':'khi','car':'oto','pie':'banh'}

    for anh,viet in Dict.items():
        if  anh==a :
            print(anh,":",viet)
        else:
            print("No data")
        
if __name__=="__main__":
    tudien()