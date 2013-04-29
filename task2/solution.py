from collections import OrderedDict


def groupby(func, seq):
    groups = {}
    for element in seq:
        groups.setdefault(func(element), []).append(element)
    return groups


def compose(f, g):
    return lambda x: f(g(x))


def iterate(func):
    composition = lambda x: x

    while True:
        yield composition
        composition = compose(func, composition)


def zip_with(func, *iterables):
    return (func(*x) for x in zip(*iterables))


def cache(func, cache_size):
    if cache_size <= 0:
            return func
    func_cache = OrderedDict()
    def func_cached(*x):
        if not x in func_cache.keys():
            if len(func_cache) == cache_size:
                func_cache.popitem(False)
            func_cache[x] = func(*x)
        return func_cache[x]
    return func_cached