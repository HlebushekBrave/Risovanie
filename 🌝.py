#Case-study 6
#Belozertseva Maria
#Adristi Fauzi
#Alexandra Raspopova
import turtle

#для 2 цветов и количества шестиугольников (рабочее):
def get_color_choice(n):
    i = 0
    while i != 1:
        try:
            if n == a or n == b or n == c or n == d or n == e or n == f or n == g or n == h:
                color = n
                i = 1
                print(color)
                return color
                break
            else:
                n = input("'"+n+"'"+" не является верным значением. Пожалуйста, повторите попытку: ")
                i = 0
                l = n
        except TypeError:
            n = input("'"+n+"'"+" не является верным значением. Пожалуйста, повторите попытку: ")
            i = 0
            continue
def get_num_hexagons(count_hexagon):
    i = 0
    while i != 1:
        try:
            if int(count_hexagon)>=4 and int(count_hexagon)<=20:
                i = 1
                print(count_hexagon)
                break
            else:
                count_hexagon = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
                i = 0
                l = count_hexagon
        except ValueError:
            i = 0
            count_hexagon = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
            continue
first_color = input('Пожалуйста, введите цвет: ')
n=first_color
a = 'красный'
b = 'желтый'
c = 'оранжевый'
d = 'синий'
e = 'зеленый'
f = 'голубой'
g = 'черный'
h = 'коричневый'
get_color_choice(first_color)
second_color=input('Пожалуйста, введите цвет: ')
n=second_color
get_color_choice(second_color)
o=0
count_hexagon=(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
while o!=1:
    try:
        count_hexagon=int(count_hexagon)
        o=1
    except ValueError:
        o=0
        count_hexagon = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
get_num_hexagons(count_hexagon)
#продолжить
if f_color==a or sec_color==a:
    col='red2'
elif f_color==b or sec_color==b:
    col='gold'
elif f_color==c or sec_color==c:
    col='orange'
elif f_color==d or sec_color==d:
    col='RoyalBlue1'
elif f_color==e or sec_color==e:
    col='forest green'
elif f_color==f or sec_color==f:
    col='DeepSkyBlue2'
elif f_color==g or sec_color==g:
    col='black'
elif f_color==h or sec_color==h:
    col='saddle brown'
