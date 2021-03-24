from Domeniu.problema_entitati import Problema
from Validare.problema_validare import *
from copy import deepcopy
import random
import string


class ServiceProbleme(object):
    def __init__(self, repo, valid):
        """
        Initializeaza clasa ServiceProbleme
        :param: repo - RepositoryProbleme
        :param: valid - Validare_Probleme
        """
        self.__repo = repo
        self.__valid = valid

    def adauga_problema(self, nrLab_nrPb, desc, deadline):
        """
        adauga o problema
        :param: nrLab_nrPb - string
        :param: desc - string
        :param: deadline - int > 0
        """
        problema = Problema(nrLab_nrPb, desc, deadline)
        self.__valid.valideaza(problema)
        self.__repo.adauga(problema)

    def numar_probleme(self):
        """
        Obtine numarul de probleme
        :return: integer numarul de probleme
        """
        return self.__repo.size()

    def get_probleme(self):
        """
        Obtine lista de probleme
        :return: list
        """
        return self.__repo.get_all()

    def gaseste_pb_by_nrPb(self, nrLab_nrPb):
        """
        Gaseste o problema dupa nrLab_nrPb
        :param: nrLab_nrPb - string ( identificator unic al unei probleme)
        :return: Problema (obiectul problema cu datele cautate)
        """
        key_pb = Problema(nrLab_nrPb, None, None)
        return self.__repo.cauta(key_pb)

    def modifica_pb(self, nrLab_nrPb, desc, deadline):
        """
        modifica descrierea si deadline-ul unei pb existente (dupa nrLab_nrPb)
        :param: nrLab_nrPb - string ( identificator unic al unui eveniment)
        :param: description - string
        :param: deadline - int
        """
        pb_noua = Problema(nrLab_nrPb, desc, deadline)
        self.__valid.valideaza(pb_noua)
        self.__repo.modifica(pb_noua)

    def sterge_probleme(self, nrLab_nrPb):
        """
        sterge o pb dupa nrLab_nrPb
        :param: nrLab_nrPb - string ( identificator unic al unei pb)
        """
        key_pb = Problema(nrLab_nrPb, None, None)
        self.__repo.sterge(key_pb)


    def generate(self, nr):
        """
        Genereaza automat nr probleme si le adauga in repository
        :param: nr - numar natural
        :exception: Exception - in cazul in care problema generata este invalida
        """
        while nr > 0:
            nrLab_nrPb = random.randrange(1, 10)
            desc = str("".join(random.choices(string.ascii_uppercase, k=14)))
            deadline = random.randrange(nrLab_nrPb + 1, 20)
            problema = Problema(nrLab_nrPb, desc, deadline)
            try:
                self.__valid.valideaza(problema)
                self.__repo.adauga(problema)
                nr = nr - 1
            except Exception:
                pass

    def adauga_probleme_auto(self):
        """
        adauga probleme in repository
        """
        probleme = [0] * 10
        probleme[0] = Problema("12_2", "misterioasa", 15)
        probleme[1] = Problema("12_3", "misterioasa", 15)
        probleme[2] = Problema("12_4", "misterioasa", 18)
        probleme[3] = Problema("12_5", "misterioasa", 15)
        probleme[4] = Problema("12_6", "misterioasa", 15)
        probleme[5] = Problema("11_2", "misterioasa", 15)
        probleme[6] = Problema("8_2", "misterioasa", 15)
        probleme[7] = Problema("7_1", "misterioasa", 15)
        probleme[8] = Problema("3_8", "de groaza", 7)
        probleme[9] = Problema("10_1", "foarte grea", 12)

        for i in range(len(probleme)):
            self.__valid.valideaza(probleme[i])
            self.__repo.adauga(probleme[i])

    def numar_events_clona(self):
        """
        Obtine numarul de liste clonate din clona
        :return: integer (numarul de liste clonate)
        """
        return self.__repo.size_clona()

    def adauga_clona_problema(self):
        """
        adauga  o clona a listei de probleme
        """
        lista_probleme = deepcopy(self.__repo.get_all())
        self.__repo.adauga_clona(lista_probleme)

    def undo(self):
        """
        Reface ultima actiune
        """
        return self.__repo.get_clona()
