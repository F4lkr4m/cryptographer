# const for alphabet
RUS_ALP = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', \
           'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', \
           'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def caesarCipher(text, key):  # cipher Caesar
    cryptoText = ''
    if key > 32:
        key %= 32
    for i in range(len(text)):  # encrypt
        if text[i] in RUS_ALP:
            if RUS_ALP.index(text[i]) + key > len(RUS_ALP) - 1:
                newInd = RUS_ALP.index(text[i]) + key - len(RUS_ALP)
            else:
                newInd = RUS_ALP.index(text[i]) + key
            cryptoText += RUS_ALP[newInd]
        if text[i] not in RUS_ALP:  # not change signs in text
            cryptoText += text[i]
    return cryptoText


def caesarDeCrypt(cryptoText, key):  # decrypt
    if key > 32:
        key %= 32
    deCryptoText = ''
    for i in range(len(cryptoText)):  # decrypting reverse algo
        if cryptoText[i] in RUS_ALP:
            if RUS_ALP.index(cryptoText[i]) - key < 0:
                newInd = len(RUS_ALP) + (RUS_ALP.index(cryptoText[i]) - key)
            else:
                newInd = RUS_ALP.index(cryptoText[i]) - key
            deCryptoText += RUS_ALP[newInd]
        if cryptoText[i] not in RUS_ALP:
            deCryptoText += cryptoText[i]
    return deCryptoText


def cipherGronsfeld(text, key):
    cryptoText = ''
    key = str(key)
    for i in range(len(text)):
        if text[i] not in RUS_ALP:
            cryptoText += text[i]
        else:
            realShift = int(key[i % len(key)])  # polyalphabet shift
            if RUS_ALP.index(text[i]) + realShift > len(RUS_ALP) - 1:
                newInd = RUS_ALP.index(text[i]) + realShift - len(RUS_ALP)
            else:
                newInd = RUS_ALP.index(text[i]) + realShift
            cryptoText += RUS_ALP[newInd]
    return cryptoText

def gronsfeldDeCrypt(cryptoText, key):
    deCryptoText = ''
    key = str(key)
    for i in range(len(cryptoText)):
        if cryptoText[i] not in RUS_ALP:
            deCryptoText += cryptoText[i]
        else:
            realShift = int(key[i % len(key)])
            if RUS_ALP.index(cryptoText[i]) - realShift < 0:
                newInd = len(RUS_ALP) + (RUS_ALP.index(cryptoText[i]) - realShift)
            else:
                newInd = RUS_ALP.index(cryptoText[i]) - realShift
            deCryptoText += RUS_ALP[newInd]
    return deCryptoText



s = 'встреча состоится у школы'
x = cipherGronsfeld(s, 123124)
print(x)
print(gronsfeldDeCrypt(x, 123124))
print('Скажите что это не шутка')
