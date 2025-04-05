from ohce import ohce
from ohce import saludar
def test_palabra_inversa():
    assert ohce("hola") == "aloh"
    
def test_palindromo():
    assert ohce("oso") =="oso\n¡Bonita palabra!"
    
def test_detenerse_Stop():
    assert ohce("Stop!") == "Adios"

def test_saludo_dia():
    assert saludar("Juan", 9) == "¡Buenos días, Juan!"

def test_saludo_tarde():
    assert saludar("Juan", 15) == "¡Buenas tardes, Juan!"

def test_saludo_noche():
    assert saludar("Juan", 22) == "¡Buenas noches, Juan!"

def test_saludo_madrugada():
    assert saludar("Juan", 3) == "¡Buenas noches, Juan!"
