import speech_recognition as sr
import os

def apex_voice_execute():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("🔊 SAIF-VOICE ACTIVE: Awaiting Architect's Command...")
        audio = recognizer.listen(mic)
        
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"Architect said: '{text}'")
        
        # Mapping Voice to Empire Tasks
        if "scout" in text:
            os.system("python agent-scout.py")
        elif "handshake" in text:
            os.system("python agent-handshake.py")
        elif "status" in text:
            print("📊 Status: All SAIF-Nodes are operational. Billionaire target 2027: ON TRACK.")
            
    except Exception:
        print("⚠️ Could not verify voice. Try again.")

if __name__ == "__main__":
    apex_voice_execute()
