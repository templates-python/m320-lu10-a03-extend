from mobile import Mobile

class SmartPhone(Mobile):

    def __init__(self):
        pass

    def use_internet(self):
        print('das Internet benutzen')

    def what_i_am(self):
        return ('a modern smartphone')

#Test
if __name__ == '__main__':
    s = SmartPhone()
    print(s.what_i_am())
    s.calling()
    s.handle_sms()
    s.use_internet()