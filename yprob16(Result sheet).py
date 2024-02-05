


name = input("Enter Student name : ")
mark = int(input("Enter Student mark : "))

print("\n\n")

if mark>100 or mark<0:
    print("Wrong mark in input")

elif mark>=80 :
    print(name+" you got A+")
    print("You gain ", mark, " marks")
elif mark>=75 :
    print(name+" you got A")
    print("You gain ", mark, " marks")
elif mark>=70 :
    print(name+" you got A-")
    print("You gain ", mark, " marks")
elif mark>=60 :
    print(name+" you got B")
    print("You gain ", mark, " marks")
elif mark>=50 :
    print(name+" you got C")
    print("You gain ", mark, " marks")
elif mark>=40 :
    print(name+" you got D")
    print("You gain ", mark, " marks")
else:
    print(name + " you are Fail in the Exam")
    print("You gain ", mark, " marks")

