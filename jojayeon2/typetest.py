a = input("타입검사 : ")

def typetest(b):
    if b.isdecimal():
        a = int(b)
        print(f"int : {a}")
    else:
        print("문자열")

typetest(a)

