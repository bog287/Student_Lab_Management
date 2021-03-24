from UI.printeaza import printStudMenu
from Erori.exceptii import ValidError, RepoError


class Studenti_UI(object):

    def __init__(self, srv_stud):
        """
        Initializeaza clasa Studenti_UI si creaza comenzile
        """
        self.__srv_stud = srv_stud
        self.__comenzi = {"1": self.__ui_adauga_student,
                          "2": self.__ui_print_student,
                          "3": self.__ui_modifica_student,
                          "4": self.__ui_gaseste_stud_by_ID,
                          "5": self.__ui_sterge_student,
                          "6": self.__ui_generate,
                          }

    def __ui_adauga_student(self):
        """
        Adauga un student
        """
        studID = int(input(">>>Introduceti ID: "))
        nume = input(">>>Introduceti nume: ")
        grup = input(">>>Introduceti grup: ")
        print()
        self.__srv_stud.adauga_student(studID, nume, grup)
        print("...Adaugare realizata cu succes!...\n")

    def __ui_print_student(self):
        """
        Afiseaza toti studentii
        """
        if self.__srv_stud.numar_studenti() == 0:
            print("Nu exista studenti in lista!\n")
        else:
            studenti = self.__srv_stud.get_studenti()
            print("    Lista studentilor este: ")
            for student in studenti:
                print(student)

    def __ui_gaseste_stud_by_ID(self):
        """
        Gaseste student dupa ID
        """
        id = int(input(">>>Introduceti ID-ul: "))
        print()
        try:
            print("    Studentul cautat, cu ID-ul {} este:\n".format(id), self.__srv_stud.gaseste_stud_by_ID(id))
        except RepoError as re:
            print(re)

    def __ui_modifica_student(self):
        """
        Modifica un student
        """
        studID = int(input(">>>Introduceti ID-ul: "))
        nume = input(">>>Introduceti numele nou: ")
        grup = input(">>>Introduceti grup nou: ")
        print()
        try:
            self.__srv_stud.modifica_stud(studID, nume, grup)
            print("...Modificare realizata cu succes!...\n")
        except ValidError as ve:
            print(ve)

    def __ui_generate(self):
        """
        Genereaza automat x entitati pentru Student
        """
        self.__srv_stud.adauga_clona_student()
        try:
            nr = int(input(">>>Numarul de entitati: "))
            if nr < 0:
                print("\n...Numarul trebuie sa fie pozitiv!...\n")
                return
            else:
                self.__srv_stud.generate(nr)
        except ValueError:
            print("\...Numarul trebuie sa fie un numar natural!...\n")

    def __ui_sterge_student(self):
        """
        Sterge un student
        """
        id = int(input(">>>Introduceti ID-ul: "))
        print()
        try:
            self.__srv_stud.sterge_stud(id)
            print("...Student stearsa cu succes!...\n")
        except RepoError as re:
            print(re)

    def show(self):
        """
        Show menu
        """
        while True:
            printStudMenu()
            cmd = input("\n>>>Introduceti optiune dvs.: ")
            print()
            if cmd == "0":
                break
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError:
                    print("\n...Valoare numerica invalida!...\n")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            else:
                print("...Comanda invalida!...\n")
