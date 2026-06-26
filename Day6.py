1. Write a program to count the number of words in a text file.
2. Create a class Vehicle with method start(). Override it in class Car.
3. Write a program with multiple except blocks (ValueError and ZeroDivisionError).
4. Write a program that raises a custom exception if marks are not between 0 and 100
5. Write a program that raises a custom exception if a user enters a negative number
6. Create a class Shape with method area(). Override it in classes Rectangle and Circle
7. Write a program to count the number of vowels in a text file
8. Write a program to write student details into a text file from csv fil
_____________________________________
1.f = open("Student.txt", "r")
text=f.read()
word=text.split()
print("The number of counts:",len(word))
f.close()

2.


class vehicle:
    def start(self):
        print("The vehicle starts")
class car(vehicle):
    def Start(self):
        print("The car st by a key")
c=car()
c.start()

3.
try:
    a=int(input ("Enter a number:"))
    b=int(input ("Enter a number:"))
    result=a*b
    print("result:", result)

except ValueError:
    print("Give valid number")
except ZeroDivisionError:
    print("cannot divide by zero")

4.

m=int(input("Enter a number:"))

try:
    if m<0 or m>100:
        raise  Exception ("Invalid numbers")
    print("Valid numbers")
except Exception as e:
    print(e)

5.

m=int(input("Enter a number:"))
try:
    if m<0 :
        raise  Exception ("Invalid numbers")
    print("Valid numbers")
except Exception as e:
    print(e)

6.

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        l = 5
        b = 4
        print("Rectangle Area =", l * b)
class Circle(Shape):
    def area(self):
        r = 3
        print("Circle Area =", 3.14 * r * r)
r = Rectangle()
c = Circle()
r.area()
c.area()

7 .
file = open("sample.txt", "r")

text = file.read()

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

file.close()
.u
8.
import csv

with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    with open("students.txt", "w") as txtfile:
        for row in reader:
            txtfile.write("ID: " + row[0] + ", Name: " + row[1] + "\n")

print("Data copied successfully")
