from hologram_project.exceptions import InvalidFormatException

def exception_message(data):
    return f'The following data has not been properly formatted: {"".join(data)}'

def parse_basic_string(data):
    """
    Basic strings are comma separated with just two values, the id and the bytes used, both integers.

    Example data:
    `<id>,<bytes_used>`

    :param data: an array of values
    :return: a parsed object to be uploaded to the database
    """
    try:
        return_data = {
            'id': int(data[0]),
            'bytes_used': int(data[1])
        }
        return format_data(**return_data)
    except (IndexError, ValueError):
        raise InvalidFormatException(exception_message(data))

def parse_extended_string(data):
    """
    Extended strings are comma separated with values for multiple fields.
    All values are integers except `dmcc` which is a string.
    Fields are always in the same order.

    Example data:
    `<id>,<dmcc>,<mnc>,<bytes_used>,<cellid>`

    :param data: an array of values
    :return: a parsed object to be uploaded to the database
    """
    try:
        return_data = {
            'id': int(data[0]),
            'dmcc': data[1],
            'mnc': int(data[2]),
            'bytes_used': int(data[3]),
            'cellid': int(data[4]),
        }
        return format_data(**return_data)
    except (IndexError, ValueError):
        raise InvalidFormatException(exception_message(data))

def parse_hex_string(data):
    """
    Hex strings consist of two comma separate values:
    the id, and a string of hex bytes representing more rich data.
    To access the values, the hex string will have to be parsed.


    Bytes 1-2 → mnc -> be83
    Bytes 3-4 → bytes_used -> 3279
    Bytes 5-8 → cellid -> 000000c0
    Bytes 9-12 → ip -> 63e5e63d
        - NOTE: Each byte is one segment of the ip, separated by a period:
            e.g. `c0a80001` would be `'192.168.0.1'`

    :param data:
    :return:
    """
    try:
        hex_bytes = data[1]
        mnc = int(hex_bytes[0:4], 16)
        bytes_used = int(hex_bytes[4:8], 16)
        cellid = int(hex_bytes[8:16], 16)
        ip_raw = hex_bytes[16:24]
        ip = f'{int(ip_raw[0:2], 16)}.{int(ip_raw[2:4], 16)}.{int(ip_raw[4:6], 16)}.{int(ip_raw[6:8], 16)}'

        return_data = {
            'id': int(data[0]),
            'mnc': mnc,
            'bytes_used': bytes_used,
            'cellid': cellid,
            'ip': ip,
        }
        return format_data(**return_data)
    except (IndexError, ValueError):
        raise InvalidFormatException(exception_message(data))

def format_data(id, bytes_used, dmcc=None, mnc=None, cellid=None, ip=None):
    """Ensures that all data is properly formatted for upload to database"""
    return {
        'id': id,
        'bytes_used': bytes_used,
        'dmcc': dmcc,
        'mnc': mnc,
        'cellid': cellid,
        'ip': ip
    }
