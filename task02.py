#Реализуйте алгоритм перемешивания списка.
import random
def ShuffleList():
    list = [random.randint(0,10) for i in range(random.randint(5,20))]
    print(f"Cписок:\n {list}")
    random.shuffle(list)
    print(f"список после :\n{list}")

ShuffleList()