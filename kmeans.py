import mincemeat
import random

def map_kmeans(k, v):
    import math
    min_distance = float('Inf')
    centers = k[1]
    nearest_center = centers[0]
    for center in centers:
        distance = math.sqrt((center[0] - v[0]) ** 2 + (center[1] - v[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_center = center
    yield nearest_center, v

def reduce_kmeans(k, vs):
    xs = [v[0] for v in vs]
    ys = [v[1] for v in vs]
    mean = [float(sum(xs) / len(vs)), float(sum(ys) / len(vs))]
    return mean, vs

def run():
    data = {}
    centers = [round(random.uniform(0, 1), 2) for _ in range(3)]
    centers.sort()
    with open("kmeans_input.txt", "r") as f:
        lines = f.readlines()
        idx = 0
        for line in lines:
            data[(idx, centers)] = [float(a) for a in line.split(" ")]
            idx += 1

    while True:
        server = mincemeat.Server()
        server.mapfn = map_kmeans
        server.reducefn = reduce_kmeans
        server.datasource = data
        res = server.run_server(password="Password1")

        new_centers = res.keys()
        new_centers.sort()
        if new_centers == centers:
            print(res)
            break
        else:
            centers = new_centers
        points = [p for sublist in res.values() for p in sublist]
        idx = 0
        for p in points:
            data[(idx, centers)] = p
            idx += 1
