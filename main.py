from kmeans import Clusters
from random import random
import matplotlib.pyplot as plt

dataset = [(num * random(), num * random()) for num in range(100)]
group = Clusters(cluster_count=5, dataset=dataset)
group.run()

for point in dataset:
    plt.plot(point[0], point[1], "ro", color="green")
for cluster in group.clusters:
    plt.plot(cluster.location[0], cluster.location[1], "ro")
plt.show()
# we can see that the normal k-means does a poor job at finding the global minimum