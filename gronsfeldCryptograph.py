from cryptographer import Cryptographer


class GronsfeldCryptograph(Cryptographer):

    @staticmethod
    def encrypt(text, key):
        text = text.lower()
        cryptoText = ''
        key = str(key)
        for i in range(len(text)):
            if text[i] not in Cryptographer.RUS_ALP:
                cryptoText += text[i]
            else:
                realShift = int(key[i % len(key)])  # polyalphabet shift
                if Cryptographer.RUS_ALP.index(text[i]) + realShift > len(Cryptographer.RUS_ALP) - 1:
                    newInd = Cryptographer.RUS_ALP.index(text[i]) + realShift - len(Cryptographer.RUS_ALP)
                else:
                    newInd = Cryptographer.RUS_ALP.index(text[i]) + realShift
                cryptoText += Cryptographer.RUS_ALP[newInd]
        return cryptoText

    @staticmethod
    def decrypt(cryptoText, key):
        cryptoText = cryptoText.lower()
        deCryptoText = ''
        key = str(key)
        for i in range(len(cryptoText)):
            if cryptoText[i] not in Cryptographer.RUS_ALP:
                deCryptoText += cryptoText[i]
            else:
                realShift = int(key[i % len(key)])
                if Cryptographer.RUS_ALP.index(cryptoText[i]) - realShift < 0:
                    newInd = len(Cryptographer.RUS_ALP) + (Cryptographer.RUS_ALP.index(cryptoText[i]) - realShift)
                else:
                    newInd = Cryptographer.RUS_ALP.index(cryptoText[i]) - realShift
                deCryptoText += Cryptographer.RUS_ALP[newInd]
        return deCryptoText
