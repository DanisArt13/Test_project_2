""" Вестник Рагнарека """
# Когда здоровье равно 0, пет сдохнет -> Параметры здоровья от 0 до уровня
# Статы в интервале соответствующего уровня
# Статы меняются в зависимости от действий
# Потребление ресурса в зависимости от уровня и действий
# Количество прожитых дней для получения нового уровня

KIND(
    ('fenrir', 'фенрир'),
    MatureStage(
        5,
        KindParameter(Health, 0, 100, 0.5, 8),
        KindParameter(Satiety, 0, 100, 1.5, 0),
        KindParameter(Hungry, 0, 100, ),
        KindParameter(Hygiene, 0, 100, ),
        KindParameter(Strange, 30, 80, ),
        KindParameter(Dexterity, 50, 100, ),
        KindParameter(Intelligence, 10, 60, ),
        player_actions=[
            Feed(10), 
            Drink(5),
            Washed(),
            PlayPet(), 
            TrainPet(), 
            Praise(), 
        ],
        creature_actions=[
            Walk(0.9),
            Sleep(0.8),
            Miss(0.7),
        ]
    ),
    MatureStage(
        50,
        KindParameter(Health, 0, 100, 0.5, 8),
        KindParameter(Satiety, 0, 100, 1.5, 0),
        KindParameter(Hungry, 0, 100, ),
        KindParameter(Hygiene, 0, 100, ),
        KindParameter(Strange, 230, 280, ),
        KindParameter(Dexterity, 250, 350, ),
        KindParameter(Intelligence, 210, 260, ),
        player_actions=[
            Feed(10), 
            Drink(5),
            Washed(),
            PlayPet(), 
            TrainPet(), 
            Praise(), 
        ],
        creature_actions=[
            Walk(0.9),
            Sleep(0.8),
            Miss(0.7),
        ]
    ),
    MatureStage(
        30,
        KindParameter(Health, 0, 150, 0.5, 8),
        KindParameter(Satiety, 0, 150, 1.5, 0),
        KindParameter(Hungry, 0, 150, ),
        KindParameter(Hygiene, 0, 150, ),
        KindParameter(Strange, 180, 280, ),
        KindParameter(Dexterity, 200, 300, ),
        KindParameter(Intelligence, 160, 210, ),
        player_actions=[
            Feed(10), 
            Drink(5),
            Washed(),
            PlayPet(), 
            TrainPet(), 
            Praise(), 
        ],
        creature_actions=[
            Walk(0.9),
            Sleep(0.8),
            Miss(0.7),
        ]
    )
)
