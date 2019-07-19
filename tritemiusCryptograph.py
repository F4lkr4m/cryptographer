from cryptographer import Cryptographer


def inpFunction():
    return input('Введите вашу функцию с переменной x, без пробелов --> ')


def function(i, s):
    x = i
    return eval(s)


class TritemiusCryptographer(Cryptographer):

    TriALP = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', \
                    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', \
                    'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', \
                    'ю', 'я', '.', ' ', '1', '2', '3', '4', '5', '6', \
                    '7', '8', '9', '0', ',', '-']

    @staticmethod
    def encrypt(text, func):
        s = func
        cryptoText = ''
        for i in range(len(text)):
            if text[i] in TritemiusCryptographer.TriALP:
                newInd = (TritemiusCryptographer.TriALP.index(text[i]) + function(i, s))\
                         % len(TritemiusCryptographer.TriALP)
                cryptoText += TritemiusCryptographer.TriALP[newInd]
            else:
                cryptoText += text[i]
        return cryptoText

    @staticmethod
    def decrypt(cryptoText, func):
        s = func
        deCryptoText = ''
        for i in range(len(cryptoText)):
            if cryptoText[i] in TritemiusCryptographer.TriALP:
                newInd = (TritemiusCryptographer.TriALP.index(cryptoText[i]) - function(i, s))\
                         % len(TritemiusCryptographer.TriALP)
                deCryptoText += TritemiusCryptographer.TriALP[newInd]
            else:
                deCryptoText += cryptoText[i]
        return deCryptoText





