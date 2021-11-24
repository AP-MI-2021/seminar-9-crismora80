from Domain.localitateValidator import LocalitateValidator
from Domain.rutaValidator import RutaValidator
from Repository.json_repository import JsonRepository
from Service.localitateService import LocalitateService
from Service.rutaService import RutaService
from Teste.tests import runAllTests
from UserInterface.console import Console


def main():
    localitateRepository = JsonRepository("localitati.json")
    localitateValidator = LocalitateValidator()
    rutaRepository = JsonRepository("rute.json")
    rutaValidator = RutaValidator()

    localitateService = LocalitateService(localitateRepository,
                                          localitateValidator)
    rutaService = RutaService(rutaRepository, rutaValidator, localitateRepository)

    console = Console(localitateService, rutaService)
    console.runMenu()


if __name__ == '__main__':
    runAllTests()
    main()
