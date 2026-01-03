# Key word Arugements : 

def display(uname,email,pwd):
    print(f"username: {uname}\nemail:{email}\npwd:{pwd}")
username=input()
gmail=input()
password=input()
display(uname=username,email=gmail,pwd=password)
display(email=gmail,uname=username,pwd=password)
display(email=gmail,pwd=password,uname=username)

# Default Arguments :

def display(uname,email,pwd,status="Absent"):
    print(f"username: {uname}\nemail:{email}\npwd:{pwd}")
display("subhash","subhashklvs@gmail.com","s@123")
display("lucky","lucky@gmail.com","lucky@123","present")


def display(*names):
    for i in names:
        print(i)
    print("--------")
display("ram","prasad","sujith")
display("subhash","lohith","sai teja","surya")
display("Abhinov","rakesh")
display("vishu")

# function that accepts any number of keyword arguments :

def display(**names):
    for i in names:
        print(f'{i}:{names[i]}')
    print("--------")
display(k1="ram",k2="prasad",k3="sujith")
display(n1="subhash",n2="lohith",n3="sai teja",n4="surya")
display(l1="Abhinov",l2="rakesh")
display(y1="vishu")

# Scope of The Variable : 

def display():
    global name
    name='lohit'
    print(f"Inside:{name}")
display()
print(f"outside:{name}")

# 

def display(course):
    print(f"starting:{course}")
    def change():
        nonlocal course
        course="python Full stack"
        print(f"change:{course}")
    change()
    print(f"Final course:{course}")
course="java Fill stack"
display(course)
    