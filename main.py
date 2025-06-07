import pvporcupine
import pyaudio
import struct
# import openai  # Uncomment later when adding AI response

porcupine = pvporcupine.create(
    access_key="jLdg8v42arQZ16gzuY3Ja4opPwcGC083XoqpCGGqujrtV0FNezRlWQ==",
    keywords=["over"]
)

# Initialize PyAudio
pa = pyaudio.PyAudio()
stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("🔊 Amiga VOX running → HAM MANUAL MODE → Waiting for trigger word: 'Over'...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("✅ HAM WORD DETECTED! → Processing buffer and sending to AI (Placeholder)...")
            # Placeholder for future Whisper + ChatGPT call
            print("**AI Response:** (This is a placeholder for now — real AI coming next phase)")
            print("🔄 Ready → Waiting for next 'Over'...")

except KeyboardInterrupt:
    print("\n🛑 Stopping Amiga VOX...")

finally:
    stream.stop_stream()
    stream.close()
    porcupine.delete()
    pa.terminate()
