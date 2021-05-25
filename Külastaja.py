from kodutoo.Raamat import raamat


class külastaja:
    def __init__(self, eesNimi, perekonnaNimi):
        self.nimi = eesNimi
        self.perenimi = perekonnaNimi
        self.laenuraamatud = [] #Tühi list

    def laenutaRaamat(self, laenutavRaamat):
        self.laenuraamatud.append(laenutavRaamat)

    def tagastaRaamat(self, tagastavraamat):
        self.laenuraamatud.remove(tagastavraamat)

    def kuvaLaenutatudRaamatud(self):
        for laenuraamatud in self.laenuraamatud:
            print(laenuraamatud.pealkiri)


raamat1 = raamat("mingi pealkiri", "mingi autor", 350)
raamat2 = raamat("mingi pealkiri2", "mingi autor2", 350)
külastaja1 = külastaja("Joosep", "joosepson")

külastaja1.laenutaRaamat(raamat1)
külastaja1.kuvaLaenutatudRaamatud()
print()
külastaja1.laenutaRaamat(raamat2)
külastaja1.kuvaLaenutatudRaamatud()