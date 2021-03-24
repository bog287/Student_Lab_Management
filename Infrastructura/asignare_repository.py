from Erori.exceptii import RepoError
from Domeniu.asignare_entitati import Asignare


class RepositoryAsignare(object):
    """
        Stocheaza asignarile in memorie
        """

    def __init__(self):
        """
        Initializeaza lista in care vor fi stocate asignarile
        """
        self.__elems = []

    def size(self):
        """
        Returneaza numarul de asignari
        :return: integer (numar asignari)
        """
        return len(self.__elems)

    def adauga(self, asign):
        """
        Adauga o asignare in memorie
        :param: asign - Asignare
        :exception: RepoError: o inscriere cu acelasi ID exista deja
        """
        if asign in self.__elems:
            raise RepoError("Element existent!\n")
        for el in self.__elems:
            if el.get_stud_ID() == asign.get_stud_ID() and el.get_nrLab_nrPb() == asign.get_nrLab_nrPb():
                raise RepoError("Element existent!\n")
        self.__elems.append(asign)

    def get_all(self):
        """
        Returneaza lista cu toate asignarile
        :return: list (lista asignarilor)
        """
        return self.__elems[:]

    def cauta(self, key_asign):
        """
        Cauta un element in functie de o cheie specificata
        :param: key_asign - string
        :exception: RepoError: Nu exista niciun element cu cheia data
        :return: list (elementul cautat)
        """
        if key_asign not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for elem in self.__elems:
            if elem == key_asign:
                return elem

    def cauta_dupa_nrLab_nrPb(self, nrLab_nrPb):
        """
        Cauta un element dupa nrLab_nrPb unei probleme
        :param: nrLab_nrPb - string(identificator unic al unei pb)
        """
        gasit = []
        for elem in self.__elems:
            if elem.get_nrLab_nrPb() == nrLab_nrPb:
                gasit.append(elem)
        return gasit