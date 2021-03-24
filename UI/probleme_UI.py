from UI.printeaza import printProblemeMenu
from Erori.exceptii import ValidError, RepoError


class Probleme_UI(object):
    def __init__(self, srv_probleme):
        """
        Initializeaza clasa Probleme_UI si creaza comenzile
        """
        self.__srv_probleme = srv_probleme
        self.__comenzi = {"1": self.__ui_adauga_problema,
                          "2": self.__ui_print_problema,
                          "3": self.__ui_modifica_problema,
                          "4": self.__ui_gaseste_pb_by_nrLab_nrPb,
                          "5": self.__ui_sterge_problema,
                          "6": self.__ui_generate
                          }

    def __ui_adauga_problema(self):
        """
        Adauga o problema
        """
        nrLab_nrPb = int(input(">>>Introduceti nrLab_nrPb: "))
        desc = input(">>>Introduceti descrierea: ")
        deadline = input(">>>Introduceti deadline-ul: ")
        print()
        self.__srv_probleme.adauga_problema(nrLab_nrPb, desc, deadline)
        print("...Adaugare realizata cu succes!...\n")

    def __ui_print_problema(self):
        """
        Afiseaza toate problemele
        """
        if self.__srv_probleme.numar_probleme() == 0:
            print("Nu exista evenimente in lista!\n")
        else:
            probleme = self.__srv_probleme.get_probleme()
            print("    Lista problemelor este: ")
            for problema in probleme:
                print(problema)

    def __ui_gaseste_pb_by_nrLab_nrPb(self):
        """
        Gaseste o problema dupa nrLab_nrPb
        """
        id = (input(">>>Introduceti nrLab_nrPb: "))
        print()
        try:
            print("    Problema cautata, cu nrLab_nrPb-ul {} este:\n".format(id), self.__srv_probleme.gaseste_pb_by_nrPb(id))
        except RepoError as re:
            print(re)

    def __ui_modifica_problema(self):
        """
        Modifica o pb
        """
        nrLab_nrPb = input(">>>Introduceti nrLab_nrPb-ul: ")
        desc = input(">>>Introduceti o noua descriere: ")
        deadline = int(input(">>>Introduceti un nou deadline: "))
        print()
        try:
            self.__srv_probleme.modifica_pb(nrLab_nrPb, desc, deadline)
            print("...Modificare realizata cu succes!...\n")
        except ValidError as ve:
            print(ve)


    def __ui_sterge_problema(self):
        """
        Sterge o problema
        """
        id = (input(">>>Introduceti nrLab_nrPb: "))
        print()
        try:
            self.__srv_probleme.sterge_probleme(id)
            print("    Problema stearsa cu succes!\n")
        except RepoError as re:
            print(re)

    def __ui_generate(self):
        """
        Genereaza automat x entitati
        """
        try:
            nr = int(input(">>>Numarul de entitati: "))
            if nr < 0:
                print("\n...Numarul trebuie sa fie pozitiv!...\n")
                return
            else:
                self.__srv_probleme.generate(nr)
        except ValueError:
            print("\...Numarul trebuie sa fie un numar natural!...\n")

    def show(self):
        """
        Show menu
        """
        while True:
            printProblemeMenu()
            cmd = input("\n>>>Introduceti optiunea dvs.: ")
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
