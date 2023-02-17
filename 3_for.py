"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

# Создаём список словарей

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

# Посчитать и вывести суммарное количество продаж для каждого товара

sum_of_iPhone_sales = 0
for items_sold in sales[0]['items_sold']:
    sum_of_iPhone_sales += items_sold
print("Суммарное количество продаж iPhone 12 -", sum_of_iPhone_sales)

sum_of_Xiaomi_sales = 0
for items_sold in sales[1]['items_sold']:
    sum_of_Xiaomi_sales += items_sold
print("Суммарное количество продаж Xiaomi Mi11 -", sum_of_Xiaomi_sales)

sum_of_Samsung_sales = 0
for items_sold in sales[2]['items_sold']:
    sum_of_Samsung_sales += items_sold
print("Суммарное количество продаж Samsung Galaxy 21 -", sum_of_Samsung_sales)

# Посчитать и вывести среднее количество продаж для каждого товара

avg_of_iPhone_sales = sum_of_iPhone_sales / len(sales[0]['items_sold'])
avg_of_iPhone_sales = int(avg_of_iPhone_sales)
print("Cреднее количество продаж iPhone 12 -", avg_of_iPhone_sales)

avg_of_Xiaomi_sales = sum_of_Xiaomi_sales / len(sales[1]['items_sold'])
avg_of_Xiaomi_sales = int(avg_of_Xiaomi_sales)
print("Cреднее количество продаж Xiaomi Mi11 -", avg_of_Xiaomi_sales)

avg_of_Samsung_sales = sum_of_Samsung_sales / len(sales[2]['items_sold'])
avg_of_Samsung_sales = int(avg_of_Samsung_sales)
print("Cреднее количество продаж Samsung Galaxy 21 -", avg_of_Samsung_sales)

# Посчитать и вывести суммарное количество продаж всех товаров

sum_of_all_sales = sum_of_Xiaomi_sales + sum_of_iPhone_sales + sum_of_Samsung_sales
print("Cуммарное количество продаж всех товаров -", sum_of_all_sales)

# Посчитать и вывести среднее количество продаж всех товаров

avg_of_all_sales = sum_of_all_sales / 3
avg_of_all_sales = int(avg_of_all_sales)
print("Cреднее количество продаж всех товаров -", avg_of_all_sales)

if __name__ == "__main__":
    main()
