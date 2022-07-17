from ..ModularPy import ModularOps
    
def test_binary_field():
    "Check that modular operations work for binary fields."
    binField = ModularOps(2)
    
    assert binField.add(0, 0) == 0
    assert binField.add(0, 1) == 1
    assert binField.add(1, 0) == 1
    assert binField.add(1, 1) == 0
    
    assert binField.subtract(0, 0) == 0
    assert binField.subtract(0, 1) == 1
    assert binField.subtract(1, 0) == 1
    assert binField.subtract(1, 1) == 0
    
