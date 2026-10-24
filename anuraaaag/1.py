#to print name and age
name = "Anurag"
age="20"
print("my name is",name)
print("my age is",20)
#add two numbers
a = 19
b = 18
print(a+b)
#Even or odd
num = 7
if num%2==0:
    print("Even")
else:
    print("odd")
    #to find greatest among 2 numbers
a = 9
b = 8
if(a>b):
    print("a is greater")
else:
    print("b is greater")
#print num 1 to 10
for i in range (1,11):
    print(i)
#print multiplication table of number
num = 5
for i in range(1,11):
    print(num, "x", i , "=", num * i)
    #to print sum of numbers from 1 to n
    n = 5
    total = 0
    for i in range (1, n+1):

      total = total + i
print("Total =", total)
#count the characters in string
text="Believe"
count =len(text)
print("characters =",count)
#To revers a string
text = "Siuuuuu"
reverse =text [::-1]
print(reverse)
#find the  largest no. in list
numbers = [10,20,30,40,51,50]
largest = max(numbers)
print("Largest =",largest)
#create a function to add 2 numbers
def sub(a, b):
    return b - a

result = sub(10, 20)
print(result)
#calculate total markks and percentage
marks = [80, 83, 90, 85, 70]

total = sum(marks)
percentage = (total / 500) * 100

print("Total marks =", total)
print("Percentage =", percentage, "%")
#find the largest element in list
numbers ={21,1,22,54,63,54,67,98,99}
largest = max(numbers)
print("largest=",largest)
