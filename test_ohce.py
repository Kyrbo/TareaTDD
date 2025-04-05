from ohce import ohce

def test_palabra_inversa():
    assert ohce("hola") == "aloh"
    
def test_palindromo():
    assert ohce("oso") =="oso\n¡Bonita palabra!"