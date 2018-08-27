## Through the CPython Looking Glass
<br><br>
#### `extend` and `+=` on lists
#### Varun Nayyar

---

### Setting the stage

```python
def main(config):
    cmd = ["/company/binary"]
    ...
    if config.dryrun:
        cmd += ["--dest", "localhost", "--dryrun"]
```

- “Use extend instead, += is slower and less efficient. This will create new list from originals and concatenate“
- “But += is more pythonic. Doesn’t matter for small lists”
- Good excuse to avoid work!!

---

### Simple Solution - `extend`

```python
# extend
>>> a = [1]
>>> b = a
>>> a.extend([2])
>>> a
[1, 2]
>>> b
[1, 2]
```

---
### Simple Solution - `+=`
```python
# +=
>>> a = [1]
>>> b = a
>>> a += [2]
>>> a
[1, 2]
>>> b
[1, 2]
```
 
---
### Simple Solution - `timeit`

Note: run with `N` repeats and 1 run to reset and not deal with list creation times.
Also, keep 
```python
setupStr = """
a = list(range({N})); b=list(range({N}, 2*{N}))
"""

statement = {
    'ext': "a.extend(b)",
    'iadd': "a += b",
    'add': "a + b"
}

for Npow in range(1, 7):
    for method, stmt in statement.items():
        time = min(timeit.repeat(stmt, setup.format(N=10**Npow, repeat=10**(7-Npow), number=1))
```


---
### Simple Solution - `timeit`

Note: run with `N` repeats and 1 run to reset and not deal with list creation times.
Also, keep 
```python
setupStr = """
a = list(range({N})); b=list(range({N}, 2*{N}))
"""

statement = {
    'ext': "a.extend(b)",
    'iadd': "a += b",
    'add': "a + b"
}

for Npow in range(1, 7):
    for method, stmt in statement.items():
        time = min(timeit.repeat(stmt, setup.format(N=10**Npow, repeat=10**(7-Npow), number=1))
```

---
### Simple Solution - `timeit`

Times reported are `time*num_repeat` for standardisation

|   Npow |       ext |      iadd |       add |
|-------:|----------:|----------:|----------:|
|      1 | 0.180997  | 0.149972  | 0.173983  |
|      2 | 0.0395987 | 0.0357977 | 0.0569009 |
|      3 | 0.0146602 | 0.0140999 | 0.04467   |
|      4 | 0.017182  | 0.017094  | 0.053719  |
|      5 | 0.0521498 | 0.0515629 | 0.0768844 |
|      6 | 0.0633772 | 0.0634223 | 0.159378  |



---
### Simple Solution - `timeit`

![Graph](assets/timer.png)

---

@snap[center]
## Solved? |
## Too Easy!! 
## We need to go deeper!
@snapend

---

### Binary Ops in Python

- Let’s use [PEP 465 - Matmul(@)](https://github.com/python/cpython/commit/d51374ed78a3e3145911a16cdf3b9b84b3ba7d15) as a guide!
- `ceval.c` executes the ast
- `object.h` defines the structs of functions
- `abstract.c` defines how operations are carried out
- `listobject.c` defines how lists behave


--- 
### Addition in Python

#### ceval.c:1280-1304

```c
TARGET(BINARY_ADD) {
    PyObject *right = POP();
    PyObject *left = TOP();
    PyObject *sum;
    /* NOTE(haypo): Please don't try to micro-optimize int+int on
       CPython using bytecode, it is simply worthless.
       See http://bugs.python.org/issue21955 and
       http://bugs.python.org/issue10044 for the discussion. In short,
       no patch shown any impact on a realistic benchmark, only a minor
       speedup on microbenchmarks. */
    if (PyUnicode_CheckExact(left) &&
             PyUnicode_CheckExact(right)) {
        sum = unicode_concatenate(left, right, f, next_instr);
        /* unicode_concatenate consumed the ref to left */
    }
    else {
        sum = PyNumber_Add(left, right);
        Py_DECREF(left);
    }
    Py_DECREF(right);
    SET_TOP(sum);
    if (sum == NULL)
        goto error;
    DISPATCH();
}
```

+++

### Addition in Python
#### object.h







