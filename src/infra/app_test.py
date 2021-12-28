from infra.app import app


def app_test():
    assert app() == 'olá mundo'
