#!/usr/bin/env python

import sys
import struct

xor = 138
data = sys.argv[1]

payload = struct.pack('!' + ('i' * len(sys.argv[1])), *map(lambda x : ord(x) ^ xor, list(sys.argv[1])))

outfile = open("data.bin", "wb")
outfile.write(payload)
outfile.close()
