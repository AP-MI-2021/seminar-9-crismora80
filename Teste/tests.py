from Domain.localitate import Localitate
from Domain.localitateValidator import LocalitateValidator
from Domain.rutaValidator import RutaValidator
from Repository.json_repository import JsonRepository
from Service.localitateService import LocalitateService
from Service.rutaService import RutaService


def runAllTests():
    testAdaugaLocalitate()
    testAdaugaRuta()
    testOrdoneazaLocalitati()
    testRuteMunicipiu()

def clearFile(filename):
    with open(filename, "w") as f:
        pass

def testAdaugaLocalitate():
    clearFile("test-localitati.json")
    localitateRepository = JsonRepository("test-localitati.json")
    localitateValidator = LocalitateValidator()

    localitateService = LocalitateService(localitateRepository,
                                          localitateValidator)

    localitateService.adauga("1", "Fagaras", "municipiu")
    localitateService.adauga("2", "Brasov", "oras")

    localitati = localitateService.getAll()
    assert len(localitati) == 2
    assert localitati[0].id_entity == "1"
    assert localitati[0].nume == "Fagaras"
    assert localitati[0].tip == "municipiu"
    assert localitati[1].id_entity == "2"
    assert localitati[1].nume == "Brasov"
    assert localitati[1].tip == "oras"

def testAdaugaRuta():
    clearFile("test-localitati.json")
    localitateRepository = JsonRepository("test-localitati.json")

    localitateRepository.create(Localitate("1", "Fagaras", "municipiu"))
    localitateRepository.create(Localitate("2", "Brasov", "oras"))

    clearFile("test-rute.json")
    rutaRepository = JsonRepository("test-rute.json")
    rutaValidator = RutaValidator()

    rutaService = RutaService(rutaRepository, rutaValidator, localitateRepository)

    rutaService.adauga("1", "1", "2", 23.5, True)

    rute = rutaService.getAll()
    assert len(rute) == 1
    assert rute[0].id_entity == "1"
    assert rute[0].idOrasPornire == "1"
    assert rute[0].idOrasOprire == "2"
    assert rute[0].pret == 23.5
    assert rute[0].dusIntors == True

def testOrdoneazaLocalitati():
    clearFile("test-localitati.json")
    localitateRepository = JsonRepository("test-localitati.json")

    localitateRepository.create(Localitate("1", "Fagaras", "municipiu"))
    localitateRepository.create(Localitate("2", "Brasov", "oras"))
    localitateRepository.create(Localitate("3", "Floresti", "sat"))

    clearFile("test-rute.json")
    rutaRepository = JsonRepository("test-rute.json")
    rutaValidator = RutaValidator()

    rutaService = RutaService(rutaRepository, rutaValidator,
                              localitateRepository)

    rutaService.adauga("1", "1", "2", 23.5, True)
    rutaService.adauga("2", "2", "3", 23.5, False)

    localitatiOrdonate = rutaService.ordoneazaLocalitatiNrRute()
    assert localitatiOrdonate[0]["localitate"].id_entity == "2"
    assert localitatiOrdonate[0]["numarRute"] == 0
    assert localitatiOrdonate[1]["localitate"].id_entity == "3"
    assert localitatiOrdonate[1]["numarRute"] == 0
    assert localitatiOrdonate[2]["localitate"].id_entity == "1"
    assert localitatiOrdonate[2]["numarRute"] == 1

def testRuteMunicipiu():
    clearFile("test-localitati.json")
    localitateRepository = JsonRepository("test-localitati.json")

    localitateRepository.create(Localitate("1", "Fagaras", "municipiu"))
    localitateRepository.create(Localitate("2", "Brasov", "oras"))
    localitateRepository.create(Localitate("3", "Floresti", "sat"))

    clearFile("test-rute.json")
    rutaRepository = JsonRepository("test-rute.json")
    rutaValidator = RutaValidator()

    rutaService = RutaService(rutaRepository, rutaValidator,
                              localitateRepository)

    rutaService.adauga("1", "3", "2", 23.5, True)
    rutaService.adauga("2", "2", "1", 23.5, True)

    ruteMunicipiu = rutaService.determinaRuteMunicipiu()
    assert len(ruteMunicipiu) == 1
    assert ruteMunicipiu[0]["ruta"].id_entity == "2"
    assert ruteMunicipiu[0]["numeOrasPornire"] == "Brasov"
    assert ruteMunicipiu[0]["numeOrasOprire"] == "Fagaras"
