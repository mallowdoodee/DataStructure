"""Missing module docstring"""
class Person:
    """Missing class docstring"""
    def __init__(self, name_, age_):
        self.name = name_.strip()
        self.age = age_

    def get_details(self):
        """get_details"""
        return "%s, %d years old" % (self.name, self. age)

    def say_hello(self):
        """say_hello"""
        return "Hello, my name is %s!" % self.name

USER_NAME = input()
USER_AGE = int(input())

PERSON = Person(USER_NAME, USER_AGE)
print(PERSON.get_details())
print(PERSON.say_hello())
