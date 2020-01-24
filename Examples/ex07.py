'''
Demo on Multiple inheritance
'''

class Phone:
    def __init__(self):
        print('Phone instantiated')
    def make_call(self):
        print('Making a call...')
    def receive_call(self):
        print('Receiving a call...')

class Camera:
    def __init__(self):
        print('Camera instantiated')
    def take_picture(self):
        print('Taking picture...')

class SmartPhone(Phone, Camera):
    def __init__(self):
        # super().__init__() # this will invoke the first constructor only
        Phone.__init__(self)
        Camera.__init__(self)
        print('SmartPhone instantiated')

def main():
    sp = SmartPhone()
    from ex01 import dirr
    print('Attributes in sp: ', dirr(sp))

if __name__=='__main__': main()