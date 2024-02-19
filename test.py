print("Добро пожаловать в наш сервис ВкусноПочти и точка, пожалуйста выберите что желаете:")

toppings = ["бигХит", "сырный соус", "нагетсы", "салат", "картошка фри",]
top1 = [ "кола", "сок", "пиво"]


for i in range(len(toppings)):
    print(f"{i+1}: {toppings[i]}")   
                    #список блюд

for i in range(len(top1)):
    print(f"{i+1}: {top1[i]}")                  #чтобы список напитков продолжался в порядке


user_burger = []

user_burger1 = []                                


while True:
   print("Если хотите завершить заказ,пожалуйста выберите позицию не из списка!")
   user_choice = int(input("Введите номер позиции блюда, который вы хотите"
                        "добавить"))
   if user_choice not in range(1, 6):                      
        print("Вы завершили заказ!")
        break
   else:
       user_burger.append(toppings[user_choice-1])
while True:
   print("Если хотите завершить заказ,пожалуйста выберите позицию не из списка!")
   user_choice1 = int(input("Введите номер позиции напитка, который вы хотите"
                        "добавить"))
   if user_choice1 not in range(1, 4):             # добавил функцию чтобы можно было разделить на группы таких как напитки и блюда
        print("Вы завершили заказ!")
        break
   else: 
        
        user_burger1.append(top1[user_choice1-1])



print(f"ваше блюдо: {','.join(user_burger)}")
print(f"ваш напиток: {','.join(user_burger1)}")

zakaz = input("Вам понравился наш сервис? выберите 'да' или 'нет' ")
