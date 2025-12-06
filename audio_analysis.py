import librosa
import numpy as np
import tempfile

def analyze_audio(audio_file):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(audio_file.read())
    temp.close()

    y, sr = librosa.load(temp.name)
    
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    energy = np.mean(np.abs(librosa.feature.rms(y=y)))
    pitch = np.mean(librosa.yin(y, 50, 300, sr=sr))

    delivery_score = int(min(100, (energy * 100) + (tempo/2)))

    delivery_summary = {
        "Pitch Stability": float(pitch),
        "Energy Level": float(energy),
        "Speaking Pace": float(tempo)
    }

    return delivery_score, delivery_summary
