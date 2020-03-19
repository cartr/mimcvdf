import sys
import os
sys.path.append('..')
import unittest
import time
from hashlib import sha3_256

import mimcvdf.mimc

class TestMimc(unittest.TestCase):

    def test_bytes(self):
        start = time.time()
        data = b"a" * 6000000
        h = sha3_256()
        h.update(data)
        data = int(h.hexdigest(), 16)

        forw = mimcvdf.forward_mimc(data, 2000)

        rev = mimcvdf.reverse_mimc(forw, 2000)

        print(data)
        print(forw, rev)
        self.assertEqual(rev, data)

unittest.main()