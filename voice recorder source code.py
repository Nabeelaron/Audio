import matplotlib.pyplot as plt 
import pyaudio
import wave

FRAME_PER_BUFFER = 2048
SAMPLING_RATE = 44100
DURATION = 5
FORMAT = pyaudio.paInt32
CHANNEL = 2

audio_object = pyaudio.PyAudio()
stream_input = audio_object.open( format = FORMAT,
								channels = CHANNEL,
								rate = SAMPLING_RATE,
								frames_per_buffer = FRAME_PER_BUFFER,
								input = True,
								stream_callback = None
								)
frames = []

for i in range(0, int(( DURATION * SAMPLING_RATE )/ FRAME_PER_BUFFER) ):
	data = stream_input.read(FRAME_PER_BUFFER)
	frames.append( data )


stream_input.stop_stream()
stream_input.close()
audio_object.terminate()


# print(frames[1][:10])
# print ("in ASCII format : " )
# values = map(ord , str(frames[1][:10]) )
# print( list(values) )

# saving file
wave_file_object = wave.open("blocking.wave","wb")
wave_file_object.setnchannels(CHANNEL)
wave_file_object.setframerate(SAMPLING_RATE)
wave_file_object.setsampwidth(audio_object.get_sample_size(FORMAT))
wave_file_object.writeframes(b''.join(frames))
wave_file_object.close()