from Domeniu.student_entitati import Student
from copy import deepcopy
import random
import string


class ServiceStudenti(object):
    def __init__(self, repo, valid):
        """
        Initializeaza clasa ServiceStudenti
        :param: repo - RepositoryStudenti
        :param: valid - Validare_Student
        """

        self.__repo = repo
        self.__valid = valid

    def adauga_student(self, studID, nume, grup):
        """
        adauga un student
        :param: studID - nr natural pozitiv ( identificator unic al unui student)
        :param: nume - string
        :param: grup - int
        """
        student = Student(studID, nume, grup)
        self.__valid.valideaza(student)
        self.__repo.adauga(student)

    def get_studenti(self):
        """
        Obtine lista de studenti
        :return: list (lista de studenti)
        """
        return self.__repo.get_all()

    def numar_studenti(self):
        """
        Obtine numarul de studenti
        :return: integer (numarul de studenti)
        """
        return self.__repo.size()

    def adauga_stud_auto(self):
        """
        adauga studenti in repository
        """
        studenti = [0] * 6
        studenti[0] = Student(1, "Alina", 222)
        studenti[1] = Student(2, "Maria", 224)
        studenti[2] = Student(3, "Larisa", 226)
        studenti[3] = Student(4, "Daniel", 224)
        studenti[4] = Student(5, "Raluca", 223)
        studenti[5] = Student(6, "Alina", 228)

        for i in range(len(studenti)):
            self.__valid.valideaza(studenti[i])
            self.__repo.adauga(studenti[i])

    def generate(self, nr):
        """
        Genereaza automat nr studenti si ii adauga in repository
        :param: nr - numar natural
        :exception: Exception - in caul in care persoana generata este invalida
        """
        while nr > 0:
            studID = random.randrange(1, 100)
            nume = str("".join(random.choices(string.ascii_uppercase, k=7)))
            grup = random.randrange(1, 300)
            student = Student(studID, nume, grup)
            try:
                self.__valid.valideaza(student)
                self.__repo.adauga(student)
                nr = nr - 1
            except Exception:
                pass

    def gaseste_stud_by_ID(self, studID):
        """
        Gaseste un student dupa ID
        :param: studID - numar natural ( identificator unic al unui student)
        :return: Student (obiectul student cu ID-ul cautat)
        """
        key_student = Student(studID, None, None)
        return self.__repo.cauta(key_student)

    def modifica_stud(self, studID, nume, grup):
        """
        modifica numele si adresa unui student existent (dupa ID)
        :param: studID - numar natural ( identificator unic al unui student)
        :param: nume - string
        :param: grup - string
        """
        student_nou = Student(studID, nume, grup)
        self.__valid.valideaza(student_nou)
        self.__repo.modifica(student_nou)


    def sterge_stud(self, studID):
        """
        sterge un student dupa ID
        :param: studID - numar natural ( identificator unic al unei persoane)
        """
        key_persoana = Student(studID, None, None)
        self.__repo.sterge(key_persoana)






    def numar_studenti_clona(self):
        """
        Obtine numarul de liste clonate din clona
        :return: integer (numarul de liste clonate)
        """
        return self.__repo.size_clona()

    def adauga_clona_student(self):
        """
        adauga  o clona a listei de studenti
        """
        lista_stud = deepcopy(self.__repo.get_all())
        self.__repo.adauga_clona(lista_stud)





