from copy import copy

def list_to_string(lista):
    s = "[" + lista[0]
    for j in range(1,len(lista)):
        s += "," + str(lista[j])
    s += "]"
    return s

class Automat:
    def __init__(self):
        self.stari = []
        self.stareinitiala = None
        self.starifinale = []
        self.tranzitii = {}

    def read(self):
        f = open("date.txt",'r')
        self.stari = f.readline().split()
        self.stareinitiala = f.readline().replace("\n","")
        self.starifinale = f.readline().split()
        for i in self.stari:
            self.tranzitii[i] = {}
        x = f.readline()
        while x:
            x = x.split()
            if x[1] not in self.tranzitii[x[0]].keys():
                self.tranzitii[x[0]][x[1]]=[]
            self.tranzitii[x[0]][x[1]].append(x[2])
            x = f.readline()

    def convert(self):
        stari = copy(self.stari)
        stareinitiala = copy(self.stareinitiala)
        starifinale = copy(self.starifinale)
        tranzitii = copy(self.tranzitii)
        t=[]
        for i in tranzitii.values():
            for j in i.keys():
                if j not in t:
                    t.append(j)
        self.stari = []
        self.starifinale = []
        self.stareinitiala = list_to_string([stari[0]])
        self.stari.append([stari[0]])
        self.tranzitii = {}
        for i1 in self.stari:
            for i2 in t:
                curent = []
                for i3 in i1:
                    if i2 in tranzitii[i3].keys():
                        for i4 in tranzitii[i3][i2]:
                            if i4 not in curent:
                                curent.append(i4)
                if len(curent) > 0:
                    curent.sort()
                    if curent not in self.stari:
                        self.stari.append(curent)
                    a = list_to_string(i1)
                    b = list_to_string(curent)
                    for j in starifinale:
                        if j in curent and b not in self.starifinale:
                            self.starifinale.append(b)
                    if a not in self.tranzitii.keys():
                        self.tranzitii[a] = {}
                    self.tranzitii[a][i2] = b


        print(self.stari,self.stareinitiala,self.starifinale,self.tranzitii,t,sep="\n")
        print()
        print(self.stari)
        print(self.stareinitiala)

    def verificare(self, cuvant):
        i = 0
        ok = 1
        j = self.stareinitiala

        while ok and i < len(cuvant):
            if cuvant[i] in self.tranzitii[j].keys():
                j = self.tranzitii[j][cuvant[i]]
                i += 1
            else:
                if j not in self.starifinale or i != len(cuvant):
                    ok = 0

        if j not in self.starifinale:
            ok = 0

        if ok == 1:
            return 'Cuvant acceptat'
        elif j not in self.starifinale:
            return 'Cuvant respins - starea in care s-a oprit nu este finala'
        else:
            return 'Cuvant respins - drum inexistent'

a = Automat()
a.read()
print(a.tranzitii)
print()
a.convert()
print(a.verificare(''))
with open("cuvant.txt") as g:
    x = g.readline().replace("\n","")
    while x:
        print(x,a.verificare(x),sep = "-")
        x = g.readline().replace("\n","")
