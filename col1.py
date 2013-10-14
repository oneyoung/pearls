import math


class BitVectors(object):
    def __init__(self, size):
        byte_size = int(math.ceil(size / 8.0))
        self.data = bytearray(byte_size)

    def get(self, index):
        byte_index = index / 8
        bit_offset = index % 8
        byte = self.data[byte_index]
        return 1 if byte & (1 << bit_offset) else 0

    def set(self, index, value):
        byte_index = index / 8
        bit_offset = index % 8
        byte = self.data[byte_index]
        if value:
            self.data[byte_index] = byte | (1 << bit_offset)
        else:
            self.data[byte_index] = byte & ~(1 << bit_offset)


def bitmap_sort(fin, fout, n):
    fp_in = open(fin)
    fp_out = open(fout, 'w')
    # generate bitmaps
    bits = BitVectors(n)
    # set bitmaps
    for num in fp_in.xreadlines():
        bits.set(int(num), 1)
    # extract bitmaps
    for index in xrange(n):
        if bits.get(index):
            fp_out.write(str(index) + '\n')
    fp_in.close()
    fp_out.close()
