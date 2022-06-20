# import pytest for testing
import pytest

# import the function to be tested
from height_pairs import find_macthing_pairs

# test for the minimun height : 139 
def test_min():
    print("Testing the minimum height possible")
    exp_pairs = [print('Brevin Knight          Nate Robinson'),print('Nate Robinson          Mike Wilks')]
    assert find_macthing_pairs(139) == exp_pairs

# test several values of h with no matching pairs 
@pytest.mark.parametrize("test_input,expected", [(305, "No matches found!"), (90, "No matches found!"), (619, "No matches found!")])
def test_no_matches(test_input, expected):
    assert find_macthing_pairs(test_input) == expected
 