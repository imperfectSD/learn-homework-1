"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def strings_comparing(first_string, second_string):

      if first_string != str(first_string) and second_string != str(second_string):
        return 0
      elif first_string == second_string:
        return 1
      elif first_string != second_string and len(first_string) > len(second_string):
        return 2
      elif first_string != second_string and second_string == "learn":
        return 3  

    result_1 = strings_comparing(12345, 678910)
    result_2 = strings_comparing("learn python", "learn python")
    result_3 = strings_comparing("while drinking coffee", "learn python")    
    result_4 = strings_comparing("py", "learn")

    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    
if __name__ == "__main__":
    main()
