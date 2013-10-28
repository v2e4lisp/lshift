class _Partial(object):
    def __init__(self, *args, **kwargs):
        self.fn = None
        self.args = list(args)
        self.kwargs = kwargs

    def __rlshift__(self, fn):
        self.fn = fn
        return self

    def __lshift__(self, part):
        return self.partial(*part.args, **part.kwargs)

    def __call__(self, *args, **kwargs):
        args = self.args + list(args)
        kwargs = dict(self.kwargs, **kwargs)
        return self.fn(*args, **kwargs)

    def partial(self, *args, **kwargs):
        self.args.extend(list(args))
        self.kwargs.update(kwargs)
        return self
        

def arg(*args, **kwargs):
    return _Partial(*args, **kwargs)
