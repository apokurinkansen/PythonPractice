# デコレータについて--------------------------
# def base_func(details = True):
#     #修飾すべき関数を受け取る
#     def outer(func):
#         # 本来の関数にわたすべき引数を受け取る
#         def inner(*args, ** keywds):
#             print("------------------------")
#             print(f'Name ={func.__name__}')
#             if(details):
#                 print(f'Args ={args}')
#                 print(f'Keywds = {keywds}')
#                 print("------------------------")
#             return inner
#     return outer

# @base_func(details=False)
# def hoge_func(x,y,m="bar",n="piyo"):
#     print(f'hoge:{x}-{y}/{m}-{n}')

# hoge_func(15,28,m ="ほげ",n="ピヨ")
# ------------------------------------------

# クロージャー--------------------------------
# def counter(init):
#     count = init
    
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment

# answer = counter(1)
# answerNext = counter(25)

# print(answer())
# print(answer())
# print(answerNext())
# print(answerNext())
# ------------------------------------------

# ジェネレータ--------------------------------
# import time

# def my_gen():
#     yield "アイウエオ"
#     time.sleep(10)
#     yield "かきくけこ"
#     yield "さしすせそ"

# for element in my_gen():
#     print(element)
# ------------------------------------------

# 素数を求めるジェネレータ----------------------
# import math

# def get_func():
#     num = 2
#     # 2から順に素数判定し、素数の倍位にだけyield
#     while True:
#         if check_func(num):
#             yield num
#         num +=1

# def check_func(value):
#     result = True
#     for y in range(2,math.floor(math.sqrt(value))+1):
#         if value % y ==0:
#             result = False
#             break
#     return result

# for i in get_func():
#     print(i)
#     if i > 100:
#         break
# ------------------------------------------

# 素数を求めるジェネレータ----------------------
def gen_com():
    while True:
        # 入力ボックスの呼び出し
        n = yield input("名前を入力してください:")
        # sendメソッドからの値でメッセージを生成
        yield f"こんにちわ、{n}さん!"
    
gen = gen_com()

for name in gen:
    # ジェネレーターからの戻り値(入力値)を再送
    res = gen.send(name.upper())
    # ジェネレーターからの戻り値を表示
    print(res)

# ------------------------------------------





