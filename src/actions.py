""" Активность Пета """

from pathlib import Path
from abc import ABC, abstractmethod
from base import Parameters, Creature

class Action(ABC):
    """ Совершить действие """
    name: str
    
    def __init__(
        self,
        animation_timer: int, 
        description: str, 
        params: Parameters
    ):
            self.animation_timer = animation_timer
            self.description = description
            self.params = params
    
    def __hash__(self):
        return hash(self.name)
        
    @abstractmethod
    def do(self) -> None:
        pass
    
    def animate():
        ...
    
    def param_change():
        ...
        
class CreatureAction(Action):
    """ Действия существа """
    
    def __init__(self, probability: int):
        self.probability = probability
        
    def __getter__(self, probability) -> int:
        ...
        
class UserAction(Action):
    """ Действие игрока """
    image: Path
    
#######################
# Управление Питомцем #
#######################

class Feed(UserAction):
    """ Покормить """
    def param_change():
        ...
    
class Drink(UserAction):
    """ Напоить """
    def param_change():
        pass  

class Washed(UserAction):
    """ Вымыть """
    def param_change():
        pass  

class PlayPet(UserAction):
    """ Поиграть """
    def param_change():
        pass  

class TrainPet(UserAction):
    """ Тренировать """
    def param_change():
        pass  
    
class Praise(UserAction):
    """ Похвалить """
    def param_change():
        pass  
    
#######################
# Активность Питомца #
#######################

class Walk(Action):
    """ Гуляет """
    def param_change():
        pass
    
class Sleep(Action):
    """ Бездействует """
    def param_change():
        pass

class Miss(Action):
    """ Скучает """
    def param_change():
        pass    
