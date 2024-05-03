class Jelek:
    def __init__(self, ora, perc, masodperc, x, y):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.x = x
        self.y = y

def eltelt():
    mbpe = sor[0]*360 + sor[1]*60 + sor[2]

lista = []
f = open('jel.txt', 'rt', encoding='utf-8')
for sor in f:
    sor = sor.strip().split(' ')
    lista.append(Jelek(sor[0], sor[1], sor[2], sor[3], sor[4]))
f.close()

print('2. feladat: ')
sorszam = int(input('Adja meg a jel sorszámát: '))
