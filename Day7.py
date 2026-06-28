enter n : 7

      *
     ***
    *****
   *******
  *********
 ***********
*************
 ***********
  *********
   *******
    *****
     ***
      *


--------------------------

enter n :5
    *
   * *
  *   *
 *     *
*********

-----------------------------

Enter no of rows: 6
     *
    **
   ***
  ****
 *****
******
 *****
  ****
   ***
    **
     *

---------------------------

n=6
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *

-------------------------------------------------------------
1.
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

2.
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * n):
        if i == n or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

3.
n = int(input("Enter no of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

4.
n = int(input("Enter n: "))

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
