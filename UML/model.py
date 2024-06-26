@startuml



legend bottom left
    //~# переменные аннотаций//
    TypeCrParam = Type[CreatureParameter]
    KParamsDict = dict[TypeCrParam, KindParameter]
    Range = tuple[float, float]
end legend

interface dict1 as "dict"
interface dict2 as "dict"

interface DictOfRanges {
    <font:Brass Mono><size:12>(int, int): Any
    --
    __init__()
    __getitem__()
}

class Kind {
    <font:Brass Mono><size:12>(int, int): MatureStage
    --
    +file_name: <i>str</i>
    +str_name: <i>str</i>
}

class MatureStage {
    +days: <i>int</i>
    +time_before_act: <i>int</i>
    +params: <font:Noto Mono><size:14>KParamsDict
    +user_actions: <i>list</i> [UserAction]
    +creature_actions: <i>list</i> [CreatureAction]
}

abstract Parameter {
    -min: <i>float</i>
    -max: <i>float</i>
    -delta: <i>float</i>
}

class KindParameter << dataclass >> {
    +cls: <font:Noto Mono><size:14>TypeCrParam
    +default: <i>float</i>
}

class Creature {
    +kind: Kind
    #age: <i>int</i>
    +params: Parameters
    +user_actions: <i>list</i> [UserAction]
    -creature_actions: <i>list</i> [CreatureAction]
    --<size:12>// getters  // --
    +age → <i>int</i>
    --<size:12>// setters  // --
    +age()
    --<size:12>// methods  // --
    -grow_up()
    +act()
}

class Parameters {
    <font:Brass Mono><size:12>TypeCrParam: CreatureParameter
    --
    __setitem__()
    +update()
}

abstract CreatureParameter {
    +{static}name: <i>str</i>
    -params: Parameters
    #value: <i>float</i>
    --<size:12>// getters  // --
    +range → <font:Noto Mono><size:14>Range
    +value → <i>float</i>
    --<size:12>// setters  // --
    +value()
    --<size:12>// methods  // --
    +{abstract}update()
}

class Health {
    +update()
}

class Satiety {
    +update()
}

class Emotion {
    +update()
}

abstract Action {
    -animation_timer: <i>int</i>
    -description: <i>str</i>
    -params: Parameters
    +animate()
    +{abstract}param_change()
}

abstract UserAction

abstract CreatureAction {
    -probability: <i>int</i>
    --<size:12>// getters  // --
    +{abstract}probability → <i>int</i>
}

class Feed {
    +param_change()
}

class Play {
    +param_change()
}

class ChasingTail {
    +param_change()
}

class Sleep {
    +param_change()
}

hide abstract empty members
hide class empty members
hide interface empty members

left to right direction

dict1 <|- DictOfRanges
dict2 <|- Parameters

DictOfRanges <|- Kind

Kind o- MatureStage

Parameter <|- KindParameter
Parameter <|-- CreatureParameter

MatureStage o-- KindParameter
MatureStage o-- Action

Creature o-up- Kind
Creature o-- Parameters
Creature o-left- Action

Parameters o-o CreatureParameter

CreatureParameter <|-- Health
CreatureParameter <|-- Satiety
CreatureParameter <|-- Emotion

Action <|-- CreatureAction
Action <|-- UserAction
Action o-right- Parameters

UserAction <|-- Feed
UserAction <|-- Play

CreatureAction <|-- ChasingTail
CreatureAction <|-- Sleep

@enduml
