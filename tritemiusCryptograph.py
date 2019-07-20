from cryptographer import Cryptographer


def inpFunction():
    return input('Введите вашу функцию с переменной x, без пробелов --> ')


def function(i, s):
    x = i
    return eval(s)


class TritemiusCryptographer(Cryptographer):

    @staticmethod
    def encrypt(text, func):
        text = text.lower()
        s = func
        cryptoText = ''
        for i in range(len(text)):
            if text[i] in Cryptographer.RUS_ALP:
                newInd = (Cryptographer.RUS_ALP.index(text[i]) + function(i, s))\
                         % len(Cryptographer.RUS_ALP)
                cryptoText += Cryptographer.RUS_ALP[newInd]
            else:
                cryptoText += text[i]
        return cryptoText

    @staticmethod
    def decrypt(cryptoText, func):
        cryptoText = cryptoText.lower()
        s = func
        deCryptoText = ''
        for i in range(len(cryptoText)):
            if cryptoText[i] in Cryptographer.RUS_ALP:
                newInd = (Cryptographer.RUS_ALP.index(cryptoText[i]) - function(i, s))\
                         % len(Cryptographer.RUS_ALP)
                deCryptoText += Cryptographer.RUS_ALP[newInd]
            else:
                deCryptoText += cryptoText[i]
        return deCryptoText





