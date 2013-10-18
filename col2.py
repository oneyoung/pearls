

# array reverse
def reverse(array, start, end):
    mean = (start + end) / 2
    l, r = start, end
    while l <= mean:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1


def gcd(a, b):
    ''' get gcd of a and b '''
    m, n = (a, b) if a > b else (b, a)
    if n:
        return gcd(m % n, n)
    else:
        return m


# rotate a one-dimensional vec of n elements left by i positions,
# e.g. n=8,i=3, vec='abcdefgh' ==> 'defghabc'
# requirement: T(n)=O(n), only a few extra bytes of storage

def rotate_reverse(array, n, i):
    # idea: let array=ab, where a=[:i], b is the rest
    # revserse(a), then reverse(b), finally reverse(array) will get the result
    reverse(array, 0, i - 1)
    reverse(array, i, n - 1)
    reverse(array, 0, n - 1)
