mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = 0
success_total = 0
b4_2000 = []

for name in mission_names:
    total_missions += 1

for success in mission_success:
    if success == True:
        success_total += 1
    else:
        pass

success_rate = success_total / total_missions * 100

for i in range(len(mission_years)):
    if mission_years[i] < 2000:
        b4_2000.append(mission_names[i])
#save it and apply it to the mission names list in order to present which missions were launched prior to 2000

print(f'There are {total_missions} mission names')
print(f"{success_total} of the missions were successful")
print('---')
print(f"Mission success rate: {success_rate:.2f}%")
print(f'Missions launched before the year 2000:')

for i in b4_2000:
    print(f'- {i}')