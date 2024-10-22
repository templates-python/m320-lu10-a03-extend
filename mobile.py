from phone import Phone

class Mobile(Phone):

    def __init__(self):
        pass

    def handle_sms(self):
        print('sms senden und empfangen')

    def what_i_am(self):
        return('an old mobile')

#Test
if __name__ == '__main__':
    mobile = Mobile()
    print(mobile.what_i_am())
    mobile.calling()
    mobile.handle_sms()