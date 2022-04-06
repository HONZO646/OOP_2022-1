from math import *

import pygame
from pygame.draw import *

pygame.init()
FPS = 30

ginger = (200, 115, 5)


def input_int():
    """
    Ввод числа и перевод его в тип int.
    Функция не принимает аргументов.
    """
    s_number = int(input())
    return s_number


def input_many():
    """
    Ввод нескольких чисел, перевод их в тип int и занесение их в массив
    Функция не принимает аргументов.
    """
    m_numbers = list(map(int, input().split()))
    return m_numbers


def angry_emoji():
    """
    Рисует злой смайлик
    Функция ничего не принимает
    """
    screen = pygame.display.set_mode((400, 400))
    screen.fill((80, 80, 80))
    screen.fill((80, 80, 80))
    circle(screen, (255, 255, 0), (200, 200), 170)
    circle(screen, (0, 0, 0), (200, 200), 170, 5)
    circle(screen, (255, 0, 0), (140, 140), 30)
    circle(screen, (0, 0, 0), (135, 140), 15)
    circle(screen, (255, 0, 0), (260, 140), 35)
    circle(screen, (0, 0, 0), (260, 140), 15)
    polygon(screen, (0, 0, 0), [(60, 85), (50, 75), (180, 115), (175, 120)])
    polygon(screen, (0, 0, 0), [(210, 120), (215, 115), (370, 75), (380, 85)])
    rect(screen, (0, 0, 0), (100, 260, 200, 15))


def draw_ellipse_angle(surface, color, rectangle, angle, width=0):
    """
    Функция поворота эллипса (взята с стаковерфлоу)
    surface - поверхность
    color - цвет
    rectangle - прямоугольник для рисования эллипса
    angle - угол поворота эллипса
    width - обводка(необязательный аргумент)
    """
    target_rect = pygame.Rect(rectangle)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def window_scale(x, y, i, screen):
    """
    Рисует окно с параметрами
    x: координата начала окна по горизонтали
    y: координата начала окна по вертикали
    i: коэффициент увелечения/уменьшения
    """
    i = i / 10
    x0 = 415
    y0 = 10
    x1 = - x0 * i + x
    y1 = - y0 * i + y
    rect(screen, (55, 208, 208), (415 * i + x1, 10 * i + y1, 375 * i, 325 * i))  # стекло
    rect(screen, (210, 250, 250), (415 * i + x1, 10 * i + y1, 375 * i, 325 * i), 20)  # рама 1
    line(screen, (210, 250, 250), (415 * i + x1, 130 * i + y1), (785 * i + x1, 130 * i + y1), 15)  # рама 2
    line(screen, (210, 250, 250), (600 * i + x1, 10 * i + y1), (600 * i + x1, 325 * i + y1), 15)  # рама 3


def cat_scale(x, y, i, screen, color):
    """
    Рисует кота с параметрами
    x: координата начала кота по горизонтали
    y: координата начала кота по вертикали
    i: коэффициент увелечения/уменьшения
    color: цвет кота - tuple длины 3, значения 0<=int<=255
    """
    i = i / 10
    x0 = 20
    y0 = 370
    x1 = - x0 * i + x
    y1 = - y0 * i + y

    def draw_tail():  # хвост
        draw_ellipse_angle(screen, color, [563 * i + x1, 360 * i + y1, 250 * i, 80 * i], 30, 0)
        draw_ellipse_angle(screen, (0, 0, 0), [563 * i + x1, 360 * i + y1, 250 * i, 80 * i], 30, 1)

    def draw_body():  # тело
        ellipse(screen, color, (100 * i + x1, 360 * i + y1, 530 * i, 165 * i))
        ellipse(screen, (0, 0, 0), (100 * i + x1, 360 * i + y1, 530 * i, 165 * i), 1)

    def draw_paw():  # лапа под головой
        ellipse(screen, color, (60 * i + x1, 430 * i + y1, 60 * i, 65 * i))
        ellipse(screen, (0, 0, 0), (60 * i + x1, 430 * i + y1, 60 * i, 65 * i), 1)

    def draw_head():  # голова
        ellipse(screen, color, (20 * i + x1, 375 * i + y1, 220 * i, 110 * i))
        ellipse(screen, (0, 0, 0), (20 * i + x1, 375 * i + y1, 220 * i, 110 * i), 1)

    def draw_front_paw():  # лапа передняя
        ellipse(screen, color, (130 * i + x1, 480 * i + y1, 130 * i, 50 * i))
        ellipse(screen, (0, 0, 0), (130 * i + x1, 480 * i + y1, 130 * i, 50 * i), 1)

    def draw_back_paw():  # лапа задняя (бедро)
        ellipse(screen, color, (450 * i + x1, 425 * i + y1, 180 * i, 115 * i))
        ellipse(screen, (0, 0, 0), (450 * i + x1, 425 * i + y1, 180 * i, 115 * i), 1)

    def draw_left_ear():  # левое ухо
        polygon(screen, color,
                [(x, y), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)])  # левое ухо снаружи
        polygon(screen, (0, 0, 0), [(x, y), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)], 1)

        polygon(screen, (250, 180, 240),
                [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1),
                 (34 * i + x1, 403 * i + y1)])
        polygon(screen, (0, 0, 0),
                [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1), (34 * i + x1, 403 * i + y1)],
                1)

    def draw_right_ear():  # правое ухо
        polygon(screen, color, [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1),
                                (160 * i + x1, 382 * i + y1)])
        polygon(screen, (0, 0, 0),
                [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1), (160 * i + x1, 382 * i + y1)], 1)

        polygon(screen, (250, 180, 240), [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1),
                                          (172 * i + x1, 381 * i + y1)])  # правое ухо внутри
        polygon(screen, (0, 0, 0),
                [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1), (172 * i + x1, 381 * i + y1)], 1)

    def draw_left_eye():  # левый глаз
        ellipse(screen, (114, 158, 47), (55 * i + x1, 410 * i + y1, 55 * i, 40 * i))
        ellipse(screen, (0, 0, 0), (55 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)
        ellipse(screen, (0, 0, 0), (85 * i + x1, 410 * i + y1, 10 * i, 40 * i))  # левый зрачок
        draw_ellipse_angle(screen, (255, 255, 255), [73 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)  # левый блик

    def draw_right_eye():  # правый глаз
        ellipse(screen, (114, 158, 47), (150 * i + x1, 410 * i + y1, 55 * i, 40 * i))
        ellipse(screen, (0, 0, 0), (150 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)
        ellipse(screen, (0, 0, 0), (180 * i + x1, 410 * i + y1, 10 * i, 40 * i))  # правый зрачок
        draw_ellipse_angle(screen, (255, 255, 255), [168 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)  # правый блик

    def draw_nose():  # нос
        polygon(screen, (250, 180, 240),
                [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
                 (115 * i + x1, 450 * i + y1)])
        polygon(screen, (0, 0, 0),
                [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
                 (115 * i + x1, 450 * i + y1)], 1)
        line(screen, (0, 0, 0), (127 * i + x1, 457 * i + y1), (127 * i + x1, 467 * i + y1), 1)

    def draw_mouth_whisker():  # рот
        arc(screen, (0, 0, 0), [127 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)
        arc(screen, (0, 0, 0), [111 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)

        # усы
        arc(screen, (0, 0, 0), [-80 * i + x1, 444 * i + y1, 700 * i, 500 * i], 1.55, 1.9)
        arc(screen, (0, 0, 0), [-78 * i + x1, 455 * i + y1, 700 * i, 200 * i], 1.55, 1.9)
        arc(screen, (0, 0, 0), [-145 * i + x1, 463 * i + y1, 700 * i, 200 * i], 1.3, 1.7)

        arc(screen, (0, 0, 0), [-375 * i + x1, 440 * i + y1, 700 * i, 500 * i], 1.2, 1.65)
        arc(screen, (0, 0, 0), [-410 * i + x1, 448 * i + y1, 700 * i, 200 * i], 1.1, 1.5)
        arc(screen, (0, 0, 0), [-345 * i + x1, 460 * i + y1, 700 * i, 200 * i], 1.3, 1.75)

    draw_tail()
    draw_body()
    draw_paw()
    draw_head()
    draw_front_paw()
    draw_back_paw()
    draw_left_ear()
    draw_right_ear()
    draw_left_eye()
    draw_right_eye()
    draw_nose()
    draw_mouth_whisker()


def ball_scale(x, y, i, screen):
    """
    Рисует клубок с параметрами
    x: координата начала клубочка по горизонтали
    y: координата начала клубочка по вертикали
    i: коэффициент увелечения/уменьшения
    """
    i = i / 10
    x0 = 400
    y0 = 560
    x1 = - x0 * i + x
    y1 = - y0 * i + y

    ellipse(screen, (180, 180, 180), (400 * i + x1, 560 * i + y1, 135 * i, 100 * i))  # клубок
    ellipse(screen, (0, 0, 0), (400 * i + x1, 560 * i + y1, 135 * i, 100 * i), 1)
    arc(screen, (0, 0, 0), (420 * i + x1, 570 * i + y1, 100 * i, 75 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (405 * i + x1, 580 * i + y1, 100 * i, 50 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (325 * i + x1, 590 * i + y1, 185 * i, 100 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (430 * i + x1, 600 * i + y1, 80 * i, 80 * i), 2 * pi / 3, pi)
    arc(screen, (0, 0, 0), (450 * i + x1, 610 * i + y1, 80 * i, 80 * i), 2 * pi / 3, pi)

    arc(screen, (180, 180, 180), (310 * i + x1, 590 * i + y1, 300 * i, 60 * i), pi, 3 * pi / 2)  # нить
    arc(screen, (180, 180, 180), (160 * i + x1, 600 * i + y1, 150 * i, 40 * i), 0, pi)


def big_cat():
    """
    Рисует стандартных окно, кота и клубок (задание 2)
    Функция не принимает аргументов, ничего не вводите
    """
    screen = pygame.display.set_mode((800, 700))
    screen.fill((95, 80, 30))
    rect(screen, (140, 120, 50), (0, 350, 800, 350))  # стол
    window_scale(415, 10, 10, screen)  # окно
    cat_scale(20, 370, 10, screen, ginger)  # кот
    ball_scale(400, 560, 10, screen)  # клубок


def many_cats():
    """
    Рисует картину с множеством котов (задание 3)
    Функция не принимает аргументов, ничего не вводите
    """
    screen = pygame.display.set_mode((800, 700))
    screen.fill((95, 80, 30))
    rect(screen, (140, 120, 50), (0, 350, 800, 350))  # стол
    window_scale(415, 10, 10, screen)
    window_scale(10, 10, 10, screen)
    ball_scale(20, 370, 10, screen)
    ball_scale(50, 450, 3, screen)
    ball_scale(280, 550, 4, screen)
    ball_scale(111, 650, 4, screen)
    ball_scale(350, 500, 3, screen)
    ball_scale(550, 370, 6, screen)
    cat_scale(20, 370, 2, screen, ginger)
    cat_scale(50, 450, 3, screen, ginger)
    cat_scale(100, 600, 2, screen, ginger)
    cat_scale(350, 370, 3, screen, ginger)
    cat_scale(700, 370, 2, screen, ginger)
    cat_scale(450, 560, 4, screen, ginger)


def pygame_done():
    """
    Основные функции работы pygame и ее завершение
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()
