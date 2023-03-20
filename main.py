def z1():
    s=["5","7","9","90","120"]
    a=str(input())
    if a in s:
        print("Поздравляю,вы угадали число!")
    else:
        print("Упс,такого числа нет...")
def z2():
    s=["3","8","12","3","12","21","3"]
    print(s)
    povtor={x for x in s if s.count(x)>1}
    print(povtor)
def z3():
    days1=("понедельник","вторник","среда","четверг","пятница","суббота","воскресенье")
    a=int(input("введите желаемое кол-во выходных\n"))
    days=days1[::-1]
    print("ваши выходные дни:",days[:a])
    b=7-a
    days2=days1
    days2=days2[:b]
    print("ваши рабочие дни:",days2)
def z4():
    stud1=["Иванов","Сидоров","Петров"]
    stud2=["Помидоркин","Антонов","Андреев","Иванов"]
    sport=()
    sport=stud1+stud2
    print("1 группа",stud1)
    print("2 группа", stud2)
    print("спортивная команда",sport)
    print("длина кортежа",len(sport))
    sport.sort()
    print("спортивная команда по алфавиту", sport)
    if "Иванов" in sport:
        count=sport.count("Иванов")
        print("В команде есть студент(ы) с фамилией Иванов:",count)
    else:
        print(False)
if __name__=="__main__":
    print("угадайте число")
    z1()
    print("\n")
    print("проверка повтора чисел")
    z2()
    print("\n")
    print("Выходные")
    z3()
    print("\n")
    print("Фамилии")
    z4()