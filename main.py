from caesarCryptograph import CaesarCryptograph
from gronsfeldCryptograph import GronsfeldCryptograph
from tritemiusCryptograph import TritemiusCryptographer

s = 'встреча состоится у школы'
x = CaesarCryptograph.encrypt(s, 3)
print(x)
print(CaesarCryptograph.decrypt(x, 3))
m = GronsfeldCryptograph.encrypt(s, 1213)
print(m)
print(GronsfeldCryptograph.decrypt(m, 1213))

x = TritemiusCryptographer.encrypt(s)
print(x)
print(TritemiusCryptographer.decrypt(x))
