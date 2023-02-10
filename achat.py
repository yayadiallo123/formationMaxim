

class Achats:
    def __init__(self):
        self.produits = {}
        
        
    def ajouter(self,produit,prix):
        self.produits[produit]=prix
        
    def supprimer(self,produit):
        if produit in self.produits:
            del self.produits[produit]
        else:
            print(" Erreur : produit invalide : ")
            
                 
    def afficher(self):
        print("------------------------")
        for i, p in enumerate(self.produits):
            print(f"{i} : {p} -- {self.produits[p]}  euros")
            
    def prix_total(self):
        total =0
        # for p in self.produits:
        #     total += self.produits[p]
        for p,v in self.produits.items():
            total +=  v
        print("Le prix total est : ", total)


achats = Achats()
achats.ajouter("banane",12)
achats.ajouter("oueuf",10)
achats.ajouter("salade",4)
while True:
    
    cmd = input("Commandes (+: Ajouter , s: Supprimer , t:Afficher le prix total , a:Afficher, q:Quitter)")
    if cmd == "+":
        produit = input("Entrer le produit : ")
        prix =  float(input(" Entrer le prix : "))
        achats.ajouter(produit,prix)
        
    elif cmd =="s":
        produit = input("Entrer le produit : ")
        achats.supprimer(produit)
        print("Produit supprime avec succes ", produit)
        
        
    elif cmd == "t":
        achats.prix_total()
        
    elif cmd == "a":
        achats.afficher()
        
    elif cmd == "q":
        break
    else:
        print("Commande non valide: ")

# 
# achats.afficher()
# achats.prix_total()
# # achats.supprimer("banane")
# achats.afficher()

    