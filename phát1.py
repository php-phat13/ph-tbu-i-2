#Lập chương trình thực hiện công việc sau:
#    Nhập ba số a, b, c bất kì từ bàn phím
#    Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  
#(Kể cả trường hợp a=0)

print("giai phuong trinh bac 2: ax^2 + bx + c =0")
a = float(input("nhap a:"))
b = float(input("nhap b:"))
c = float(input("nhap c:"))
import math
if a==0:
 if b==0:
  if c==0:
print("phuong trinh vo so nghiem")
else:
	print("phuong trinh vo nghiem")
else:
	if c==0: 
		print("phuong trinh co 1 nghiem x=0 ")
	else:
		print("phuong trinh co 1 nghiem x=",-c/b)
	else:
		delta = b*b-4*a*c
		if delta < 0:
			print("phuong trinh vo nghiem")
			elif delta ==0
			print("phuong trinh co 1 nghiem x=",-b/(2*a))
		else:
			print("phuong trinh co 2 nghiem phan biet")
			print("x1=",float((-b-sqrt(delta))/(2*a)))
			print("x2=",float((-b+sqrt(delta))/(2*a)))
			