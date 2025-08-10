# импорт библиотек и переменных

import random

from config import acp, ocp

# генератор паролей для админки
achars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(1):
    anickpass = ''
    for i in range(acp):
        anickpass += random.choice(achars)

# генератор паролей для создателя
ochars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#%*$&?!@'
for n in range(1):
    onickpass = ''
    for i in range(ocp):
        onickpass += random.choice(ochars)