# use the package speech_recognition
import speech_recognition as sr

# define the function and the parameter audio_input means the path of the audio and the txt_output means the path and the name of your output file
def recognize_speech(audio_input,txt_output):
    r = sr.Recognizer()
    beginner = sr.AudioFile(audio_input)
    with beginner as source:
        audio = r.record(source)
        # use Google Web Speech API
        txt = r.recognize_google(audio)
        # store the result in a txt file
        if str is bytes:
            result = u"{}".format(txt).encode("utf-8")
        else:
            result = "{}".format(txt)

        with open(txt_output, "a") as f:
            f.write(result)
        print(result)

# test this function
recognize_speech("C:/Users/taotao/Desktop/research/OSR_us_000_0010_8k.wav","C:/Users/taotao/Desktop/research/OSR_us_000_0010_8k.txt")