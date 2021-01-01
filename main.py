from kmeans import Clusters
from random import random
import matplotlib.pyplot as plt

dataset = [(num * random(), num * random()) for num in range(100)]
group = Clusters(cluster_count=4, dataset=dataset)
group.run()

fig = plt.figure("k-means with random dataset")
graph = fig.add_subplot(1, 1, 1)

for point in dataset:
    graph.plot(point[0], point[1], "ro", color="green")
for cluster in group.clusters:
    graph.plot(cluster.location[0], cluster.location[1], "ro")

graph.set_title("normal k-means")
graph.set_xlabel('x (randomly generated)')
graph.set_ylabel('y (randomly generated)')

plt.show()
# we can see that the normal k-means does a poor job at finding the global minimum
