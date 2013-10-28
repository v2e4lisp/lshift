# shift
left shift arguments to make a function a partial application.

[![Build Status](https://travis-ci.org/v2e4lisp/shift.png)](https://travis-ci.org/v2e4lisp/shift)
tested on 2.7, 3.2, 3.3

## install
```bash
pip install shift
```

## API
* `arg(*args, **kwargs)`

## Example
```python
from shift import arg
import operator

double = operator.mul << arg(2)
mapinc = map << arg(lambda x: x+1)
```
