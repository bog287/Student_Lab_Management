from UI.printeaza import printAsignariMenu
from Erori.exceptii import ValidError, RepoError


class Asignari_UI(object):

    def __init__(self, srv_asign):
        """
        Initializeaza clasa Asign_UI si creaza comenzile
        """
        self.__srv_asign = srv_asign
        self.__comenzi = {"1": self.__ui_asign,
                          "2": self.__ui_print_asign,
                          }

    def __ui_asign(self):
        """
        Adauga o asignare
        """
        asignare_ID = int(input(">>>Introduceti ID-ul asignarii: "))
        stud_ID = int(input(">>>Introduceti ID-ul studentului: "))
        nrLab_nrPb = (input(">>>Introduceti ID-ul problemei: "))
        nota = int(input(">>>Introduceti nota: "))
        print()
        self.__srv_asign.adauga_asignare(asignare_ID, stud_ID, nrLab_nrPb, nota)
        print("...Asignare realizata cu succes!...\n")

    def __ui_print_asign(self):
        """
        Afiseaza toate asignarile
        """
        print("________________________________________________________")
        if self.__srv_asign.numar_asignare() == 0:
            print("...Nu exista asignari in lista!...")
        else:
            asign = self.__srv_asign.get_asignare()
            print("ID asignare".center(14) + "ID student".center(14) + "nrLab_nrPb".center(14) + "nota".rjust(8))
            for sgn in asign:
                print(sgn)
        print("________________________________________________________")

    def show(self):
        """
        Show menu
        """
        while True:
            printAsignariMenu()
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

