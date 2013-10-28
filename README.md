# lshift
left shift arguments to make a function a partial application.

[![Build Status](https://travis-ci.org/v2e4lisp/lshift.png)](https://travis-ci.org/v2e4lisp/lshift)
tested on 2.7, 3.2, 3.3

## install
```bash
pip install lshift
```

## API
* `arg(*args, **kwargs)`

## Example
```python
from lshift import arg
import operator

double = operator.mul << arg(2)
mapinc = map << arg(lambda x: x+1)
```
