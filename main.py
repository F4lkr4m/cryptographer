from caesarCryptograph import CaesarCryptograph

s = 'встреча состоится у школы'
x = CaesarCryptograph.encrypt(s, 3)
print(x)
print(CaesarCryptograph.decrypt(x, 3))