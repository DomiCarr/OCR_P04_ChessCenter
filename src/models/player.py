""" Player """


class Player:
    def __init__(self, national_id, first_name, last_name, birth_date):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def to_dict(self):
        return self.__dict__





"""
objet players:

classe qui gere la logique de la sauvegarde avec plusieurs methodes
metgodes qui :
gestion des players
- recupere le fichioer txt dans un tableau d'iobjects players
- enregistre le fichier txt a partir du tableau objects players

pour les tournois
- recuperer un joueur dans le txt et
- modifier un joueur
- ajouter un joueur (doit verifier au existe pas deja

+ faire CLI

"""
