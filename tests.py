import unittest
import random


class TestCol1(unittest.TestCase):
    def test_BitVectors(self):
        from col1 import BitVectors
        length = 13
        bits = BitVectors(length)
        # initial value check
        for i in xrange(length):
            assert not bits.get(i), 'initial val not zero'
        # set test
        for i in xrange(length):
            val = 1
            bits.set(i, val)
            if val:
                assert bits.get(i), 'set error to 1'
            else:
                assert not bits.get(i), 'set error to 0'
            val = 0
            bits.set(i, val)
            if val:
                assert bits.get(i), 'set error to 1'
            else:
                assert not bits.get(i), 'set error to 0'

    def test_bitmap_sort(self):
        def nums_gen(fname, n):
            nums = range(n)
            random.shuffle(nums)
            fp = open(fname, 'w')
            string = '\n'.join(map(str, nums))
            fp.write(string)
            fp.close()

        input_file = '/tmp/nums.txt'
        output_file = '/tmp/nums_sort.txt'
        n = 1000000
        nums_gen(input_file, n)
        from col1 import bitmap_sort as bitmap_sort
        bitmap_sort(input_file, output_file, n)
        # vefiry result
        last = -1
        fp = open(output_file)
        for l in fp.xreadlines():
            num = int(l)
            assert num > last, 'num not sort'
            last = num


class TestCol2(unittest.TestCase):
    def test_rotate_array(self):
        # prepare tested data
        a1 = 'abcedfgh'
        a2 = 'ihjkilshil'
        n = len(a1) + len(a2)
        i = len(a1)
        desired_array = bytearray(a2 + a1)

        def test1method(method):
            array = bytearray(a1 + a2)
            method(array, n, i)
            self.assertSequenceEqual(array, desired_array)

        # test reverse method
        from col2 import rotate_reverse
        test1method(rotate_reverse)

        # test juggling method
        from col2 import rotate_juggling
        test1method(rotate_juggling)
