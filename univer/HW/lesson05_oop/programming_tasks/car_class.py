from ua.univer.HW.lesson05_oop.programming_tasks.task02_car import Car

def main():
    car1 = Car('Chevrolet 1968', 'General Motors', 0)
    for i in range(5):
        car1.accelerate()
    print(car1.get_speed())




main()
