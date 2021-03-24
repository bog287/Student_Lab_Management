from Business.probleme_servicii import ServiceProbleme
from Domeniu.problema_entitati import Problema
from Erori.exceptii import ValidError, RepoError
from Infrastructura.probleme_repository import RepositoryProbleme
from Validare.problema_validare import Validare_Problema


class Teste_Problema(object):

    def __ruleaza_teste_domeniu(self):
        nrLab_nrPb = "2_7"
        desc = "interesanta"
        deadline = 6
        problema = Problema(nrLab_nrPb, desc, deadline)
        assert problema.get_nrLab_nrPb() == nrLab_nrPb
        assert problema.get_desc() == desc
        assert problema.get_deadline() == deadline
        assert str(problema) == "2_7 : interesanta : 6"
        alta_pb = Problema(nrLab_nrPb, None, None)
        assert problema == alta_pb

    def __ruleaza_teste_validare(self):
        nrLab_nrPb = ""
        desc = "ok"
        deadline = -2
        problema = Problema(nrLab_nrPb, desc, deadline)
        valid = Validare_Problema()
        try:
            valid.valideaza(problema)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID-ul nu poate fi gol!\nDeadline-ul nu poate fi un numar negativ!\n"

    def __ruleaza_teste_repo(self):
        # adaugare
        repo = RepositoryProbleme()
        assert repo.size() == 0
        nrLab_nrPb = "3_2"
        desc = "nu-mi place"
        deadline = "7"
        problema = Problema(nrLab_nrPb, desc, deadline)
        repo.adauga(problema)
        assert repo.size() == 1

        # cautare
        key_pb = Problema(nrLab_nrPb, None, None)
        gasit = repo.cauta(key_pb)
        try:
            repo.adauga(key_pb)
            assert False
        except RepoError as re:
            assert str(re) == "Problema existenta!\n"
        assert gasit.get_desc() == desc
        key_pb_nu = Problema("24", None, None)
        try:
            repo.cauta(key_pb_nu)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

        # modificare
        pb_noua = Problema("13_5", "merge", 14)
        repo.adauga(pb_noua)
        repo.modifica(pb_noua)
        gasit = repo.cauta(pb_noua)
        assert gasit.get_desc() == "merge"
        try:
            repo.modifica(key_pb_nu)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

        # stergere si size
        repo.sterge(key_pb)
        assert repo.size() == 1
        try:
            repo.sterge(key_pb)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

    def __ruleaza_teste_serviciu_gaseste_pb_by_nrLab_nrPb(self):
        repo = RepositoryProbleme()
        valid = Validare_Problema()
        srv = ServiceProbleme(repo, valid)
        nrLab_nrPb = "3_6"
        desc = "ok"
        deadline = 6
        pb = Problema(nrLab_nrPb, desc, deadline)
        repo.adauga(pb)
        assert srv.numar_probleme() == 1
        assert repo.size() == 1
        gasit = srv.gaseste_pb_by_nrPb(nrLab_nrPb)
        assert gasit.get_desc() == "ok"
        assert gasit.get_deadline() == 6
        try:
            srv.gaseste_pb_by_nrPb(3)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

    def __ruleaza_teste_serviciu_modificare(self):
        repo = RepositoryProbleme()
        valid = Validare_Problema()
        srv = ServiceProbleme(repo, valid)
        nrLab_nrPb = "2_1"
        desc = "super"
        deadline = 6
        pb = Problema(nrLab_nrPb, desc, deadline)
        repo.adauga(pb)
        assert srv.numar_probleme() == 1
        assert repo.size() == 1
        desc_noua = "nu e chiar super"
        deadline_nou = 5
        srv.modifica_pb(nrLab_nrPb, desc_noua, deadline_nou)
        key_pb = Problema(nrLab_nrPb, None, None)
        gasit = repo.cauta(key_pb)
        assert gasit.get_desc() == "nu e chiar super"
        assert gasit.get_deadline() == 5
        try:
            srv.modifica_pb(3, desc_noua, deadline_nou)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"


    def __ruleaza_teste_serviciu_sterge(self):
        repo = RepositoryProbleme()
        valid = Validare_Problema()
        srv = ServiceProbleme(repo, valid)
        nrLab_nrPb = "12_11"
        desc = "se putea mai bine"
        deadline = 14
        pb = Problema(nrLab_nrPb, desc, deadline)
        repo.adauga(pb)
        assert srv.numar_probleme() == 1
        srv.adauga_problema("13_4","bine", 16)
        assert srv.numar_probleme() == 2
        srv.sterge_probleme(nrLab_nrPb)
        assert srv.numar_probleme() == 1
        try:
            srv.sterge_probleme("4_1")
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

    def ruleaza_teste(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_serviciu_gaseste_pb_by_nrLab_nrPb()
        self.__ruleaza_teste_serviciu_modificare()
        self.__ruleaza_teste_serviciu_sterge()