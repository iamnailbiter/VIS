class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzZZzzZZ"

    def count_legs(self):
        print "I have %s legs." % self.number_of_legs

class dog(pet):
    def bark(self):
        print "woof"


doug = dog()
doug.number_of_legs = 4
doug.count_legs()