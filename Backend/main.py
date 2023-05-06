from matplotlib import pyplot as plt
from matplotlib import image as img

plt.title("Map")
plt.xlabel("West-East")
plt.ylabel("North-South")
plotPoints = False #Should points be shown
plotNumbers = True #Should numbers be shown

#point 1-6 (index 0-5) is ~77km or ~606pixels
#77/606 ~= 0.127063 km/pixel
#point 1: (600, 620)
#point 6: (950, 125)

meteoriteLocation = (1000, 400)
sensorLocations = [(600, 620), (800, 250),
(180, 500), (400, 100), (575, 350), (950, 125), (50, 150)]
def plotSensor(i, x, y):
    if plotPoints: plt.plot(x, y, marker='x', color="black")
    if plotNumbers: plt.text(x-10, y+10, str(i), color='black')
                            #"+/-10" offsets the text so it's centered on the correct point

def plotSensorLocations():
    for i, pos in enumerate(sensorLocations):
        plotSensor(i+1, pos[0], pos[1])

def plotMeteorite(x,y):
    plt.plot(x,y, marker='x', color='r', markersize=12)

image = img.imread("./Map1.png")
plotSensorLocations()
plotMeteorite(meteoriteLocation[0], meteoriteLocation[1])
plt.imshow(image)
plt.show()
