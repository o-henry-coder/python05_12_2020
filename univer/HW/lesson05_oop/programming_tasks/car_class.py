from ua.univer.HW.lesson05_oop.programming_tasks.task02_car import Car

def main():
    car1 = Car('Chevrolet 1968', 'General Motors', 0)
    speed = 0
    for i in range(5):
        print(car1.accelerate(speed))
        print(car1.get_speed())




main()