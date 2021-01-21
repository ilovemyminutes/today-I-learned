# 추상클래스
import abc


class Parent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def method_parent(self):
        pass


class Child(Parent):
    def method_child(self):
        return


temp = Child()
