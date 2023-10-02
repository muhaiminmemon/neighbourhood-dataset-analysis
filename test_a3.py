import copy
import unittest
from a3 import get_bigger_neighbourhood as gbn
from a3 import SAMPLE_DATA


class TestGetBiggerNeighbourhood(unittest.TestCase):
    """Test the function get_bigger_neighbourhood."""

    def test_first_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when its population is strictly greater than the
        population of the second neighbourhood.

        """
        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Rexdale-Kipling', 'Elms-Old Rexdale')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)

    # TODO: add a complete test suite here
    
    def test_second_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when its population is larger than the
        population of the second neighbourhood.

        """
        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Elms-Old Rexdale', 'Rexdale-Kipling')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_second_not_in_dict(self):
        """Test that get_bigger_neighbourhood returns the first
        neighbourhood when the second neighbourhood is not in the dictionary.
        
        """
        sample_data_copy = copy .deepcopy(SAMPLE_DATA)
        expected = 'York University Heights'
        actual = gbn(SAMPLE_DATA, 'York University Heights', 'utsc')
        msg = message (sample_data_copy, expected, actual)
        self.assertEqual (actual, expected, msg)
        
        
    def test_same_both(self):
        """Test that get_bigger_neighbourhood returns the first
        neighbourhood when the population is equal to the second neighbourhood.
        
        """
        sample_data_copy = copy .deepcopy(SAMPLE_DATA)
        expected = 'utsc'
        actual = gbn(
            SAMPLE_DATA, 'utsc', 'uoft')
        msg = message (sample_data_copy, expected, actual)
        self.assertEqual (actual, expected, msg)  
   
    
    def test_first_not_in_dict(self):
        """Test that get_bigger_neighbourhood returns the second
        neighbourhood when the first neighbourhood is not in the dictionary.
        
        """
        sample_data_copy = copy .deepcopy(SAMPLE_DATA)
        expected = 'York University Heights'
        actual = gbn(SAMPLE_DATA, 'utsc', 'York University Heights')
        msg = message (sample_data_copy, expected, actual)
        self.assertEqual (actual, expected, msg)    


def message(test_case: dict, expected: list, actual: object) -> str:
    """Return an error message saying the function call
    get_most_published_authors(test_case) resulted in the value
    actual, when the correct value is expected.

    """

    return ("When we called get_most_published_authors(" + str(test_case) +
            ") we expected " + str(expected) +
            ", but got " + str(actual))


if __name__ == '__main__':
    unittest.main(exit=False)
