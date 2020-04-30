
def Computerpay(hr_work,base_rate):
	if int(hr_work)<=40:
		pay_amount=int(hr_work)*float(base_rate)
	else:
		pay_amount=(40*float(base_rate))+((int(hr_work)-40)*float(base_rate)*1.5)
	return pay_amount

hr_work=input("type number of hours")
base_rate=input("type base rate")
x=Computerpay(hr_work,base_rate)
print(x)
