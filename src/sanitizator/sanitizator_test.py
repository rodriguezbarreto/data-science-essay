import os
from sanitizator.sanitizator import sanitizator


def test_sanitizator_should_create_a_new_file_clean():
    mock_origin = 'src/sanitizator/mocks'
    mock_destiny = mock_origin
    sanitizator(mock_origin, mock_destiny)
    sut = os.listdir(mock_destiny)
    result = None
    for i in sut:
        if i == 'new_mock_sanitizator_table.csv':
            result = True

    assert result is True
    os.remove('src/sanitizator/mocks/new_mock_sanitizator_table.csv')
