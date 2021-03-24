from typing import Dict

from Domeniu.problema_entitati import Problema
from Domeniu.student_entitati import Student


class ServiceStatistici(object):
    def __init__(self, repo_asign, repo_stud, repo_prob):
        """
        Initializeaza clasa ServiceStatistici
        :param: repo_asign - RepositoryAsignare
        :param: repo_stud - RepositoryStudenti
        :param: repo_prob - RepositoryProbleme
        :param: valid - Validare_Asign
        """
        self.__repo_asign = repo_asign
        self.__repo_stud = repo_stud
        self.__repo_prob = repo_prob

    def raport_ordonat_alfabetic(self, nrLab_nrPb):
        """
        Returneaza o lista de studenți și notele lor la o problema de laborator dat, ordonat dupa nume
        :param: nrLab_nrPb - string (identificatorul unic al unei pb)
        :return: lista - list(lista de studenti si notele lor la o pb de laborator dat, in ordine dupa nume)
        """
        lista = []
        gasit = self.__repo_asign.cauta_dupa_nrLab_nrPb(nrLab_nrPb)
        if len(gasit) != 0:
            for el in gasit:
                stud_ID = el.get_stud_ID()
                key_stud = Student(stud_ID, None, None)
                lista.append((self.__repo_stud.cauta(key_stud), el.get_nota()))
            lista.sort(key=lambda x: x[0].get_nume())
        return lista

    def raport_ordonat_dupa_nota(self, nrLab_nrPb):
        """
        Returneaza o lista de studenți și notele lor la o problema de laborator dat, ordonat dupa nota
        :param: nrLab_nrPb - string (identificatorul unic al unei pb)
        :return: lista - list(lista de studenti si notele lor la o pb de laborator dat, in ordine dupa nume)
        """
        lista = []
        gasit = self.__repo_asign.cauta_dupa_nrLab_nrPb(nrLab_nrPb)
        if len(gasit) != 0:
            for el in gasit:
                stud_ID = el.get_stud_ID()
                key_stud = Student(stud_ID, None, None)
                lista.append((self.__repo_stud.cauta(key_stud), el.get_nota()))
            lista.sort(key=lambda x: x[1])
        return lista

    def raport_media_5(self):
        """
        Studentii cu media laboratoarelor mai mica de 5
        """
        dict_lab_notate = {}
        dict_total_note = {}
        lista_restantieri = []
        all_asgn = self.__repo_asign.get_all()
        for el in all_asgn:
            dict_lab_notate[el.get_stud_ID()] = 0
            dict_total_note[el.get_stud_ID()] = 0
        for el in all_asgn:
            dict_lab_notate[el.get_stud_ID()] += 1
            dict_total_note[el.get_stud_ID()] += el.get_nota()

        for el in dict_lab_notate:
            key_stud = Student(el, None, None)
            gasit = self.__repo_stud.cauta(key_stud)
            media = dict_total_note[el] / dict_lab_notate[el]
            if media < 5:
                lista_restantieri.append((gasit, media))
        return lista_restantieri


    def raport_media_lab_dat(self, nrLab_nrPb):
        """
        Returneaza numărul de studenți notați și „media laboratorului” pentru un laborator dat
        :param: nrLab_nrPb - string (identificatorul unic al unei pb)
        :return: raspuns - un tuplu(pe prima pozitie e numarul de studenti notati, iar pe a 2-a media laboratorului)

        """
        raspuns =(0,0)
        medie = 0
        gasit = self.__repo_asign.cauta_dupa_nrLab_nrPb(nrLab_nrPb)
        if len(gasit) != 0:
            for el in gasit:
                medie += el.get_nota()
            medie /= len(gasit)
            raspuns = (len(gasit),medie)
            return raspuns
        else:
            return raspuns


