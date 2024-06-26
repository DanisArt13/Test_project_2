@startuml


allowmixing

abstract list
hide abstract empty members

class App {
    +creature: model.Creature
    -{static}is_live() → <i>bool</i>
}

class LoadCreature {
    +{static}default_path: <i>Path</i>
    +{static}game_days_to_real_hours: <i>frac</i>
    +{static}save() → <i>None</i>
    +{static}load() → model.Creature
    #{static}params_evolution() → model.State
}

class LoadKinds {
    +{static}default_path: <i>Path</i>
    #generate()
    #read_file()
    __init__()
}

class MainMenu {
    +{static}choose_kind() → model.Creature
    -{static}show_kinds() → <i>None</i>
}

collections Kind

App ..> LoadCreature
App ..> MainMenu

list <|-- LoadKinds
LoadKinds o.. Kind

MainMenu .left.> LoadKinds

@enduml