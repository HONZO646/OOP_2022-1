from func import *
pygame.init()
FPS = 30


def main_cycle():
    """
    Функция главного цикла.
    Функция ничего не принимает.
    """
    print('Выберите номер задания:')
    print(' 1. Вывод злого смайлика', '\n',
          '2. Вывод картины с котом', '\n',
          '3. Много котов (с возможностью выбора режима)')
    task = input_int()
    if task == 1:
        angry_emoji()
    elif task == 2:
        big_cat()
    elif task == 3:
        print('Выберите режим:', '\n',
              '1. Заданная картинка', '\n',
              '2. Расставить объекты самому')
        mode = input_int()
        if mode == 1:
            many_cats()
        elif mode == 2:
            screen = pygame.display.set_mode((800, 700))
            screen.fill((95, 80, 30))
            rect(screen, (140, 120, 50), (0, 350, 800, 350))  # стол
            window_scale(415, 10, 10, screen)
            window_scale(10, 10, 10, screen)
            print('Введите кол-во котов и клубков через пробел')
            a = input_many()
            cats, balls = a[0], a[1]
            print('Помните, что координата "y" края стола - 350')
            for i in range(1, cats+1):
                print('Введите координаты и размер (стандарт - 10) кота №', i)
                b = input_many()
                print('Введите цвет кота')
                color = input()
                cat_scale(b[0], b[1], b[2], screen, color)
            for i in range(1, balls+1):
                print('Введите координаты и размер (стандарт - 10) клубка №', i)
                b = input_many()
                ball_scale(b[0], b[1], b[2], screen)
        else:
            print('Такого режима работы не существует!')
    else:
        print('Такого задания не существует!')
    pygame_done()


print('Данная программа позволяет выводить на экран изображения, сделанные с помощью библиотеки PyGame', '\n')
z = 1
while z == 1:
    main_cycle()
    help(cat_scale)
    print('Хотите продолжить?', '\n',
          '1 - да', '\n',
          '2 - нет')
    z = input_int()
