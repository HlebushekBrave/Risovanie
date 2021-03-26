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
                return count_hexagon
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
f_color=get_color_choice(first_color)
if f_color==a:
    col1='red2'
elif f_color==b:
    col1='gold'
elif f_color==c:
    col1='orange'
elif f_color==d:
    col1='RoyalBlue1'
elif f_color==e:
    col1='forest green'
elif f_color==f:
    col1='DeepSkyBlue2'
elif f_color==g:
    col1='black'
elif f_color==h:
    col1='saddle brown'
second_color=input('Пожалуйста, введите цвет: ')
n=second_color
sec_color=get_color_choice(second_color)
if sec_color==a:
    col2='red2'
elif sec_color==b:
    col2='gold'
elif sec_color==c:
    col2='orange'
elif sec_color==d:
    col2='RoyalBlue1'
elif sec_color==e:
    col2='forest green'
elif sec_color==f:
    col2='DeepSkyBlue2'
elif sec_color==g:
    col2='black'
elif sec_color==h:
    col2='saddle brown'
o=0
count_hexagon=(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
while o!=1:
    try:
        count_hexagon=int(count_hexagon)
        o=1
    except ValueError:
        o=0
        count_hexagon = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
counts=get_num_hexagons(count_hexagon)
print(counts)
print(col1, col2)
