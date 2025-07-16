from ASR.ASR_component import ASRService
from LLM.LLM_component_test import LLMService
from utils.connection import PepperConnection

def main():
    # ip_address = "192.168.26.106"
    # pepper_connection = PepperConnection()
    # session = pepper_connection.connect_to_robot_ip(ip_address)

    asr_service = ASRService()
    # llama_service = LLMService()

    # tts = session.service("ALTextToSpeech")
    # tts.setLanguage("English")

    try:
        while True:
            command = input("Enter command ('f': start recording, 's': stop recording and transcribe, 'q': quit): ")

            if command == 'q':
                # tts.say("Goodbye!")
                break

            if command == 'f':
                asr_service.start_recording()
                print("Listening...")

            elif command == 's':
                asr_service.stop_recording()
                transcribed_text = asr_service.audio_to_text()
                print(f"User: {transcribed_text}")

                # if transcribed_text:
                    # response = llama_service.ask_llama(transcribed_text)
                    # print(f"Pepper: {response}")
                    # tts.say(response)
            else:
                print("Unknown command, please try again.")
    finally:
        asr_service.close()

if __name__ == "__main__":
    main()

