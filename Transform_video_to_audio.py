# define a new function and its parameters are the path of input and output materials


def convert_video(video, speech_file):

    FFMPEG_BIN = "C:/ffmpeg/bin/ffmpeg.exe"
    import subprocess as sp
    command = [ FFMPEG_BIN,
                "-i", video,  # input path
                "-f", "wav",  # format
                "-vn",  # disable video recording
                "-ar", "44100",  # sets the sampling rate for audio streams
                "-ac", "1",  # set the number of audio channels
                "-acodec", "pcm_s16le",
                "-b:a", "128k",  # set the audio bit
                speech_file ]  # output path
    sp.Popen(command)


# test new function
convert_video("C:/Users/taotao/Desktop/research/test/HHcut.mp4","C:/Users/taotao/Desktop/research/test/HHcut.wav")

