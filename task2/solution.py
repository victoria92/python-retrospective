import collections


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
    func_copy = lambda *x: func(*x)
    func_copy.cache = collections.OrderedDict()

    def func_cached(*x):
        if not x in func_copy.cache.keys():
            if len(func_copy.cache) == cache_size:
                func_copy.cache.popitem(False)
            func_copy.cache[x] = func_copy(*x)
        return func_copy.cache[x]

    return func_cached