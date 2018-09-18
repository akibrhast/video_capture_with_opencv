import sounddevice as sd
import soundfile as sf
import numpy as np
import datetime
from constants import *

start=datetime.datetime.now()

if not os.path.isdir(AUDIO_DICECTORY_PATH):
	os.mkdir(AUDIO_DICECTORY_PATH)

sd.default.samplerate = AUDIO_FS
sd.default.channels = AUDIO_CHANNELS
recording = sd.rec(int(AUDIO_LENGTH_SECONDS * AUDIO_FS))
sd.wait()
sf.write('%s/%s.wav' % (AUDIO_DICECTORY_PATH, start.strftime("%y-%m-%d-%H-%M-%S")), recording, AUDIO_FS)
