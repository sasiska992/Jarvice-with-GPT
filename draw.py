from turtle import Turtle, Screen
import random


def get_half(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y


def draw_sierpinski():
    screen = Screen()
    screen.setup(width=1920, height=1080)
    pen = Turtle()
    size_x = screen.screensize()[0]
    size_y = screen.screensize()[1]
    pen.speed(0)
    pen.penup()

    # Включаем режим трейсеров
    screen.tracer(0)

    top = (0, size_y)
    left = (-size_x, -size_y)
    right = (size_x, -size_y)

    # Начальная случайная точка
    random_dot = (random.randint(-size_x, size_x), random.randint(-size_y, size_y))

    # Рисуем начальные точки
    pen.goto(top)
    pen.dot()
    pen.goto(left)
    pen.dot()
    pen.goto(right)
    pen.dot()

    # Основной цикл
    for _ in range(100000):  # Увеличьте количество итераций для более детального фрактала
        random_number = random.randint(1, 6)

        if random_number in [1, 2]:
            half_dot = get_half(top[0], top[1], random_dot[0], random_dot[1])
        elif random_number in [3, 4]:
            half_dot = get_half(left[0], left[1], random_dot[0], random_dot[1])
        else:
            half_dot = get_half(right[0], right[1], random_dot[0], random_dot[1])

        random_dot = half_dot
        pen.goto(half_dot[0], half_dot[1])  # Рисуем точку
        pen.dot()

    # Обновляем экран после завершения рисования
    screen.update()

    pen.hideturtle()  # Скрываем черепашку после завершения
    screen.mainloop()


if __name__ == '__main__':
    draw_sierpinski()
