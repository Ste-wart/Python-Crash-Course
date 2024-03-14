print('Hello World')


def success(persistence, dedication, passion):
    persistence += 1
    dedication += 1
    passion = True
    if passion:
        magic = persistence + dedication
        return magic
    else:
        magic = 0
        return magic


wow = success(20, 30, True)
print(wow)
