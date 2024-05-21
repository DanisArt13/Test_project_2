from pathlib import Path
from pickle import dump
from sys import path

from model import *


kinds = [
    Kind(
        'cat',
        'кошка',
        MatureStage(
            5,
            KindParameter(Health, 0, 20, 0.5, 8),
            KindParameter(Satiety, 0, 25, 1.5, 0),
        ),
        MatureStage(
            40,
            KindParameter(Health, 0, 50, 0.4, None),
            KindParameter(Satiety, 0, 40, 1, None),
        ),
        MatureStage(
            20,
            KindParameter(Health, 0, 35, 0.6, None),
            KindParameter(Satiety, 0, 30, 0.8, None),
        ),
    ),
]


if __name__ == '__main__':
    
    test_data_dir = Path(path[0]).parent.parent / 'data'
    kinds_dir = test_data_dir / 'kinds'
    
    for kind in kinds:
        with open(kinds_dir / f'{kind.file_name}.kind', 'wb') as fileout:
            dump(kind, fileout)
    
    from pickle import load
    from pprint import pprint
