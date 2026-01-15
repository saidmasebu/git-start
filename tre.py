list = ["physics","chemistry",1997,2000]

print(list[2])
list[2] = 2001

print(list[2])
tup1 = ("physics","chemistry",1997,2000)
tup2 = (1,2,3,4,5,6,7)
print(tup1[0])
print(tup2[0])
number = 76
if number < 40:
    grade = "D"
elif number < 50:
    grade = "C"
elif number < 60:
    grade = "B"
else:
    grade = "A"
print("your grade is :", grade)

sum = 0
data = input("Enter a number or just enter to quit")
while data != "":
    number = float(data)
    sum += number
    data = input("Enter a number or just enter to quit")
print("sum is:", sum)
sum = 0
for count in range(1,100001):
    sum += count
print(sum)