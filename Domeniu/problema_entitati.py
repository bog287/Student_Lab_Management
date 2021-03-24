class Problema(object):
    def __init__(self, nrLab_nrPb, desc, deadline):
        """
        Initializeaza clasa Problema
        :param: nrLab_nrPb - string
        :param: desc - string
        :param: deadline - int
        """
        self.__nrLab_nrPb = nrLab_nrPb
        self.__desc = desc
        self.__deadline = deadline


    def get_nrLab_nrPb(self):
        """
        Obtine nr si laboratorul unei probleme
        :return: nrLab_nrPb - string
        """
        return self.__nrLab_nrPb

    def get_lab_pb(self, nrLab_nrPb):
        """
        Obtine lab-ul problemei
        :return: string ( lab-ul in care a fost data problema)
        """
        return int(self.__nrLab_nrPb.split("_")[0])

    def get_nr_pb(self, date):
        """
        Obtine numarul problemei
        :return: string
        """
        return int(self.__nrLab_nrPb.split("_")[1])



    def get_desc(self):
        """
        Obtine descrierea unei probleme
        :return: desc - string
        """
        return self.__desc

    def get_deadline(self):
        """
        Obtine deadline-ul unei probleme
        :return: deadline - int > 0
        """
        return  self.__deadline

    def set_deadline(self, val):
        """
        Seteaza  deadline-ul unei pb
        :param: val - int
        """
        self.__deadline = val


    def set_desc(self, val):
        """
        Seteaza descrierea unei pb
        :param: value - string (descriere problema)
        """
        self.__desc = val


    def __str__(self):
        """
        Converteste acest obiect in string
        :return: string (nrLab_nrPb, desc, deadline)
        """
        return str(self.__nrLab_nrPb) + " : " + str(self.__desc) + " : " + str(self.__deadline)

    def __eq__(self, problema):
        """
        Verifica daca doua probleme au acelasi ID
        :param: problema - Problema
        :return: bool (True daca pb curenta are acelasi ID cu pb; False in caz contrar)
        """
        return self.__nrLab_nrPb == problema.__nrLab_nrPb