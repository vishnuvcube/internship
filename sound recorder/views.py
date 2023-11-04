import sounddevice
import numpy as np
from scipy.io import wavfile
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import os

def recorder(request):
    if request.method == 'POST':
        sec = request.POST.get('sec')
        try:
            sec = int(sec)
            if sec <= 0:
                raise ValueError("Invalid time")
        except ValueError:
            return render(request, 'recorder/recorder.html', {'error_message': 'Invalid time value'})

        # Record audio
        sample_rate = 44100
        duration = sec
        recording = sounddevice.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
        sounddevice.wait()

        # Save the recording to a file
        filename = os.path.join('media', 'demo.wav')  # Save in the 'media' folder
        wavfile.write(filename, sample_rate, (np.array(recording) * 32767).astype(np.int16))

        # Provide the file path in the response context
        file_path = os.path.abspath(filename)

        return render(request, 'recorder/recorder.html', {'file_path': file_path})

    return render(request, 'recorder/recorder.html')
