hr_work=input("type number of hours")
base_rate=input("type base rate")

#print(hr_work)
#print(base_rate)

hr_work=int(hr_work)
base_rate=float(base_rate)
if hr_work<=40:

    pay=hr_work*base_rate
    print(pay)
else:
    pay=(40*base_rate)+((hr_work-40)*base_rate*1.5)
    print(pay)
