import inspect
from functools import total_ordering, lru_cache


class Dummy:
    def __get__(self, instance, owner):
        return instance.dummy

    def __set__(self, instance, value):
        instance.sth = 10
        instance.dummy = value


@total_ordering
class Bot:
    def __init__(self, name):
        self.name = name
    property_1 = Dummy()
    property_2 = Dummy()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self) + "sss"

    def __eq__(self, other):
        return len(self.name) == len(other.name)

    def __lt__(self, other):
        return len(self.name) < len(other.name)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def say_hi(self):
        """
        >>>>>>>
        :return: gggg
        """
        print("My name is {self.name}".format(**locals()))

    def __getattr__(self, name):
        return "You want {}".format(name)




class AngryBot(Bot):
    def say_hi(self) -> Bot:
        """
        >>>>>>>
        :return: gggg
        """
        print("fuck off!")


class EvilBot(Bot):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        return AngryBot(*args, **kwargs)


@lru_cache()
def fib(n):
    print()
    if n < 2:
        return 2
    return fib(n-1) + fib(n-2)



if __name__ == "__main__":
    #n = int(input("List length: "))
    #print(sorted([Bot(str(i)) for i in range(n * 10, 0, -10)]))
    b = Bot("ddd")
    b.property_1 = "something"
    b.property_2 = "2222222"
    print(b.__dict__)
    print(b.property_1)
    print(vars(b))





