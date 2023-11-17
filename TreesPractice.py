
# =============================================================================
# creation d une arbre
# =============================================================================

a=[5,[3,[1,[],[]],[4,[],[]]],[2,[8,[],[]],[10,[],[]]]]


# Exo1 TD2

def vide(tree):
    if  len(tree)==0:
        return True 
    return False

print(vide(a))  

def Racine(tree) :
    if not vide(tree) :
        return tree[0]
    return None 

print('la racine de a est :',Racine(a))

def FilsGauche(a) :
    if not vide(a):
        return a[1]
    return None

print('fils gauche de l arbre a est :',FilsGauche(a))

def FilsDroite(a):
    if not vide(a):
        return a[2]
    return None

print('fils droite de l arbre a est ', FilsDroite(a))


# Premiere Methode 
def Prefix(tree):
    if not vide(tree) :
          print(tree[0], end=' , ')
          Prefix(FilsGauche(tree))
          Prefix(FilsDroite(tree))
          
# print('le parcours prefix de l arbre a est :',Prefix(a))



# deuxieme Methode 
def PPrefix(tree):
    if vide(tree):
        return []
    else:
        return [Racine(tree)]+[PPrefix(FilsGauche(tree))]+[PPrefix(FilsDroite(tree))]
          
print('le parcours prefix de l arbre a est :',PPrefix(a))


# Premiere Methode 
def Infixe(tree):
    if not vide(tree) :
          Infixe(FilsGauche(tree))
          print(tree[0], end=' , ')
          Infixe(FilsDroite(tree))
            
# print('le parcours Infixe de l arbre a est :',Infixe(a))

# deuxieme Methode 
def PInfixe(tree):
    if vide(tree):
        return []
    else:
        return [PInfixe(FilsGauche(tree))]+[Racine(tree)]+[PInfixe(FilsDroite(tree))]
          
print('le parcours infixe de l arbre a est :',PInfixe(a))


# Premiere Methode 
def Postfixe(tree):
    if not vide(tree) :
          Infixe(FilsGauche(tree))
          Infixe(FilsDroite(tree))
          print(tree[0] , end=' , ')
    
# print('le parcours Postfixe de l arbre a est :',Postfixe(a))


# deuxieme Methode 
def PPostfixe(tree):
    if vide(tree):
        return []
    else:
        return [PInfixe(FilsGauche(tree))]+[PInfixe(FilsDroite(tree))]+[Racine(tree)]
          
print('le parcours Postfixe de l arbre a est :',PPostfixe(a))


def nbrNoeud(a) :
    if vide(a):
        return 0
    return 1+nbrNoeud(FilsGauche(a))+nbrNoeud(FilsDroite(a))

print('nombre de noeud est ',nbrNoeud(a))



def estFeuille(a):
    if not vide(a):
        if vide(FilsGauche(a)) and vide(FilsDroite(a)):
            return True 
    return False

def NombreFeuille(tree):
    if vide(tree):
        return 0
    elif estFeuille(tree):
        return 1 
    else :
        return NombreFeuille(FilsGauche(tree))+NombreFeuille(FilsDroite(tree))
    
print('le nombre de feuille de l arbre a est :',NombreFeuille(a))




def estNoeudInterne(tree):
    if vide(tree) or estFeuille(tree):
        return False
    return True


def NombreNoeudInterne(tree) :
    return nbrNoeud(tree)-NombreFeuille(tree)

    
print('le nombre de noeud Interne est :',NombreNoeudInterne(a))


def exist(a,nbr):
    if vide(a):
        return False
    elif Racine(a)==nbr :
        return True
    return exist(FilsGauche(a),nbr) or exist(FilsDroite(a), nbr)

print('est ce que 5 exist dans l arbre', exist(a,5))


# Exo 2 Td2 


b = ['+',['*',[4,[],[]],[7,[],[]]],['-',['+',[3,[],[]],[1,[],[]]],[8,[],[]]]]

def calculer(a, b , c):
        if c=='+':
            return a+b
        elif c=='-':
            return a-b
        elif c=='*':
            return a*b
        
            
def Evaluer(a) :
    if vide(a):
        return None
    elif estFeuille(a):
        return Racine(a)
    else :
        return calculer(Evaluer(FilsGauche(a)),Evaluer(FilsDroite(a)),Racine(a))
    
print('la valeur de a est :',Evaluer(b))



#Exo3 Td2

b = [7,[5,[2,[],[]],[6,[],[]]],[18,[17,[],[]],[19,[],[]]]]

def existVal(a , val):
    if vide(a):
        return False
    if Racine(a) == val:
        return True
    if val<Racine(a):
        return existVal(FilsGauche(a), val)
    else:
        return existVal(FilsDroite(a), val)

print('est ce que la valeur 18 existe dans cette abr ',existVal(b, 18))   


def plusGrand(a) :
    if vide(a):
        return None
    elif vide(FilsDroite(a)):
        return Racine(a)
    else:
        return plusGrand(FilsDroite(a))
                
        
print('le plus grand element est', plusGrand(b))  

def plusPetit(a):
    if vide(a):
        return None
    elif vide(FilsGauche(a)):
        return Racine(a)
    else :
        return plusPetit(FilsGauche(a))

print('le plus petit element est :',plusPetit(b))


def inserer(a,val):
    if vide(a):
        a.extend([val,[],[]])
    elif val<Racine(a):
        return inserer(FilsGauche(a), val)   
    else:
        return inserer(FilsDroite(a),val)


print('inserer la valeur 2 :',inserer(b, 1))
print('la nouvelle abr b est :', b)


# Exo4 Td2


def Supression(a,val):
    if not vide(a) and existVal(a, val):
        if Racine(a)==val:
            if estFeuille(a):
                a.clear()
            else :
                if vide(FilsGauche(a)):
                    v=FilsDroite(a)
                    a[:] = v
                elif vide(FilsDroite(a)):
                    v = FilsGauche(a)
                    a[:]=v
                else :
                    m = plusGrand(FilsGauche(a))
                    print('m =',m)
                    a[0] = m
                    Supression(FilsGauche(a),m)
        elif Racine(a) > val:
            Supression(FilsGauche(a), val)
        else :
            Supression(FilsDroite(a), val)
    else :
        return None        

d = [7,[5,[2,[],[]],[6,[],[]]],[18,[17,[],[]],[19,[],[]]]]

print("Suppression de la valeur 2 ",Supression(d, 7))
print('la nouvelle c est : ',d)




























