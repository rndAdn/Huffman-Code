'''
Liste de regex utile
    ÉÈéèêë      -> e
    ÀàÂâÄä      -> a
    ÙùüÜÛû      -> u
    ÌÍÎÏìíîï    -> i
    òóôõöÒÓÔÕÖ  -> o
    çÇ          -> c

'''



class Noeud:
    '''
    Dans cette classe les mots Feuille et Arbre corresponde au meme objet la distinction est :
    Une Feuille n'a ni gauche ni droit  mais elle possède un char avec sa frequence
    Un  Arbre n'a pas de char et sa freq correspond a la frequence des char ces sous Arbres/Feuille


    '''
    DicoBinaire = dict()

    def __init__(self, freq,gauche=None,droit=None, char=""):
        self.freq = freq
        self.gauche=gauche
        self.droit = droit
        self.char = char


    def ArbreToDict(self, ch):
        if self.char:
            DicoBinaire[self.char] = ch
            return

        self.gauche.ArbreToDict(ch+"0")
        self.gauche.ArbreToDict(ch + "1")




def toArbre(freqTableau):
    '''
    Cette Fonction est la fonction pricipale de la transformation d'un tableau de frequence
    en un arbre binaire
    Elle va dabord tranformer le tableau de frequence en tableau de feuille TRIÉE
    Puis appeler sa fonction recusive toArbreRec
    '''
    pass

def toArbreRec(freqFeuille):
    '''
    Tant que le tableau a plus de deux éléments on retire les deux Feuille/Arbre avec les plus petites frequences
    Puis on tranforme ces Feuille/Arbre en un autre Arbre (la plus petite frequence dès deux se trouve a gauche)
    Le nouvel Arbre est ensuite rajouté au tableau classé
    '''
    pass

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

    return dico


