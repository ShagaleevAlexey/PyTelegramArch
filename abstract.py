from abc import ABCMeta, abstractmethod, abstractproperty
from typing import List

class BotAbstract(metaclass=ABCMeta):

    @abstractmethod
    def configurate(self, views: List):
        pass

    @abstractmethod
    def start(self):
        pass

