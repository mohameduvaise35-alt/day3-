List:
--------
1.Write a Python program to find the sum of all elements in a list.
2.Write a Python program to find the number of elements in a list.
3.Write a Python program to find the largest element in a list without using max().
4.Write a Python program to find the smallest element in a list without using min().
5.Write a Python program to count the number of even and odd elements in a list.
6.Write a Python program to reverse a list without using reverse().
7.Write a Python program to check whether a given element is present in a list.
8.Write a Python program to Merge two lists.
9.Separate even and odd numbers into two different lists.
10.Find the second largest element in a list.
_____________________________________
(List)
1.
lst = [10, 20, 30, 40, 50]
total = 0
for i in lst:
    total += i
print("Sum =", total)

2.
lst = [10, 20, 30, 40, 50]

count = len(lst)

print("Number of elements =", count)

3.
l= [10, 20, 30, 40, 50]
largest = l[0]
for i in l:
    if i > largest:
        largest = i
print("Largest element =", largest)


4.
l= [10, 20, 30, 40, 50]
largest = l[0]
for i in l:
    if i <largest:
        largest = i
print("Largest element =", largest)


5.
lst = [10, 15, 20, 25, 30]

even = 0
odd = 0

for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count =", even)
print("Odd count =", odd)

6.
lst = [10, 20, 30, 40, 50]

rev = []

for i in lst:
    rev = [i] + rev

print("Reversed list =", rev)

7.
lst = [10, 20, 30, 40, 50]

x = int(input("Enter element: "))

if x in lst:
    print("Element found")
else:
    print("Element not found")

8.
lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

merged = lst1 + lst2

print("Merged list =", merged)

9.
lst = [10, 15, 20, 25, 30]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even list =", even)
print("Odd list =", odd)

10.
lst = [10, 20, 30, 40, 50]

lst.sort()

print("Second largest =", lst[-2])


_____________________________________

                            TUPLE
1. 
t = (10, 20, 10, 30, 10)

print(t.count(10))
2.t = (10, 20, 30, 40, 50)

print(t[::-1])
3.
t = ("John", 21, "Chennai")
name, age, city = t
print(name)
print(age)
print(city)
4.
t = (10, 20, 30, 40)
for i in t:
    print(i)
5.
t = (10, 20, 30, 40)

x = 20

if x in t:
    print("Found")
else:
    print("Not Found")
6.
t = (10, 20, 30)

lst = list(t)
print(lst)

tuple_2 = tuple(lst)
print(tuple_2)

_____________________________________

                            SET
1.
s = {10, 20, 30, 40}

if 20 in s:
    print("Found")
else:
    print("Not Found")

2.
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)

3.
s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 & s2)

4.
s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 - s2)

5.
s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 ^ s2)

6.
lst = [1, 2, 2, 3, 4, 4, 5]
result = list(set(lst))
print(result)

_____________________________________ 

                       DICTIONARY 

1.
student = {
    "name": "John",
    "age": 21,
    "city": "Chennai"
}

print(student)

2.
student = {
    "name": "John",
    "age": 21,
    "city": "Chennai"
}

student["course"] = "Python"

print(student)

3.
student = {
    "name": "John",
    "age": 21,
    "city": "Chennai"
}

for key, value in student.items():
    print(key, value)

4.
lst = [1, 2, 1, 3, 2, 1]

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
5.
d = {}

for i in range(1, 6):
    d[i] = i * i

print(d)


