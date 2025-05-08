import random as rd

### Марк, не заскринил кароче создание имени
# у роботов, если допишешь, то круто будет)))

robots = []
money = 530

class Robot:
    global money
    def __init__(self):
        self.name = 'Вася'
        self.life = rd.randint(7, 10)
        self.result = rd.randint(90, 200)

    def hello(self):
        print('Привет, я {}, моя производительность {}'.format(self.name, self.result))

    def work(self):
        self.life -= 1
        return self.result

    def ddel(self):
        print("Я {} закончил свою жизнь".format(self.name))

def game():
            global money
            for robot in robots:
                money += robot.work()
                if robot.life == 0:
                    robot.ddel()
                    robots.remove(robot)

def start():
    global money
    rb = input("У вас сейчас {} роботов и {} средств. Сколько хотите купить? ".format(len(robots), money))
    if rb == '' or rb == '0':
        game()
    elif int(rb)*500 <= money:
        for i in range(int(rb)):
            robot = Robot()
            robot.hello()
            robots.append(robot)
        money -= int(rb) * 500
        game()
    else:
        print("У вас недостаточно средств")
        game()

if __name__ == '__main__':
    while True:
        start()
        if money >= 1000000:
            print('Вы миллионер!')
            break
