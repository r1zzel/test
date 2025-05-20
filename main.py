import random
import os
from colorama import Fore

# Глобальные переменные, которые проще прописать в самом начале
is_cheatcode = False
rand_num = random.randint(0, 10)

# Создание собственного исключения для использования "читкода"
class TestError(Exception):
    pass

# Сама функция читкода. Выводит сообщение об активации читкода
def cheatcode(user_num:int):
    global is_cheatcode
    if user_num == 1707:
        raise TestError(Fore.LIGHTBLACK_EX + "Cheat actived!\n" + Fore.RESET)
    return True

# Фукция которая выводит текст самой игры. Очищает прошлый вывод для красоты
def gameText(attempts_count:int, previous_attempts:str):
    global is_cheatcode, rand_num
    os.system('cls')
    print("Guess the random number from 0 to 10 (including both end points)!")
    
    # Разветвление, проверяющее переменную "is_cheatcode", которая отвечает за доступ к самому читу
    if is_cheatcode:
        print(f"You have {Fore.LIGHTYELLOW_EX}{attempts_count}{Fore.RESET} attempts | Predicted number is {Fore.LIGHTGREEN_EX}{rand_num}{Fore.RESET}\n")
    else:
        print(f"You have {Fore.LIGHTYELLOW_EX}{attempts_count}{Fore.RESET} attempts\n")
    
    print(previous_attempts, end="")

# Функция игры, код выведен отдельно в функцию, чтобы была возможность досрочно (при победе) завершить код 
def theGame():
    global is_cheatcode
    global rand_num
    prev_attempts = ""

    for i in range(3):
        gameText(3-i, prev_attempts)
        while True:
            try:
                user_ans = int(input("$ "))
                cheatcode(user_ans)
            except ValueError: # Исключение значения - если введено не int
                prev_attempts = ""
                gameText(3-i, prev_attempts)
                print(Fore.LIGHTRED_EX + "You have writed no number\n" + Fore.RESET)
            except TestError as e: # Исключение читкода - при вводе числа 1707, активирует читкод, меняя значение "is_cheatcode" на True
                is_cheatcode = True
                prev_attempts = ""
                gameText(3-i, prev_attempts)
                print(e)
            else:
                break   
        if user_ans == rand_num:
            os.system('cls')
            print(f"Yes! Random number is {Fore.GREEN}{user_ans}{Fore.RESET}. {Fore.LIGHTYELLOW_EX}\nYou win!{Fore.RESET}")
            return 0
        else:
            prev_attempts = f"Nope. {Fore.RED}{user_ans}{Fore.RESET} isn't correct\n\n"

    os.system('cls')
    print(f"{Fore.RED}You lose!{Fore.RESET}\nRandom number is {Fore.LIGHTGREEN_EX}{rand_num}{Fore.RESET}")


if __name__ == "__main__":
    theGame()