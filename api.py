from flask import request
from flask_restful import Resource

from constants import EXTENDED_STRING_ENDING, HEX_STRING_ENDING
from utils import parse_extended_string, parse_hex_string, parse_basic_string


class Cdr(Resource):
    def post(self):
        """
        Allows the user to upload CDR (Call Data Record) files to the database

        :return:
        """
        file = request.files['file']
        file_content = file.read()

        for line in file_content.decode('utf-8').split('\n'):
            data = line.split(',')

            if data[0][-1] == EXTENDED_STRING_ENDING:
                parsed_object = parse_extended_string(data)
            elif data[0][-1] == HEX_STRING_ENDING:
                parsed_object = parse_hex_string(data)
            else:
                parsed_object = parse_basic_string(data)

