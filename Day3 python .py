1.Write a function to check whether a given number is a palindrome.
2.Write a function to count the number of vowels in a string.
3.Write a function to reverse a string.
4.Write a function to check whether number is prime or not.
5.Write a function to check whether a given number is divisible by 3 & 8.
_____________________________________

1.def palindrome (n):
  original=n
  rev=0
  
  while(n>0):
   digit=n%10
   rev=(rev*10)+digit
   n=n//10
   
  return original== rev
  
num=int(input ("num:"))
if(palindrome (num)):
    print("palindrome ")
else:
    print("Not palindrome ")

Output:
Num:121
Palindrome 

2.def countvowels(s):
  count=0
  for v in s:
      if v in "aeiouAEIOU":
       count=count+1
  return count
text=(input ())  
print("The number of string:",countvowels(text))

 Output:e
The number of string:1

3.def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1

    return count


text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

4.def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("num: "))
if prime(num):
    print("its a prime")
else:
    print("its not a prime")

5.def check(num):
    if num % 3 == 0 and num % 8 == 0:
        print("Divisible by 3 and 8")
    else:
        print("Not divisible by 3 and 8")
n = int(input("Enter a number: "))
check(n)
