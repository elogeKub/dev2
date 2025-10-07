import math
# Q1
def patinage(epaisseur_glace, temperature_moyen):
    ''' cette fonction determine si canal Rideaux est ouvert
    pour le patinage '''
    entrain_de_teste=False
    if(epaisseur_glace>=30 and temperature_moyen<=-10):
       entrain_de_teste=True
    else:
       entrain_de_teste=False
    return  entrain_de_teste     

#-----------------------------------------------------------------


#Q2

def  alphaNote(note_final):
    '''contrat type: (int)->str'''
    if note_final >= 90:
        return "A+"
    elif note_final >= 85:
        return "A"
    elif note_final >= 80:
        return "A-"
    elif note_final >= 75:
        return "B+"
    elif note_final >= 70:
        return "B"
    elif note_final >= 65:
        return "C+"
    elif note_final >= 60:
        return "C"
    elif note_final >= 55:
        return "D+"
    elif note_final >= 50:
        return "D"
    elif note_final >= 40:
        return "E"
    else:
        return "F"
#-----------------------------------------------------------------

# Q3
def alphaNoteVerif():
     note_final = float(input("Entrez la note finale (0 à 100) : "))
     while note_final < 0 or note_final > 100:
           note_final = float(input("Entrer une note valide : "))
     correspo= alphaNote(note_final)  
     print(f"La note alphabetique est: {correspo}")

     if correspo in ("E","F"):
        print("Echoué")
     else:
        print("Réussi")
   


#-----------------------------------------------------------------------------
#Q4
def boucles(n):
    ''' Contrat type : (int) -> None'''
    for i in range(1, n, 2):
        print(i, end=" ")
    
    print()
    if n % 2 == 0:
        var_to_start = n - 1
    else:
        var_to_start = n
    
    for i in range(var_to_start, 0, -2):
        print(i, end=" ")


#------------------------------------------------------------------------

#Q5

def facteursDeN(n):
    '''contrat type:(int)->bool'''
    somme = 0
    print(f"Facteurs de {n} = ", end=" ")
    for i in range(2, n):
        if n % i == 0:
            print(i, end=" ")
            somme += i
    print() 
    print(f"Somme des Facteurs={somme}", )
    
    return somme < n
#-----------------------------------------------------------------


#exo Q6
def carreParfait(n):
  '''contrat du type: (int)->bool'''
  if n<0:
    print(f"Le nombre {n} n'est pas un carée parfaim")
  racine=int(math.sqrt(n))  
  if  racine*racine==n:
      print(f"{n} est un carré parfait et sa racine carrée est {racine}.")
      return True

  else:
      print(f"{n} n’est pas un carré parfait.")
      return False
    
#-----------------------------------------------------------------


#ex Q7
def maFun(n):
    res = (-1)**n / (2*n + 1)
    return res

#-----------------------------------------------------------------

 #ex Q8
def maFun_bis(n):
    somme = 0
    for i in range(n + 1):
        somme += maFun(i)
    
    resu = 4 * somme
    return resu