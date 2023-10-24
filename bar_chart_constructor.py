import os
import pandas as pd
import matplotlib.pyplot as plt
import json

# cues up the file
file = open("transcript_json_2.json")

# this is a list
data = json.load(file)

# goal: break down the podcast into a bar chart where the independent variable is the speaker and the dependent variable is the word count

speakers_and_word_counts = {}

for utterance_object in data:

    # identify the speaker
    speaker = ""
    speaker_label = utterance_object["speaker"]

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

    if speaker_label == "A":
        speaker = "Interviewees"
    if speaker_label == "B":
        speaker = "Hosts"
    if speaker_label == "C":
        speaker = "Hosts"
    if speaker_label == "D":
        speaker = "Ads"
    if speaker_label == "E":
        speaker = "Reporters"
    if speaker_label == "F":
        speaker = "Reporters"
    if speaker_label == "G":
        speaker = "Reporters"
    if speaker_label == "H":
        speaker = "Interviewees"
    if speaker_label == "I":
        speaker = "Ads"
    if speaker_label == "J":
        speaker = "Ads"
    if speaker_label == "K":
        speaker = "Ads"
    
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
    y = 'values',
    title = 'NPR Up First 10/19/2023',
    xlabel = 'Word Count of Speaker',
    ylabel = 'Type of Speaker'
)

plt.show()
