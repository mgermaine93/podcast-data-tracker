import os
import pandas as pd
import matplotlib.pyplot as plt
import json

file = open("transcript_json_2.json")

# this is a list
data = json.load(file)

# goal: break down the podcast into a bar chart where the independent variable is the speaker and the dependent variable is the word count

speakers_and_word_counts = {}

for utterance_object in data:
    # identify the speaker
    speaker = utterance_object["speaker"]
    text = utterance_object["text"]

    if speaker not in speakers_and_word_counts:
        speakers_and_word_counts[speaker] = 0
    
    speaker_word_count = len(text.split())
    speakers_and_word_counts[speaker] += speaker_word_count

print(speakers_and_word_counts)

speaker_labels = speakers_and_word_counts.keys()
word_count_labels = speakers_and_word_counts.values()

df = pd.DataFrame({
    'labels': speaker_labels,
    'values': word_count_labels
})

ax = df.plot.barh(
    x = 'labels',
    y = 'values'
)

plt.show()

# A is Biden (quote)
# B is Michelle Martin
# C is A Martinez
# D is sponsor
# E is Zaya Batrawi (reporter)
# F is Greg Myri
# G is Deirdre Walsh
# H is Patrick McHenry (quote)
# I is Deepa Fernandez
# J is a sponsor
# K is Danielle Alarcon




# df = pd.DataFrame.from_dict(data)

# # goal: break down the podcast into a bar chart where the independent variable is the speaker and the dependent variable is the word count


# speakers = df.groupby("speaker")
# chart = df.plot.barh(x='speaker',y=)