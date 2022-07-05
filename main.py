'''import math
import analysis


def calc_locations(position):
    temp = original
    if position == 1:  # performs translation for if camera is at bottom of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - monitor[0] / 2)
            temp[i][1] = -1 * (original[i][1] + 5)

    if position == 2:  # performs translation for if camera is at top of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - monitor[0] / 2)
            temp[i][1] = (monitor[1] + 5.5 - original[i][1])

    if position == 3:  # performs translation for if camera is at left of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] + 2.8)
            temp[i][1] = -1 * (original[i][1] - monitor[1] / 2)

    if position == 4:  # performs translation for if camera is at right of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - 63)
            temp[i][1] = -1 * (original[i][1] - monitor[1] / 2)
    return calc_truths(temp)
    return temp


def calc_truths(position):  # returns an array of distances from the subject to A-E
    truths = []
    for i in iterate:
        xgaze = math.asin(math.sqrt((position[5][0] - position[i][0]) ** 2) / math.sqrt(
            ((position[5][0] - position[i][0]) ** 2) + (position[5][2] ** 2)))
        ygaze = math.asin(math.sqrt((position[5][1] - position[i][1]) ** 2) / math.sqrt(
            ((position[5][1] - position[i][1]) ** 2) + (position[5][2] ** 2)))
        if i == 0:
            ygaze = ygaze * -1
        if i == 1:
            xgaze = xgaze * -1
            ygaze = ygaze * -1
        if i == 2:
            xgaze = xgaze * -1
        truths.append([xgaze, ygaze])
    return truths



monitor = [53, 30]
original = [[5.6, 24.3], [47.7, 24.3], [47.7, 5.5], [5.6, 5.5], [26.65, 13]]
iterate = [0, 1, 2, 3, 4, 5]
print(original)
position = float(input("Please choose a camera location:\n1. Bottom\n2. Top\n3. Left\n4. Right\n"))
distance = float(input("Please enter the distance from camera\n"))
original.append([monitor[0] / 2, monitor[1] / 2, distance])
print(original)
# print(calc_truths(position, distance))
print(calc_locations(original))
'''
import math
import analysis
import plotter

def calc_locations(
        position):  # new locations of points and user are found, then passed to calc_truths to get angles
    temp = original
    if position == 1:  # performs translation for if camera is at bottom of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - monitor[0] / 2)
            temp[i][1] = -1 * (original[i][1] + 5)

    if position == 2:  # performs translation for if camera is at top of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - monitor[0] / 2)
            temp[i][1] = (monitor[1] + 5.5 - original[i][1])

    if position == 3:  # performs translation for if camera is at left of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] + 2.8)
            temp[i][1] = -1 * (original[i][1] - monitor[1] / 2)

    if position == 4:  # performs translation for if camera is at right of screen
        for i in iterate:
            temp[i][0] = -1 * (original[i][0] - 63)
            temp[i][1] = -1 * (original[i][1] - monitor[1] / 2)
    return calc_motion_truths(temp)
    # return calc_truths(temp)

def calc_motion_truths(position):
    truths= []
    speed




def calc_truths(position):  # returns an array of X, Y gaze pairs for the user looking at each point A-E, with the last entry being the user's location
    truths = []
    for i in iterate:  # calculates the xgaze and ygaze of the user for each of the points A-E
        xgaze = math.atan((position[4][0]-position[i][0])/position[5][2])
        ygaze = math.atan((position[4][1]-position[i][1])/position[5][2])
        truths.append([xgaze, ygaze])
    return truths  # what is returned is an array of pairs corresponding to each point's xgaze and ygaze


current_file = "/home/kre8or/PycharmProjects/Stargaze/recordings/today_06222022-155021_device_0.csv"
monitor = [53, 30]  # dimensions of the monitor in cm
original = [[5.6, 24.3], [47.7, 24.3], [47.7, 5.5], [5.6, 5.5],
            [26.65, 13]]  # locations of A-E in cm from bottom left of monitor
iterate = [0, 1, 2, 3, 4, 5]  # used to iterate in for loops
position = float(input(
    "Please choose a camera location:\n1. Bottom\n2. Top\n3. Left\n4. Right\n"))  # used to determine what translation of the points will be done
distance = float(input("Please enter the distance from camera\n"))
speed = float(input("Please enter the speed at which the dot is traveling across the screen(12, 8, or 4)"))
fps = float(input("Please enter the frames per second for the recording session()"))
original.append([monitor[0] / 2, monitor[1] / 2, distance])  # appends the location of the user
#analysis.diff_points()
#print("The xgaze, ygaze pairs for each point on screen are as follows: ")
#print(calc_locations(original))
print(calc_motion_truths(position))