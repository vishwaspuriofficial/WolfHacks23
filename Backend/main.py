from matplotlib import pyplot as plt
from matplotlib import image as img

plt.title("Map")
plt.xlabel("West-East")
plt.ylabel("North-South")
plotPoints = False #Should points be shown
plotNumbers = True #Should numbers be shown


sensorLocations = [(600, 620), (800, 250), (180, 500), (400, 100)]
def plotSensor(i, x, y):
    if plotPoints: plt.plot(x, y, marker='x', color="black")
    if plotNumbers: plt.text(x-10, y+10, str(i), color='r')

def plotSensorLocations():
    for i, pos in enumerate(sensorLocations):
        plotSensor(i+1, pos[0], pos[1])

image = img.imread("./Map1.png")
plotSensorLocations()

plt.imshow(image)
plt.show()
