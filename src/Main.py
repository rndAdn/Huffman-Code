'''
Liste de regex utile
    ÉÈéèêë      -> e
    ÀàÂâÄä      -> a
    ÙùüÜÛû      -> u
    ÌÍÎÏìíîï    -> i
    òóôõöÒÓÔÕÖ  -> o
    çÇ          -> c

'''
from pip.util import egg_link_path

DicoBinaire = dict()

class Noeud:
    '''
    Dans cette classe les mots Feuille et Arbre corresponde au meme objet la distinction est :
    Une Feuille n'a ni gauche ni droit  mais elle possède un char avec sa frequence
    Un  Arbre n'a pas de char et sa freq correspond a la frequence des char ces sous Arbres/Feuille


    '''


    def __init__(self, freq,gauche=None,droit=None, char=None):
        self.freq = freq
        self.gauche=gauche
        self.droit = droit
        self.char = char


    def ArbreToDict(self, ch):
        if self.char:
            DicoBinaire[self.char] = ch
            return

        self.gauche.ArbreToDict(ch+"0")
        self.droit.ArbreToDict(ch + "1")

    def __repr__(self):

        if self.char:
            return "{0} char:{1} g:{2} d:{3}  ".format(self.freq,self.char, self.gauche, self.droit)
        else:
            return "{0} char:{1} g:{2} d:{3}  ".format(self.freq, self.char, self.gauche, self.droit)


def freqToArbre(freqTableau):
    '''
    Cette Fonction est la fonction pricipale de la transformation d'un tableau de frequence
    en un arbre binaire
    Elle va dabord tranformer le tableau de frequence en tableau de feuille TRIÉE
    Puis appeler sa fonction recusive toArbreRec
    La frequence est un tuple ('c', 0)
    '''

    Feuilles = []
    for tup in freqTableau:
        Feuilles += [Noeud(tup[1],char=tup[0])]
    return toArbreRec(Feuilles)


def toArbreRec(freqFeuille):
    '''
    Tant que le tableau a plus de deux éléments on retire les deux Feuille/Arbre avec les plus petites frequences
    Puis on tranforme ces Feuille/Arbre en un autre Arbre (la plus petite frequence dès deux se trouve a gauche)
    Le nouvel Arbre est ensuite rajouté au tableau classé
    '''
    if len(freqFeuille) > 1:
        n1 = freqFeuille[0]
        n2 = freqFeuille[1]
        ar = Noeud(n1.freq+n2.freq, gauche=n1, droit=n2)
        freqFeuille = freqFeuille[2:]
        for i,elt in enumerate(freqFeuille):
            if ar.freq < elt.freq:
                freqFeuille = freqFeuille[:i]+[ar]+freqFeuille[i:]

                return toArbreRec(freqFeuille)
        freqFeuille  += [ar]
        return toArbreRec(freqFeuille)
    return freqFeuille[0]

def txtToFreq(txt):
    '''
    On cree un dictionnaire de lettre:occurence
    Ensuite on parcours le texte en remplissant le dictionnaire et on le renvoi

    '''
    dico = dict()

    for lettre in txt:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1

    return list(dico.items())

def encode(txt):
    '''

    '''
    # txttofreq
    # freqToArbre
    # ArbreToDict

    freqTab = txtToFreq(txt)
    freqTab.sort(key=lambda x: x[1])
    print("freqTab :\n"+str(freqTab)+"\n")
    arbre = freqToArbre(freqTab)
    arbre.ArbreToDict("")

    txt_encode = ""
    print("DicoBinaire :\n" + str(DicoBinaire)+"\n")
    for c in txt:
        txt_encode += DicoBinaire[c]

    return txt_encode


def decode(txt):
    '''

    '''
    Dico = dict(zip(DicoBinaire.values(), DicoBinaire.keys()))
    txt_decode = ""
    tmp = ""

    for bit in txt:
        tmp += bit
        if tmp in Dico:
            txt_decode += Dico[tmp]
            tmp = ""

    return txt_decode


txt = "Cette série relate les aventures du Docteur, un extraterrestre de la race des Seigneurs du Temps (Time Lords) originaire de la planète Gallifrey et qui voyage à bord d'un TARDIS (Time And Relative Dimension In Space, ou Temps À Relativité Dimensionnelle Inter Spatiale4 en français), une machine pouvant voyager dans l'espace et dans le temps. Particulièrement attaché à la Terre, il est régulièrement accompagné dans ses voyages par des compagnons, pour la plupart humains et féminins."

print("texte :\n"+txt+"\n")
encode = encode(txt)
print("encode :\n"+encode+"\n")
decode = decode(encode)



print("decode :\n"+decode)

print("egal ?  "+str(txt==decode))