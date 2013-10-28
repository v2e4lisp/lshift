# shift

left shift arguments to make a function a partial application.

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
