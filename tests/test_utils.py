from unittest import TestCase

from hologram_project.exceptions import InvalidFormatException
from hologram_project.utils import parse_basic_string, parse_extended_string, parse_hex_string


class TestUtils(TestCase):
    # Basic string parsing tests
    def test_parse_basic_string_valid(self):
        input_array = ['9991','2935']
        expected_output = {'id': 9991, 'bytes_used': 2935, 'dmcc': None, 'mnc': None, 'cellid': None, 'ip': None}
        self.assertEqual(parse_basic_string(input_array), expected_output)
    def test_parse_basic_string_non_int(self):
        input_string = ['this','fails']
        with self.assertRaises(InvalidFormatException):
            parse_basic_string(input_string)
    def test_parse_basic_string_missing_args(self):
        input_string = ['fails']
        with self.assertRaises(InvalidFormatException):
            parse_basic_string(input_string)

    # Extended string parsing tests
    def test_parse_extended_string_valid(self):
        input_array = ['4','0d39f','0','495594','214']
        expected_output = {'id': 4, 'bytes_used': 495594, 'dmcc': '0d39f', 'mnc': 0, 'cellid': 214, 'ip': None}
        self.assertEqual(parse_extended_string(input_array), expected_output)
    def test_parse_extended_string_non_int(self):
        input_array = ['fails','0d39f','0','495594','214']
        with self.assertRaises(InvalidFormatException):
            parse_extended_string(input_array)
    def test_parse_extended_string_missing_args(self):
        input_string = ['fails']
        with self.assertRaises(InvalidFormatException):
            parse_extended_string(input_string)

    # Hex string parsing tests
    def test_parse_hex_string_valid(self):
        input_array = ['16', 'be833279000000c0c0a80001']
        expected_output = {'id': 16, 'bytes_used': 12921, 'dmcc': None, 'mnc': 48771, 'cellid': 192, 'ip': '192.168.0.1'}
        self.assertEqual(parse_hex_string(input_array), expected_output)

    def test_parse_hex_string_non_int(self):
        input_array = ['fails', 'be833279000000c0c0a80001']
        with self.assertRaises(InvalidFormatException):
            parse_hex_string(input_array)

    def test_parse_hex_string_missing_args(self):
        input_string = ['fails']
        with self.assertRaises(InvalidFormatException):
            parse_hex_string(input_string)
