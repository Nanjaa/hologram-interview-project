from flask import request
from flask_restful import Resource

from hologram_project.constants import EXTENDED_STRING_ENDING, HEX_STRING_ENDING
from hologram_project.db import bulk_add_cdr, get_all_cdrs
from hologram_project.utils import parse_extended_string, parse_hex_string, parse_basic_string


class CdrController(Resource):
    def post(self):
        """
        Allows the user to upload CDR (Call Data Record) files to the database

        :return:
        """
        file = request.files['file']
        file_content = file.read()
        objects_to_upload = []

        for line in file_content.decode('utf-8').split('\n'):
            data = line.split(',')

            if data[0][-1] == EXTENDED_STRING_ENDING:
                parsed_object = parse_extended_string(data)
            elif data[0][-1] == HEX_STRING_ENDING:
                parsed_object = parse_hex_string(data)
            else:
                parsed_object = parse_basic_string(data)

            objects_to_upload.append(parsed_object)

        bulk_add_cdr(objects_to_upload)

    def get(self):
        """
        Returns a list of CDR objects from the database

        :return:
        """
        cdrs = get_all_cdrs()
        return list(cdrs)