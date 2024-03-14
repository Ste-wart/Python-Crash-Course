def make_great():
    names = []
    for name in magicians:
        names.append('Great ' + name)
    return names


def show_magicians():
    print(magicians)
    name_lists = make_great()
    print(name_lists)
    # for name in name_lists:
    #     print(name)


magicians = ['John', 'Mike', 'Paul', 'Rudd', 'Joe']
show_magicians()
