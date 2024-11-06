class pere :
    nomMere ="Mère"
class mere:
    nomPere ="Père"
class enfant(mere, pere): # héritage multiple : ordre des classes mères est important
    pass
e1 = enfant()
print(f"Mère :{e1.nomMere} , Mère :{e1.nomPere}")
print(enfant.__mro__) # affiche l'ordre de recherche des classes (mro : method resolution order)


