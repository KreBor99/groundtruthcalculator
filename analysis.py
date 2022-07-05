import csv
import math
import numpy as np

current_file = "/home/kre8or/PycharmProjects/Stargaze/recordings/today_06222022-155021_device_0.csv"


def get_csv_len():  # gets the length of the csv file since getting the length without a function moves through the file
    with open(current_file, 'r') as csv_file:
        # csv_reader = csv.reader(csv_file)
        return len(list(csv_file))

def set_csv_path(csv_name: str):
    global current_file
    current_file = csv_name

def get_csv_path():
    return current_file

def diff_points():  # function for telling fixation points from saccade points using the std of gaze vectors
    leng = get_csv_len()
    deltas = []
    temp = []
    deltasstd = []
    with open(current_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_contents = [_ for _ in csv_reader]
        if len(csv_contents) < 91:
            raise ValueError("CSV not long enough to process data.")
        for line in csv_contents[45:-45]:  # trimming first and last 45 lines
            temp.append(line)  # temp will be filled with first 5 points before calculations are done
            if int(line[0]) > 49 & int(line[0]) < leng - 50:
                currentdelta = math.sqrt(
                    ((float(line[11]) - float(temp[0][11])) * (float(line[11]) - float(temp[0][11]))) + (
                            float(line[12]) - float(temp[0][12])) * (float(line[12]) - float(temp[0][12])))
                deltas.append(
                    currentdelta)  # appends the distance between a point and 5 points behind it to the deltas
                temp.pop(0)
    temp = []
    for item in deltas[:-5]:
        temp.append(item)
        if temp.__len__() > 4:
            deltasstd.append(np.std(temp))
            temp.pop(0)
    stdstd = np.std(deltasstd)
    deltamedian = np.median(deltasstd)
    fixatedframes = []
    saccadeframes = []
    counter = 45
    for item in deltasstd:
        if item > (deltamedian + (2 * stdstd)):  # decides if a distance between two points is enough to be saccade
            saccadeframes.append(
                counter)  # saccade frames isn't actually ever used since if a line isn't in fixatedframes, it's known to be saccade
        else:  # the distance isn't great enough, then it gets its frame added to fixatedframes
            fixatedframes.append(counter)
        counter += 1
    print("The eyes are fixated in the following frames: ")
    print(fixatedframes)
    print("The eyes are in saccade in the following frames: ")
    print(saccadeframes)
    #print(identify_windows(fixatedframes))

def identify_windows(newarray):
    windowtimestamps = []
    windowid = 0
    with open(current_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_contents = [_ for _ in csv_reader]
        if len(csv_contents) < 91:
            raise ValueError("CSV not long enough to process data.")
    for line in csv_contents:
        if line[0] == 45:
            last = line
            line.append(windowid)
            continue
        if line[4] == last[4]:
            windowtimestamps.append(line[1])
            line.append(windowid)
            last = line
        else:
            print("Current window is this long:",
                  (windowtimestamps[windowtimestamps.__len__() - 1]) - windowtimestamps[0])
            windowtimestamps = []
            windowid = windowid + 1
            last = line
    return newarray
