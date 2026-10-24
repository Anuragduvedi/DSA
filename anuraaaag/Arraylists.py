#find the largest element in list
numbers ={21,1,22,54,63,54,67,98,99}
largest = max(numbers)
print("largest=",largest)
#to  find second largest element
numbers = [73,87,46,3,22,34,3,44,42]
numbers.sort()
print ("Second largest =", numbers[-2])
#reverse a list without using reverse()
numbers = [10, 20, 30, 40, 50]
result = numbers[::-1]
print(result)
#Remove duplicate elements from a list
numbers = [10, 20, 10, 30, 20, 40]
result = list(set(numbers))
print(result)
# Count even and odd numbers in a list.
numbers = [10, 15, 20, 7, 8, 3]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)
#to chk palindrome or no
word = input("Enter a word:")
reverse_word = word[::-1]

if word ==reverse_word:
    print(" value is palindrome")
else:
    print("value is not palindrome")
    #count vowels in string


