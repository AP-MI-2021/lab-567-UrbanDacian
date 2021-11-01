from Tests.TestCRUD import testAdaugareCarte, testModificareCarte
from Tests.TestFunctionalitate1 import testAplicareReduceri
from Tests.TestFunctionalitate2 import testModificareGen


def runAllTests():
    testAdaugareCarte()
    testModificareCarte()
    testAplicareReduceri()
    testModificareGen()