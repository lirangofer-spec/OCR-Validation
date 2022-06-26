import pytest as pytest
from checkForAllow import checkForAllowed
import db.methods as database

from getNumber import getNumberFromFile

@pytest.mark.parametrize("file_input, expected", [("ends_with_25_allowed", True),
                                                 ("last_two_digits_87_not_allowed", False),
                                                 ("seven_digits_ends_with_0_not_allowed", False)])
def test_allow(file_input, expected):
    plate_number_ocr = getNumberFromFile(filename="pictures/"+file_input+".jpeg")
    plate_number_cleared = plate_number_ocr.replace('-', '').replace(':', '')
    allowed_or_not = checkForAllowed(plate_number_cleared)
    assert allowed_or_not == expected
    data = database.Methods()
    data.add(plate_number_cleared, allowed_or_not, file_input)
    get_result = data.get(file_input)
    assert get_result['timestamp'] is not None
    assert get_result['platenumber'] == plate_number_cleared
    assert get_result['filename'] == file_input
    assert get_result['isallowed'] == expected


