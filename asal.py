def asal_sayi(a):
    """\
	>>> asal_sayi(17)
	2
	3
	5
	7
	11
	13
	17
	"""
    i = 1
    while i < a:
        i = i + 1
	k = 1
    while k < i:
	k = k + 1
        if i%k == 0 and i == k:
            print i
        if i%k == 0 and i != k:
            break
doctest.testmod()
