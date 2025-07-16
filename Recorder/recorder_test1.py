import pyaudio
import wave
import whisper
import numpy as np
import librosa  # 用来调整采样率
import threading

class Recorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []  # 用来存放音频数据
        self.recording = False  # 用于标记是否正在录音
        self.stream = None  # 用于存储音频流对象
        print("Loading Whisper model...")
        self.model = whisper.load_model("medium.en")  # 加载 Whisper 模型

    def start_recording(self):
        self.frames = []
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        self.recording = True
        print("Recording started...")

        def record():
            while self.recording:
                data = self.stream.read(1024)
                self.frames.append(data)

        # Use threading to continuously record audio in the background
        self.recording_thread = threading.Thread(target=record)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.recording_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        print("Recording stopped.")

    def save_audio_to_file(self, filename):
        # 将音频数据保存为 WAV 文件
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(16000)  # Whisper 模型通常使用 16kHz 采样率
            wf.writeframes(b''.join(self.frames))

    def transcribe_audio(self):
        # 将录制的音频数据转录为文本
        print("Transcribing audio...")
        audio_data = np.frombuffer(b''.join(self.frames), dtype=np.int16)
        audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max  # Normalize to float32

        # 使用 Whisper 模型进行转录
        result = self.model.transcribe(audio_data, fp16=False)  # Disable fp16 for CPU inference
        return result["text"]

if __name__ == "__main__":
    r = Recorder()

    while True:
        command = input("Press 'r' to start recording, 's' to stop and transcribe, or 'q' to quit: ")

        if command == 'r':
            r.start_recording()
        elif command == 's':
            r.stop_recording()
            r.save_audio_to_file("recorded_audio.wav")  # 保存音频文件
            transcription = r.transcribe_audio()  # Whisper 模型转录
            print("Transcription:", transcription)
        elif command == 'q':
            break
