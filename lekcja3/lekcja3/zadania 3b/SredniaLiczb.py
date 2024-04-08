def arytmetyczna(*args):
    if not args:
        return "args ERROR"
    else:
        return sum(args) / len(args)
