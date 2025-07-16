'''
    class Recorder
        属性：路径
        inner:
            1. 录制音频
                1.1 按住F键录制，释放后停止录制
            2. Save WAV file
                1.1 若音频文件不存在，保存文件
                1.2 若文件存在，覆盖文件
        outter:
            1. wav文件绝对路径
'''
import pyaudio
import wave

def start_audio(time = 8):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 16000
	RECORD_SECONDS = time  #需要录制的时间
	WAVE_OUTPUT_FILENAME = "/home/bigdata/PycharmProjects/pepper_chat/wav_file/output.wav"	#保存的文件名

	p = pyaudio.PyAudio()	#初始化
	print("Recording...")

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
		                frames_per_buffer=CHUNK)#创建录音文件
	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)#开始录音

	print("Record finished.")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')	#保存
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

# start_audio()
