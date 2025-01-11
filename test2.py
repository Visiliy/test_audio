from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

import json

AUDIO_FILE = "audioToSave702314.wav"


def main():
    try:
        deepgram = DeepgramClient("50a062200dc80b224f63d15175a7b8bb6e10e395")

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language="ru",
        )

        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)

        print(json.loads(response.to_json(indent=4))["results"]["channels"][0]["alternatives"][0]["transcript"])

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()