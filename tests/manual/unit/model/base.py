from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from numbers import Integral, Real
from typing import Any
from functools import cached_property
from enum import Enum

# переменные для аннотаций
RangesIterator = Iterable[tuple[tuple[Integral, Integral], Any]]


class DictOfRanges(dict):
    def __init__(self, iterator: RangesIterator):
        for elem in iterator:
            key, value = elem
            left, right = key
            if isinstance(left, Integral) and isinstance(right, Integral):
                if left < right:
                    continue
                else:
                    raise ValueError('first integer must be lower than second integer')
            else:
                raise TypeError('key for DictOfRanges must be iterable of two integers')
        super().__init__(iterator)
    
    def __getitem__(self, key_to_find):
        if isinstance(key_to_find, Integral):
            for key in self:
                left, right = key
                if left <= key_to_find <= right:
                    return super().__getitem__(key)
            raise KeyError(f'{key_to_find} is out of all ranges')
        else:
            return super().__getitem__(key_to_find)
    
    # def __setitem__(self, key, value):
    #     raise NotImplementedError

class Parameters(dict):

    def __setitem__(self):
        ...
    def update():
        ...
        
class Parameter(ABC):
    def __init__(self, min_: Real, max_: Real, delta: Real):
        if min_ <= max_:
            self._min = min_
            self._max = max_
        else:
            raise ValueError("'min' arg must be lower or equal than 'max' arg")
        self.delta = delta


class CreatureParameter(Parameter):
    
    name: str
    
    def __init__(self, params: Parameters, value: float):
        self.params = params
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value
    
    @cached_property
    def range(self) -> tuple[float, float]:
        return self._min, self._max
    
    @value.setter
    def value(self, new_value: float):
        if new_value <= self._min:
            self.__value = self._min
        elif self._max <= new_value:
            self.__value = self._max
        else:
            self.__value = new_value
    
    @abstractmethod
    def update(self) -> None:
        pass

####################################################
#                      Статы                      #
####################################################

class Strength:
    """ Сила """
    def update(self) -> None:
        pass
        
class Dexterity:
    """ Ловкость """
    def update(self) -> None:
        pass
        
class Intelligence:
    """ Интелект """
    def update(self) -> None:
        pass

####################################################
#                   Показатели                    #
####################################################  

class Health:
    """ Здоровье """
    def update(self) -> None:
        hunger = self.creature.params[Hunger]
        thirst = self.creature.params[Thirst]
        hygiene = self.creature.params[Hygiene]
        
        if hunger == 0:
            self.value -= 0.5
        if thirst == 0:
            self.value -= 0.5
        if hygiene == 0:
            self.value -= 0.5
                
class Mood:
    """ Настроение """
    def update(self) -> None:
        hunger = self.creature.params[Hunger]
        thirst = self.creature.params[Thirst]
        hygiene = self.creature.params[Hygiene]
        
        if hunger == 0:
            self.value -= 0.5
        if thirst == 0:
            self.value -= 0.5
        if hygiene == 0:
            self.value -= 0.5
        
class Hunger:
    """ Голод """
    def update(self) -> None:
        pass
    
class Thirst:
    """ Жажда """
    def update(self) -> None:
        pass    
        
class Hygiene:
    """ Гигиена """
    def update(self) -> None:
        pass
        
Parameters = Enum(
    """Перечислитель параметров."""
    'Parameters',
    {
        cls.__name__: cls
        for cls in CreatureParameter.__subclasses__()
    }
)