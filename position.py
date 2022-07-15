from datetime import datetime

position = {}

months = { "Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31 }

for month in months:
    position[month] = {}

    for day in range(months[month]):
        position[month][day+1] = {}

        for t in range(24):
            position[month][day+1][t] = {}

# ----- load data ----- #

position['Jan'][1][0] = { 'altitude': -62.27, 'bearing': 0 }
position['Jan'][1][1] = { 'altitude': -59.91, 'bearing': 28.37 }
position['Jan'][1][2] = { 'altitude': -53.81, 'bearing': 51.21 }
position['Jan'][1][3] = { 'altitude': -45.6, 'bearing': 68.47 }
position['Jan'][1][4] = { 'altitude': -36.42, 'bearing': 82.2 }
position['Jan'][1][5] = { 'altitude': -26.95, 'bearing': 94.03 }
position['Jan'][1][6] = { 'altitude': -17.6, 'bearing': 105.03 }
position['Jan'][1][7] = { 'altitude': -8.72, 'bearing': 115.89 }
position['Jan'][1][8] = { 'altitude': -0.63, 'bearing': 127.12 }
position['Jan'][1][9] = { 'altitude': 6.3, 'bearing': 139.08 }
position['Jan'][1][10] = { 'altitude': 11.68, 'bearing': 151.96 }
position['Jan'][1][11] = { 'altitude': 15.11, 'bearing': 165.71 }
position['Jan'][1][12] = { 'altitude': 16.29, 'bearing': 180 }
position['Jan'][1][13] = { 'altitude': 15.12, 'bearing': 194.29 }
position['Jan'][1][14] = { 'altitude': 11.69, 'bearing': 208.04 }
position['Jan'][1][15] = { 'altitude': 6.32, 'bearing': 220.93 }
position['Jan'][1][16] = { 'altitude': -0.6, 'bearing': 232.89 }
position['Jan'][1][17] = { 'altitude': -8.69, 'bearing': 244.13 }
position['Jan'][1][18] = { 'altitude': -17.57, 'bearing': 255 }
position['Jan'][1][19] = { 'altitude': -26.91, 'bearing': 266.01 }
position['Jan'][1][20] = { 'altitude': -36.38, 'bearing': 277.85 }
position['Jan'][1][21] = { 'altitude': -45.55, 'bearing': 291.59 }
position['Jan'][1][22] = { 'altitude': -53.75, 'bearing': 308.86 }
position['Jan'][1][23] = { 'altitude': -59.84, 'bearing': 331.68 }

currentHour = int(datetime.now().strftime("%H"))
altitude = position['Jan'][1][currentHour]['altitude']
bearing = position['Jan'][1][currentHour]['bearing']

if (altitude > 0):
    print ("altitude = " + str(altitude))
    print ("position = " + str(bearing))
