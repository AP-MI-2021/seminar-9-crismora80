from Domain.localitate import Localitate
from Domain.localitateValidator import LocalitateValidator
from Repository.json_repository import JsonRepository


class LocalitateService:
    def __init__(self, localitateRepository: JsonRepository, localitateValidator: LocalitateValidator):
        self.localitateRepository = localitateRepository
        self.localitateValidator = localitateValidator

    def adauga(self, idLocalitate: str, nume: str, tip: str):
        '''
        adauga o localitate in multimea de localitati
        :param idLocalitate: id-ul localitatii
        :param nume: numele localitatii
        :param tip: tipul localitatii (sat, oras, municipiu)
        :return:
        '''
        localitate = Localitate(idLocalitate, nume, tip)
        self.localitateValidator.valideaza(localitate)
        self.localitateRepository.create(localitate)

    def getAll(self):
        return self.localitateRepository.read()