num = int(input('enter the number'))
even =[]
odd = []
def check(num):
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
check(num)
if (len(even)>0 and len(odd)<=0):
    print(even,"even no")
else:
    print(odd,"odd no ")