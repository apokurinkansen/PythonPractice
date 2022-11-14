import random


count = 0

def main():
    show_menu()
    check_loap()

def show_menu():
    print("1から3の紐を選んでください")
    print("1  2  3 の数字を入力してください")

def check_loap():
    try:
        cmd = int(input(" < コマンド "))
    except (EOFError , InterruptedError):
        return

    ans_bomb = random.randint(1,3)

    if(ans_bomb == cmd):
        print("爆発!どーーーーーん!!!!!")
        return
    else:
        print("....セーフ")
        check_loap()

main()