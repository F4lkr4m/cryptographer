from abc import ABC, abstractmethod


class Cryptographer(ABC):
    # create attributes of class
    RUS_ALP = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', \
               'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', \
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    cryptoText = ''
    key = 5
