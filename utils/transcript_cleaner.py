# goal: import a local json file (take it as an argument) and reconstruct it without the "words" key and value pair for each object in the json list.

import json

def transcript_cleaner(original_json_file, month_day_year):

    cleaned_file = []

    with open(original_json_file, 'r') as input_file:

        json_string = input_file.read()

        # this becomes a list
        data_dict = json.loads(json_string)
        
        # each utterance is a dict
        for utterance in data_dict:

            new_utterance_object = {}

            for key, value in utterance.items():
                if key != "words":
                    new_utterance_object[key] = value
                
            cleaned_file.append(new_utterance_object)
        
    with open(f'./transcripts/{month_day_year}/cleaned_{month_day_year}_transcript.json', 'w') as outfile:
        json.dump(cleaned_file, outfile, indent=4)
                