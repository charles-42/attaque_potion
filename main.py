import random as rd
notre_score  = 50
score_ennemi = 50
nb_potion = 0
    
def on_attaque_potion(choix,x,y):
    if choix=="attaque":
        y -= rd.randint(5,10)
        print("le score de l'ennemi est", y)
        return y
    if choix=="potion":
        x += rd.randint(15,50)
        print("notre score apres une potion est", x)
        return x
    return False


termin=False
while not termin:
    print(notre_score,score_ennemi)
    choix = input("entrer attaque ou potion : ")
    
    if choix=="attaque":
        score_ennemi=on_attaque_potion(choix,notre_score,score_ennemi)
    elif choix=="potion":
        nb_potion +=1
        if nb_potion <=3:
            notre_score=on_attaque_potion(choix,notre_score,score_ennemi)
            print("nombre de potion",nb_potion)
        else:
            print("on a utilisé toutes les potions")
            choix = input("entrer juste attaque: ")
            while choix != "attaque":
                choix = input("entrer SVP juste attaque: ")   
            score_ennemi=on_attaque_potion(choix,notre_score,score_ennemi)       
    else:
        print("SVP entrer un choix valide")
    
    print(notre_score,score_ennemi)
    if score_ennemi <=0:
        termin=True
        print("l'ennemi est mort")
    else:
        notre_score -= rd.randint(5,15)
        print("notre score apres l'attaque de l'ennemi est",notre_score)
    if notre_score <=0:
        termin=True
        print("On est mort")
        








# def calculer_score_ennemi():
#     pass

# def ennemi_attaque():
#     pass
