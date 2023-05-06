from matplotlib import pyplot as plt
from matplotlib import image as img

plt.title("Map")
plt.xlabel("West-East")
plt.ylabel("North-South")


def plotSensor(x, y):
    plt.plot(x, y, marker='x', color="black")


image = img.imread("Backend/Map1.png")
plotSensor(100, 100)
plt.imshow(image)
plt.show()
