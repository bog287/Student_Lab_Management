from UI.asignari_UI import Asignari_UI
from UI.printeaza import printMainMenu
from UI.probleme_UI import Probleme_UI
from UI.statistici import Statistici_UI
from UI.studenti_UI import Studenti_UI


class UI(object):
    def __init__(self, srv_stud, srv_probleme, srv_asign, srv_statistici):
        """
        Initializeaza clasa UI
        """
        self.__srv_stud = srv_stud
        self.__srv_probleme = srv_probleme
        self.__srv_asign = srv_asign
        self.__srv_statistici = srv_statistici


    def run(self):
        """
        Run menu
        """
        self.__srv_stud.adauga_stud_auto()
        self.__srv_probleme.adauga_probleme_auto()
        self.__srv_asign.generate()

        while True:
            printMainMenu()
            cmd = input("\n>>>Introduceti optiune dvs.: ")
            print()
            if cmd == "0":
                print("\n    Multumesc ca ai uitilizat aplicatia mea! Bye!\n")
                return
            elif cmd == "1":
                Studenti_UI(self.__srv_stud).show()
            elif cmd == "2":
                Probleme_UI(self.__srv_probleme).show()
            elif cmd == "3":
                Asignari_UI(self.__srv_asign).show()
            elif cmd == "4":
                Statistici_UI(self.__srv_stud, self.__srv_probleme, self.__srv_asign, self.__srv_statistici).show()
            else:
                print("\n...Comanda invalida!...\n")
