class Employee:
    def __init__(self, wname, w_id):
        self.wname = wname
        self.w_id = w_id
    def set_name(self, wname):
        if wname.isalpha():
            self.wname = wname
        else:
            self.wname = None
            print('the name is incorrect')
    def get_name(self):
        return self.wname
    #@property
    # def w_id(self):
    #     return self.w_id
    #
    # @w_id.setter
    # def w_id(self, value):
    #     if value in range (1,1000):
    #         self.w_id = value
    #     else:
    #         self.w_id = None
    #         print('the value is incorrect')

    def __str__(self):
        return f"{self.wname}, {self.w_id}"


class ProductionWorker(Employee):
    def __init__(self, wname, w_id, shift_num, hourly_rate):
        Employee.__init__(self, wname, w_id)
        self.shift_num = shift_num
        self.hourly_rate = hourly_rate

    def set_shift_num(self, num):
        if num == '1':
            self.shift_num = num
            print(num, 'is daytime shift')
        elif num == '2':
            self.shift_num = num
            print(num, 'is nighttime shift')
        else :
            self.shift_num = None
            print('the shift value is incorrect')

    def get_shift_num(self):
        return self.shift_num
    # @property
    # def shift_num(self):
    #     return self.shift_num
    #
    # @shift_num.setter
    # def shift_num(self, value):
    #         if value == 1:
    #             self.shift_num = value
    #             print(value, 'is daytime shift')
    #         elif value == 2:
    #             self.shift_num = value
    #             print(value, 'is nighttime shift')
    #         else:
    #             print('the shift value is incorrect')

    def __str__(self):
        return f"{Employee.__str__(self)}, {self.shift_num}, {self.hourly_rate}"


if __name__ == '__main__':

    print('Please, enter your data')
    worker = ProductionWorker('Tom', 86, 2, 767)
    wname = input('Name ')
    worker.set_name(wname)
    worker.w_id = input('id number ')

    # worker.w_id = input('id number ')
    shift_num = input('shift number ')
    worker.set_shift_num(shift_num)
    worker.hourly_rate = input('hourly rate ')

    print('here is your data')
    print('==========================')
    print(worker)
    print('The name: ', worker.get_name())
    print('id number: ', worker.w_id)
    print('shift number: ', worker.get_shift_num())
    print('hourly rate: ', worker.hourly_rate)