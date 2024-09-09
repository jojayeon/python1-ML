a = '하이고'
b = '왜안됨'

def string_merge(a,b):
    return a+b

print(string_merge(a,b))

def string_merge2():
    global a,b
    return a+b

print(string_merge())


# 맨날 이름 쓰기 불편
def example():
    return "예제"

anther_example = lambda : "예제"

array = ["1","2","3"]
obj = {
    "조자연":"안녕",
    "김보미":"개굴",
    "황재민":"수면왕"
}

# 객체인데 ()소괄호?
another_obj = ("김정수","송이현","최유진")
# - 중복을 허용하지않는다.


