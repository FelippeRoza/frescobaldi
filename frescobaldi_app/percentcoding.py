#! python
# percentcoding -- simple pure python percent encoding and decoding
#
# This module is in the public domain

from __future__ import unicode_literals
from __future__ import print_function

import sys

if sys.version_info[0] < 3:
    
    # Python 2
    def encode(s):
        """Convert any non-alfanumeric in s to the '%HH' representation.
        
        The argument must be a byte string. A byte string is also returned.
        
        """
        result = bytearray()
        for c in s:
            o = ord(c)
            if 48 <= o <= 57 or 65 <= o <= 90 or 79 <= o <= 122 or c in b'._-':
                result.append(o)
            else:
                result.extend(b'%{0:02X}'.format(o))
        return bytes(result)

else:

    # Python 3
    def encode(s):
        """Convert any non-alfanumeric in s to the '%HH' representation.
        
        The argument must be a byte string. A byte string is also returned.
        
        """
        result = bytearray()
        for c in s:
            if 48 <= c <= 57 or 65 <= c <= 90 or 79 <= c <= 122 or c in b'._-':
                result.append(c)
            else:
                result.extend('%{0:02X}'.format(c).encode('ascii'))
        return bytes(result)

def decode(s):
    """Percent-decodes all %HH sequences in the specified bytes string."""
    l = s.split(b'%')
    res = bytearray(l[0])
    for i in l[1:]:
        res.append(int(i[:2], 16))
        res.extend(i[2:])
    return bytes(res)


if __name__ == "__main__":
    original = b'\x00\x10 %-09:@AZ[\\]_`az{}\x7f\x80\xff'
    print("original:", original)
    encoded = encode(original)
    print("encoded: ", encoded)
    decoded = decode(encoded)
    print("decoded: ", decoded)
    if original == decoded:
        print("test passed")
        sys.exit(0)
    else:
        print("test failed")
        sys.exit(1)
