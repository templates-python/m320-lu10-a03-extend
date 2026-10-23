class Phone:
    def __init__(self):
        self._phonenumber = '+41 789 56 43'

    def calling(self):
        print('anrufen')

    def what_i_am(self):
        return ('a simply phone')

    # Test


if __name__ == '__main__':
    p = Phone()
    print(p.what_i_am())
    p.calling()