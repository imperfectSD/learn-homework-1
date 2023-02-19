"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
while True:
    try:
        how_are_you = (input("Как дела? "))
        if how_are_you == "Хорошо":
            break
    except (KeyboardInterrupt):
       print("Пока!") 
       break

if __name__ == "__main__":
    hello_user()
