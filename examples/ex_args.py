
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
# equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)
all_the_args(*args, **kwargs)

