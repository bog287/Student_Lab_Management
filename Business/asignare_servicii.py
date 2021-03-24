import random

from Domeniu.asignare_entitati import Asignare
from Domeniu.problema_entitati import Problema
from Domeniu.student_entitati import Student


class ServiceAsignare(object):
    def __init__(self, repo_asign, repo_stud, repo_prob, valid):
        """
        Initializeaza clasa ServiceSignUp
        :param: repo_signUp - RepositorySignUp
        :param: repo_pers - RepositoryStudenti
        :param: repo_events - RepositoryProbleme
        :param: valid - Validare_Asignare
        """
        self.__repo_asign = repo_asign
        self.__repo_stud = repo_stud
        self.__repo_prob = repo_prob
        self.__valid = valid

    def adauga_asignare(self, asign_ID, stud_ID, nrLab_nrPb, nota):
        """
        adauga o asignare
        :param asign_ID: numar natural (identificatorul unic al unei asignari)
        :param stud_ID: numar natural (identificatorul unic al unui student)
        :param nrLab_nrPb: string (identificatorul unic al unei probleme)
        :param nota: numar natural(>0 si <10)
        """
        asign = Asignare(asign_ID, stud_ID, nrLab_nrPb, nota)
        self.__valid.valideaza(asign)
        key_student = Student(stud_ID, None, None)
        self.__repo_stud.cauta(key_student)
        key_prob = Problema(nrLab_nrPb, None, None)
        self.__repo_prob.cauta(key_prob)
        self.__repo_asign.adauga(asign)


    def numar_asignare(self):
        """
        Obtine numarul de asignari
        :return: integer (numarul de asignari)
        """
        return self.__repo_asign.size()


    def get_asignare(self):
        """
        Obtine lista de asignari
        :return: list (lista de asignari)
        """
        return self.__repo_asign.get_all()

    def generate(self):
        """
        Genereaza automat nr studenti si ii adauga in repository
        :param: nr - numar natural
        :exception: Exception - in caul in care persoana generata este invalida
        """
        nr = 20
        while nr > 0:
            asign_ID = random.randrange(1, 100)
            stud_ID = random.randrange(1, 100)
            nrLab = random.randrange(1, 100)
            nrPb = random.randrange(1, 100)
            nrLab_nrPb = str(nrLab) + "_" + str(nrPb)
            nota = random.randrange(1,10)
            asign = Asignare(asign_ID, stud_ID, nrLab_nrPb, nota)
            try:
                self.__valid.valideaza(asign)
                key_persoana = Student(stud_ID, None, None)
                self.__repo_stud.cauta(key_persoana)
                key_prob = Problema(nrLab_nrPb, None, None)
                self.__repo_prob.cauta(key_prob)
                self.__repo_asign.adauga(asign)
                nr = nr - 1
            except Exception:
                pass


