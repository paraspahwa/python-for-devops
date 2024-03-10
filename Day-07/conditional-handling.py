import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok we will create a instance for you")
elif type == "t2.medium":
    print("it will charge you more")
else:
    print("your input is not correct")
