import mincemeat

def ps1_map(k, v):
    words = v.split(" ")
    yield (words[0], words[2]), words[1]


def ps1_reduce(k, vs):
    return set(vs)


def ps2_map(k, v):
    import itertools
    sorted_words = list(v)
    sorted_words.sort()
    for pair in itertools.combinations(sorted_words, 2):
        yield pair, 1


def ps2_reduce(k, vs):
    return sum(vs)


def run():
    data = {}
    with open("pseudo_synonyms_input.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            data[idx] = line.strip()

    server = mincemeat.Server()
    server.mapfn = ps1_map
    server.reducefn = ps1_reduce
    server.datasource = data
    res1 = server.run_server(password="Password1")

    server.mapfn = ps2_map
    server.reducefn = ps2_reduce
    server.datasource = res1
    res2 = server.run_server(password="Password1")

    for key, val in res2.iteritems():
        if val > 1:
            print("%s - %s (%s)" % (key[0], key[1], val))
