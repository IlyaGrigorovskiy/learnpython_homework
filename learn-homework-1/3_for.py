"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

performance = [{'school_class': '5a', 'scores': [3,4,4,5,2]},
{'school_class': '6а', 'scores': [3,4,4,5,2,3,4,5,5,4,1,4]},
{'school_class': '7а', 'scores': [3,4,4,5,2,3,4,5,5,4,1,4]},
{'school_class': '7а', 'scores': [3,5,4,5,4,3,4,4,5,4,1,4]},
{'school_class': '8а', 'scores': [3,4,4,5,2,3,4,5,5,4,2,1,4]},
{'school_class': '10а', 'scores': [3,1,4,2,2,3,3,5,5,4,1,4]},
{'school_class': '9а', 'scores': [3,4,4,5,2,3,4,5,5,4,1,4,1,4]},
{'school_class': '10а', 'scores': [3,1,4,2,2,3,3,5,5,4,1,4]},
{'school_class': '10б,', 'scores': [3,4,4,5,2,3,4,5,5,4,1,4]},
{'school_class': '11а', 'scores': [3,4,2,5,2,3,4,5,5,4,1,4]},
{'school_class': '11б', 'scores': [3,4,4,1,2,3,4,5,1,4,1,4]}]
def main():
    scores_all_shool = []
    for i in performance:
        scores_all_shool.extend(i['scores'])
        average_class = sum(i['scores'])/len(i['scores'])
        print(f"Средняя оценка в {i['school_class']}:  {round(average_class,1)}")
    average_grade = sum(scores_all_shool)/len(scores_all_shool)
    print( f"Средняя оценка по школе: {round(average_grade,1)}")







if __name__ == "__main__":
    main()
