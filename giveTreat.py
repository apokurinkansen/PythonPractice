import random

class giveTreat:
    name = []
    name_lenghs = 0

def main():
    show_menu()
    input_name()
    check_giveHuman()

def show_menu():
    print("-----------------------------")
    print("奢る人はだーーーーーーーれだ❤︎")
    print("名前を入力してね")
    print("-----------------------------")

def input_name():
    giveTreat.name = input("名前をカンマ(,)区切りで入力してください").split(",")
    giveTreat.name_lenghs = len(giveTreat.name)

def check_giveHuman():
    num = random.randint(0,giveTreat.name_lenghs)
    print("奢る人は、",giveTreat.name[num],"で決定!!!!!!")

main()


