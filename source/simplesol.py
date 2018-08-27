# extend
>>> a = [1]
>>> b = a
>>> a.extend([2])
>>> a
[1, 2]
>>> b
[1, 2]

# +=
>>> a = [1]
>>> b = a
>>> a += [2]
>>> a
[1, 2]
>>> b
[1, 2]








python3 -m timeit -n 100 -s "N=1000000; a = list(range(N)); b=list(range(N))" "a.extend(b); a = list(range(N)); "
python3 -m timeit -n 100 -s "N=1000000; a = list(range(N)); b=list(range(N))" "a += b; a = list(range(N)); "
python3 -m timeit -n 100 -s "N=1000000; a = list(range(N)); b=list(range(N))" "a = a + b; a = list(range(N)); "
