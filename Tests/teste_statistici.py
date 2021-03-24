from Business.statistici_servicii import ServiceStatistici
from Domeniu.asignare_entitati import Asignare
from Domeniu.problema_entitati import Problema
from Domeniu.student_entitati import Student
from Infrastructura.asignare_repository import RepositoryAsignare
from Infrastructura.probleme_repository import RepositoryProbleme
from Infrastructura.studenti_repository import RepositoryStudenti
from Validare.asignare_validare import Validare_Asignare


class Teste_Statistici(object):

    def __ruleaza_teste_serviciu_statistici_ordonat_alfabetic(self):
        repo_asign = RepositoryAsignare()
        repo_stud = RepositoryStudenti()
        repo_prob = RepositoryProbleme()
        valid = Validare_Asignare()
        srv = ServiceStatistici(repo_asign, repo_stud, repo_prob)
        student_1 = Student(5, "Alina", "411")
        repo_stud.adauga(student_1)
        student_2 = Student(7,"Daniel", "321")
        repo_stud.adauga(student_2)
        student_3 = Student(10, "Bogdan", "222")
        repo_stud.adauga(student_3)
        pb_1 = Problema("13_13", "grea", 16)
        repo_prob.adauga(pb_1)
        asign_1 = Asignare(88, 5, "13_13", 7)
        repo_asign.adauga(asign_1)
        asign_2 = Asignare(89,7, "13_13", 9)
        repo_asign.adauga(asign_2)
        asign_3 = Asignare(90, 10, "13_13", 10)
        repo_asign.adauga(asign_3)
        lista = srv.raport_ordonat_alfabetic("13_13")
        assert lista[0][0].get_nume() == "Alina"
        assert lista[1][0].get_nume() == "Bogdan"
        assert lista[0][1] == 7
        lista = srv.raport_ordonat_alfabetic("15_15")
        assert lista == []


    def __ruleaza_teste_serviciu_statistici_ordonat_dupa_nota(self):
        repo_asign = RepositoryAsignare()
        repo_stud = RepositoryStudenti()
        repo_prob = RepositoryProbleme()
        valid = Validare_Asignare()
        srv = ServiceStatistici(repo_asign, repo_stud, repo_prob)
        student_1 = Student(5, "Alina", "411")
        repo_stud.adauga(student_1)
        student_2 = Student(7,"Daniel", "321")
        repo_stud.adauga(student_2)
        student_3 = Student(10, "Bogdan", "222")
        repo_stud.adauga(student_3)
        pb_1 = Problema("13_13", "grea", 16)
        repo_prob.adauga(pb_1)
        asign_1 = Asignare(88, 5, "13_13", 7)
        repo_asign.adauga(asign_1)
        asign_2 = Asignare(89,7, "13_13", 9)
        repo_asign.adauga(asign_2)
        asign_3 = Asignare(90, 10, "13_13", 10)
        repo_asign.adauga(asign_3)
        lista = srv.raport_ordonat_dupa_nota("13_13")
        assert lista[0][0].get_nume() == "Alina"
        assert lista[2][0].get_nume() == "Bogdan"
        assert lista[1][1] == 9
        lista = srv.raport_ordonat_alfabetic("15_15")
        assert lista == []


    def __ruleaza_teste_serviciu_media_5(self):
        repo_asign = RepositoryAsignare()
        repo_stud = RepositoryStudenti()
        repo_prob = RepositoryProbleme()
        valid = Validare_Asignare()
        srv = ServiceStatistici(repo_asign, repo_stud, repo_prob)
        student_1 = Student(6, "Mishu", "321")
        repo_stud.adauga(student_1)
        student_2 = Student(7, "Matei", "322")
        repo_stud.adauga(student_2)
        student_3 = Student(8, "Mircea", "352")
        repo_stud.adauga(student_3)
        problema_1 = Problema("14_1","nasoala", 16)
        repo_prob.adauga(problema_1)
        problema_2 = Problema("13_1", "nasoala", 16)
        repo_prob.adauga(problema_2)
        problema_3 = Problema("12_1", "nasoala", 16)
        repo_prob.adauga(problema_3)
        problema_4 = Problema("11_1", "nasoala", 16)
        repo_prob.adauga(problema_4)
        problema_5 = Problema("10_1", "nasoala", 16)
        repo_prob.adauga(problema_5)
        problema_6 = Problema("9_1", "nasoala", 16)
        repo_prob.adauga(problema_6)
        asignare_1 = Asignare(21, 6, "14_1", 3)
        repo_asign.adauga(asignare_1)
        asignare_2 = Asignare(22, 7, "12_1", 5)
        repo_asign.adauga(asignare_2)
        asignare_3 = Asignare(23, 8, "14_1", 4)
        repo_asign.adauga(asignare_3)
        asignare_4 = Asignare(24, 6, "10_1", 3)
        repo_asign.adauga(asignare_4)
        asignare_5 = Asignare(25, 7, "14_1", 5)
        repo_asign.adauga(asignare_5)
        asignare_6 = Asignare(26, 8, "9_1", 4)
        repo_asign.adauga(asignare_6)
        lista_1 = srv.raport_media_5()
        assert len(lista_1) == 2
        assert lista_1[0][0].get_stud_id() == 6
        assert lista_1[0][0].get_nume() == "Mishu"
        assert lista_1[1][0].get_stud_id() == 8

    def __ruleaza_teste_serviciu_statistici_media_lab_dat(self):
        repo_asign = RepositoryAsignare()
        repo_stud = RepositoryStudenti()
        repo_prob = RepositoryProbleme()
        valid = Validare_Asignare()
        srv = ServiceStatistici(repo_asign, repo_stud, repo_prob)
        student_1 = Student(5, "Alina", "411")
        repo_stud.adauga(student_1)
        student_2 = Student(7, "Daniel", "321")
        repo_stud.adauga(student_2)
        student_3 = Student(10, "Bogdan", "222")
        repo_stud.adauga(student_3)
        pb_1 = Problema("13_13", "grea", 16)
        pb_2 = Problema("13_14", "grea", 16)
        repo_prob.adauga(pb_1)
        repo_prob.adauga(pb_2)
        asign_1 = Asignare(88, 5, "13_13", 7)
        repo_asign.adauga(asign_1)
        asign_2 = Asignare(89, 7, "13_13", 7)
        repo_asign.adauga(asign_2)
        asign_3 = Asignare(90, 10, "13_13", 10)
        repo_asign.adauga(asign_3)
        answer = srv.raport_media_lab_dat("13_13")
        assert answer[0] == 3
        answer = srv.raport_media_lab_dat("15_15")
        assert answer[0] == 0

    def ruleaza_teste(self):
        self.__ruleaza_teste_serviciu_statistici_ordonat_alfabetic()
        self.__ruleaza_teste_serviciu_statistici_ordonat_dupa_nota()
        self.__ruleaza_teste_serviciu_media_5()
        self.__ruleaza_teste_serviciu_statistici_media_lab_dat()
