# Copied from the pyrlp project
# https://github.com/ethereum/pyrlp/blob/develop/rlp/utils_py2.py
def decode_hex(s):
    if not isinstance(s, (str, unicode)):
        raise TypeError('Value must be an instance of str or unicode')
    return s.decode('hex')


def encode_hex(s):
    if not isinstance(s, (str, unicode)):
        raise TypeError('Value must be an instance of str or unicode')
    return s.encode('hex')
