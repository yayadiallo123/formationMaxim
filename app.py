class Taches:
    def __init__(self):
        self.taches= []
        self.terminer=[]
        
    
    def ajouter(self,tache):
        self.taches.append(tache)
        self.terminer.append(False)
       
        
    def afficher(self):
        print('-----------------------------------')
        for i,t in enumerate(self.taches):
            
            print(f'{i} , {t} -- {self.terminer[i]}' )
            
    def valide(self,id):
        if id >= 0 and id < len(self.taches):
            return True
          
        else:
            print("Erreur : indice hors limite")
            return False
            
        
    
    
         
    def terminerT(self,id):
        if self.valide(id):
            self.terminer[id] = True
        
    def supprimerT(self,idx):
        del self.taches[idx]
        del self.terminer[idx]
        
tache = Taches()
tache.afficher()


while True:
    cmd = input("Entrer une commande (+: Ajouter, -: Terminer, s: Supprimer, a: Afficher , q: Quitter) : ")
    print()
    if cmd == "+":
        taches= input("Entrer le nom de la tache : ")
        tache.ajouter(tache)
    elif cmd == "-":
        id=int(input("id de la Tache :"))
        print()
        tache.terminerT(id)
        
    elif cmd =="s":
        idx=int(input("id de la Tache a supprime : "))
        tache.supprimerT(idx)
    elif cmd == "a":
        tache.afficher()
        
    elif cmd == "q":
        break
    else:
        print("Commande invalide")
        

#tache.afficher()
# tache.ajouter("aller au cinema")
# tache.ajouter("aller au marcher")

# tache.afficher()
# tache.terminerT(1)
# tache.afficher()
# tache.supprimerT(1)
 
