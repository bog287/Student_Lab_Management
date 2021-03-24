from Erori.exceptii import ValidError, RepoError
from UI.printeaza import printStatisticiMenu


class Statistici_UI(object):

    def __init__(self, srv_stud, srv_prob, srv_asign, srv_statistici):
        """
        Initializeaza clasa Statistici_UI si creaza comenzile
        """
        self.__srv_stud = srv_stud
        self.__srv_prob = srv_prob
        self.__srv_asign = srv_asign
        self.__srv_statistici = srv_statistici
        self.__comenzi = {"1": self.__ui_raport_ordonat_alfabetic,
                          "2": self.__ui_raport_ordonat_dupa_nota,
                          "3": self.__ui_raport_media_5,
                          "4": self.__ui_raport_media_lab_dat
                          }

    def __ui_raport_ordonat_alfabetic(self):
        """
        Raport Lista de studenți și notele lor la o problema de laborator dat, ordonat dupa nume
        """
        nrLab_nrPb = (input(">>>Introduceti ID-ul problemei: "))
        print()
        lista = self.__srv_statistici.raport_ordonat_alfabetic(nrLab_nrPb)
        print("____________________________________________________________________________________________")
        if len(lista) != 0:
            print(
                "\n     Lista de studenți și notele lor la  problema de laborator data(ordonate dupa nume): \n")

            for el in lista:
                nume = el[0].get_nume()
                grupa = el[0].get_grup()
                nota = el[1]
                print("Studentul cu numele " + nume + " din grupa " + str(grupa) + " a luat " + str(nota))
        else:
            print("\n...Problema " + nrLab_nrPb + " nu a fost asignata niciunui student!...\n")
        print("____________________________________________________________________________________________")

    def __ui_raport_ordonat_dupa_nota(self):
        """
        Raport Lista de studenți și notele lor la o problema de laborator dat, ordonat dupa nota
        """
        nrLab_nrPb = (input(">>>Introduceti ID-ul problemei: "))
        print()
        lista = self.__srv_statistici.raport_ordonat_dupa_nota(nrLab_nrPb)
        print("____________________________________________________________________________________________")
        if len(lista) != 0:
            print(
                "\n     Lista de studenți și notele lor la  problema de laborator data(ordonate dupa nota): \n")

            for el in lista:
                nume = el[0].get_nume()
                grupa = el[0].get_grup()
                nota = el[1]
                print("Studentul cu numele " + nume + " din grupa " + str(grupa) + " a luat " + str(nota))
        else:
            print("\n...Problema " + nrLab_nrPb + " nu a fost asignata niciunui student!...\n")
        print("____________________________________________________________________________________________")


    def __ui_raport_media_5(self):
        """
            Raport Lista de studenți cu media notelor de laborator mai mica decat 5
            """
        lista = self.__srv_statistici.raport_media_5()
        print("____________________________________________________________________________________________")
        if len(lista) != 0:
            print(
                "\n     Lista de studenți restantieri: \n")

            for el in lista:
                nume = el[0].get_nume()
                grupa = el[0].get_grup()
                medie = el[1]
                print("Studentul cu numele " + nume + " din grupa " + str(grupa) + " are media " + str(medie))
        else:
            print("\n...Niciun student nu este restantier!...\n")
        print("____________________________________________________________________________________________")


    def __ui_raport_media_lab_dat(self):
        """
        Numărul de studenți notați și „media laboratorului” pentru un laborator dat")
        """
        nrLab_nrPb = (input(">>>Introduceti ID-ul problemei: "))
        print()
        raspuns = self.__srv_statistici.raport_media_lab_dat(nrLab_nrPb)
        print("____________________________________________________________________________________________")
        if raspuns[0] != 0:
            print("Numarul de studenti ce au primit problema " + nrLab_nrPb + ": " + str(raspuns[0]) + "\n"
                  "Media laboratorului " + nrLab_nrPb + ": " + str(raspuns[1]) +"\n"
                  )
        else:
            print("\n...Problema " + nrLab_nrPb + " nu a fost asignata niciunui student!...\n")
        print("____________________________________________________________________________________________")



    def show(self):
        """
            Show menu
            """
        while True:
            printStatisticiMenu()
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
