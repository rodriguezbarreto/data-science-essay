from sanitizator.sanitizator import sanitizator


def test_sanitizator():
    assert sanitizator() == 'olá mundo'
