import mincemeat


def clique_map(k, v):
    for vertex in set(v):
        if vertex != k:
            yield k, 1


def clique_reduce(k, vs):
    return sum(vs)


def run():
    data = {}
    with open("check_clique_input.txt", "r") as f:
        for line in f.readlines():
            temp = line.split(" -> ")
            data[temp[0].strip()] = temp[1].strip().split(" ")

    server = mincemeat.Server()
    server.mapfn = clique_map
    server.reducefn = clique_reduce
    server.datasource = data
    res = server.run_server(password="Password1")

    edge_lists_len = res.values()
    vertex_num = len(set(res.keys()))
    print("YES" if len(set(edge_lists_len)) == 1 and edge_lists_len[0] == vertex_num - 1 else "NO")
