# Copied from the pyrlp project
# https://github.com/ethereum/pyrlp/blob/develop/rlp/utils_py3.py
import binascii

def decode_hex(s):
    if isinstance(s, str):
        return bytes.fromhex(s)
    if isinstance(s, bytes):
        return binascii.unhexlify(s)
    raise TypeError('Value must be an instance of str or bytes')


def encode_hex(b):
    if isinstance(b, str):
        b = bytes(b, 'utf-8')
    if isinstance(b, bytes):
        return str(binascii.hexlify(b))[2:-1]
    raise TypeError('Value must be an instance of str or bytes')
