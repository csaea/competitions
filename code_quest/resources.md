# Coding Competition Resources 

## Python Input Processing

### map()

* [https://www.w3schools.com/python/ref_func_map.asp](https://www.w3schools.com/python/ref_func_map.asp)
* Converts iterable elements using a function (often `int`).

### split()

* [https://www.w3schools.com/python/ref_string_split.asp](https://www.w3schools.com/python/ref_string_split.asp)
* Splits strings by whitespace by default.

### Standard Input (stdin)

* [https://www.w3schools.com/python/ref_file_readline.asp](https://www.w3schools.com/python/ref_file_readline.asp)

Key idea:

* Judges provide input automatically.

---

## Python Standard Libraries Used in Competitions

### sys

* [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
* Faster I/O and stream control.

Common pattern:

```python
import sys
input = sys.stdin.readline
```

---

### math

* [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)
  Useful functions:
* `math.gcd()`
* `math.sqrt()`
* `math.isqrt()`
* `math.factorial()`

---

### string

* [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)
  Contains:
* `string.ascii_lowercase`
* `string.ascii_uppercase`
* `string.digits`

---

## Output Rules

* No prompts
* Match spacing exactly
* Avoid extra blank lines

---

## Common Beginner Mistakes

* Using interactive prompts
* Forgetting integer conversion
* Mixing `input()` and `sys.stdin`
* Reusing exhausted iterators

---

## More Learning Resources

* Python Official Docs → [https://docs.python.org/3/](https://docs.python.org/3/)
* Competitive Programming Basics → [https://cp-algorithms.com/](https://cp-algorithms.com/)

