# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai
import requests
import json
import time
import os

base_url = "https://api.assemblyai.com/v2"
api_key = os.environ.get("ASSEMBLY_AI_KEY", "API_KEY")

headers = {
    "authorization": api_key
}

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'
with open("./NPR1839466774.mp3", "rb") as f:
    response = requests.post(
        f"{base_url}/upload",
        headers=headers,
        data=f
    )

upload_url = response.json()["upload_url"]

data = {
    "audio_url": upload_url,
    "speaker_labels": True
}

upload_url = response.json()["upload_url"]

url = f"{base_url}/transcript"
response = requests.post(url, json=data, headers=headers)

transcript_id = response.json()['id']
polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

while True:
    transcription_result = requests.get(polling_endpoint, headers=headers).json()

    if transcription_result['status'] == 'completed':
        # when the transcript is complete, extract all utterances from the response
        transcript_text = transcription_result['text']
        utterances = transcription_result['utterances']

        f = open('transcript_json.py', 'w')
        f. write(f"utterance_variable={utterances}")
        # print(utterances)

        # For each utterance, print its speaker and what was said
        for utterance in utterances:
            speaker = utterance['speaker']
            text = utterance['text']
            print(f"Speaker {speaker}: {text}")

        break

    elif transcription_result['status'] == 'error':
        raise RuntimeError(
            f"Transcription failed: {transcription_result['error']}")

    else:
        time.sleep(3)
