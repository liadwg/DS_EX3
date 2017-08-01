import mincemeat
import random

def map_kmeans(k, vs):
    import math
    min_distance = float('Inf')
    for center in vs:
        distance = math.sqrt((center[0] - k[0]) ** 2 + (center[1] - k[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_center = center
    yield nearest_center, k

def reduce_kmeans(k, vs):
    xs = [v[0] for v in vs]
    ys = [v[1] for v in vs]
    mean = (round(float(sum(xs) / len(vs)), 2), round(float(sum(ys) / len(vs)), 2))
    return mean, vs

def run():
    data = {}
    k = 3
    centers = [(round(random.uniform(0, 1), 2), round(random.uniform(0, 1), 2)) for _ in range(k)]
    centers.sort()
    with open("kmeans_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data[tuple([float(a) for a in line.split(" ")])] = centers
    while True:
        points = data.keys()
        server = mincemeat.Server()
        server.mapfn = map_kmeans
        server.reducefn = reduce_kmeans
        server.datasource = data
        res = server.run_server(password="Password1")
        new_centers = [a[0] for a in res.values()]
        new_centers.sort()
        if new_centers == centers:
            for cluster in res.values():
                for p in cluster[1]:
                    print("(%s %s)\t(%s %s)" % (p[0], p[1], cluster[0][0], cluster[0][1]))
            break
        else:
            centers = new_centers
        for p in points:
            data[p] = centers

run()