# 4)Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при 
# просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет


a = input('Введите многозначное число:')
 
for i in range(len(a) - 1):
        if a[i] >= a[i+1]:
            print(a,'Нет') 
            break
else:    
    print(a,'Да')