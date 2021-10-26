import pandas as pd

df = pd.read_csv("final.csv") 

print("How affectionate with family (1 independent, 5 lovey-dovey)")
affectionate_with_family = input()
print("How good with young children (1 not recommended 5 good with children")
good_with_children = input()
print("How good with other dogs (1 not recommended 5 good with other dogs)")
good_with_other_dogs = input()
print("Shedding level (1 no shedding 5 hair everywhere)")
shedding_level = input()
print("Coat grooming frequency (1 monthly 5 daily)")
coat_grooming_frequency = input()
print("Drooling level (1 less likely to drool 5 always have a towel)")
drooling_level = input()
print("Openness to Strangers (1 reserved 5 everyone is my best friend)")
openness_to_strangers = input()
print("Playfulness Level (1 only when you want to play 5 non-stop)")
playfulness_level = input()
print("Watchdog/Protective Nature(1 what's mine is yours 5 vigilant)")
watchdog_nature = input()
print("Adaptability Level (1 lives for routing 5 highly adaptible)")
adaptability_level = input()
print("Trainability Level (1 self willed 5 eager to please)")
trainability_level = input()
print("Energy Level (1 couch potato 5 high energy)")
energy_level = input()
print("Barking Level (1 only to alert 5 very vocal)")
barking_level = input()
print("Mental Stimulation Needs (1 happy to lounge 5 needs a job or activity)")
mental_stimulation_needs = input()
print("Coat Length (1 short 3 long)")
coat_length = input()


affectionate_diff = []
good_with_children_diff = []
good_with_dogs_diff = []
shedding_level_diff = []
coat_grooming_diff = []
drooling_diff = []
openness_diff = []
playfulness_diff = []
watchdog_diff = []
adaptability_diff = []
trainability_diff = []
energy_diff = []
barking_diff = []
mental_diff = []
# coat_length_diff = []

# for i in df["Affectionate With Family"]:
#     print(i)

# print(df.columns.values)
for i in df["Affectionate With Family"]:
    affectionate_diff.append(abs(int(affectionate_with_family) - i))
for i in df["Good With Young Children"]:
    good_with_children_diff.append(abs(int(good_with_children) - i))
for i in df["Good With Other Dogs"]:
    good_with_dogs_diff.append(abs(int(good_with_other_dogs) - i))
for i in df["Shedding Level"]:
    shedding_level_diff.append(abs(int(shedding_level) - i))
for i in df["Coat Grooming Frequency"]:
    coat_grooming_diff.append(abs(int(coat_grooming_frequency) - i))
for i in df["Drooling Level"]:
    drooling_diff.append(abs(int(drooling_level) - i))
for i in df["Openness to Strangers"]:
    openness_diff.append(abs(int(openness_to_strangers) - i))
for i in df["Playfulness Level"]:
    playfulness_diff.append(abs(int(playfulness_level) - i))
for i in df["Watchdog/Protective Nature"]:
    watchdog_diff.append(abs(int(watchdog_nature) - i))
for i in df["Adaptability Level"]:
    adaptability_diff.append(abs(int(adaptability_level) - i))
for i in df["Trainability Level"]:
    trainability_diff.append(abs(int(trainability_level) - i))
for i in df["Energy Level"]:
    energy_diff.append(abs(int(energy_level) - i))
for i in df["Barking Level"]:
    barking_diff.append(abs(int(barking_level) - i))
for i in df["Mental Stimulation Needs"]:
    mental_diff.append(abs(int(mental_stimulation_needs) - i))
# for i in df["Coat Length "]:
#     coat_length_diff.append(abs(int(coat_length) - i))



total_diff = []

data = {
    'Affectionate With Family' : affectionate_diff,
    'Good With Young Children' : good_with_children_diff,
    'Good With Other Dogs' : good_with_dogs_diff, 
    'Shedding Level' : shedding_level_diff,
    'Coat Grooming Frequency' : coat_grooming_diff,
    'Drooling Level' : drooling_diff,
    'Openness to Strangers' : openness_diff,
    'Playfulness Level' : playfulness_diff,
    'Watchdog/Protective Nature' : watchdog_diff,
    'Adaptability Level' : adaptability_diff,
    'Trainability Level' : trainability_diff,
    'Energy Level' : energy_diff,
    'Barking Level' : barking_diff,
    'Mental Stimulation Needs' : mental_diff,
    
}

data_df = pd.DataFrame(data, index=df["Breed"])
# data_df['total_value'] = df["Affectionate With Family", "Good With Young Children"](axis=1)


print(data_df.head())

