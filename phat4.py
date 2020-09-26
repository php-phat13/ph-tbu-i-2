a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))
if  ((a<b+c) and (b<a+c) and (c<b+c) and (a>0) and (b>0) and (c>0)):
        if( (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c== a*a+b*b)):
            print("Đay la Tam Giac Vuong")
        elif (a==b==c):
            print("Đay la Tam Giac Đeu")
        elif (a==b or a==c or b==c):
            print("Đay la Tam Giac Can")
        elif (a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
            print("Đay la Tam Giac Tu")
        else:
            print("Đay la Tam Giac Nhon")
else:
    print("Khong la tam Giac")