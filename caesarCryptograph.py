from cryptographer import Cryptographer
import random

class CaesarCryptograph(Cryptographer):

    @staticmethod
    def encrypt(text, key):
        text = text.lower()
        key = int(key)
        cryptoText = ''
        if key > 72:
            key %= 72
        if key == 72:
            key = 41
        for i in range(len(text)):  # encrypt
            if text[i] in Cryptographer.RUS_ALP:
                if Cryptographer.RUS_ALP.index(text[i]) + key > len(Cryptographer.RUS_ALP) - 1:
                    newInd = Cryptographer.RUS_ALP.index(text[i]) + key - len(Cryptographer.RUS_ALP)
                else:
                    newInd = Cryptographer.RUS_ALP.index(text[i]) + key
                cryptoText += Cryptographer.RUS_ALP[newInd]
            if text[i] not in Cryptographer.RUS_ALP:  # not change signs in text
                cryptoText += text[i]
        return cryptoText

    @staticmethod
    def decrypt(cryptoText, key):  # decrypt
        cryptoText = cryptoText.lower()
        key = int(key)
        if key > 32:
            key %= 32
        deCryptoText = ''
        for i in range(len(cryptoText)):  # decrypting reverse algo
            if cryptoText[i] in Cryptographer.RUS_ALP:
                if Cryptographer.RUS_ALP.index(cryptoText[i]) - key < 0:
                    newInd = len(Cryptographer.RUS_ALP) + (Cryptographer.RUS_ALP.index(cryptoText[i]) - key)
                else:
                    newInd = Cryptographer.RUS_ALP.index(cryptoText[i]) - key
                deCryptoText += Cryptographer.RUS_ALP[newInd]
            if cryptoText[i] not in Cryptographer.RUS_ALP:
                deCryptoText += cryptoText[i]
        return deCryptoText


