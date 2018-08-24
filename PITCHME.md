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
@snap[center]
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


---?code=source/ceval.c&lang=c&title=ceval.c

@[1280-1304](Addition!)

---
### Addition in Python






