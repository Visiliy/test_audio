def audio_file(file_name, new_format):
    try:
        from pydub import AudioSegment

        file_name = str(file_name)

        audio_file, old_format = file_name.split(".")
        print(old_format)

        convert = AudioSegment.from_file(file_name)

        file_name = file_name.replace(old_format, new_format)

        convert.export(file_name, format=new_format)
    
    except Exception as error:
        print(f"\nError: {error}")


audio_file("audioToSave702314.wav", "opus")
print("OK")
