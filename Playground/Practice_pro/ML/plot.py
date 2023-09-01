import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_clusters(media_usage, labels):
"""
This function plots the clusters for this exercise. This function is in a different file so that script.py is easier to read.
"""
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(111, projection='3d')

  xs = media_usage['Hours reading text']
  ys = media_usage['Hours watching video']
  zs = media_usage['Hours in VR']

  ax.scatter(xs, ys, zs, c=labels)
  ax.set_xlabel('Hours reading text')
  ax.set_ylabel('Hours watching video')
  ax.set_zlabel('Hours in VR')

  # Set the perspective so the clusters are easier to see
  ax.azim = 40
  ax.elev = 30

  plt.show()
return
