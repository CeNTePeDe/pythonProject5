class  Animal:
    def __init__(self, head, legs, ears):
        self.head = head
        self.legs = legs
        self.ears = ears

    def voice(self, roar:str):
        print(roar.upper())

    def show(self):
        print('this is your dog')
