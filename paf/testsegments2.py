import numpy as np
import opensmile
import numpy as np
from pydub import AudioSegment
import pympi.Elan as elan

from pympi import Eaf

def extract_segments(interaction):
    audio_file = "C:\\Users\\lisar\\Downloads\\PAF_2023\\PAF_2023\\Dataset\\Interactions\\"+str(interaction)+"\\person1.wav"
    elan_file = "C:\\Users\\lisar\\Downloads\\PAF_2023\\PAF_2023\\Dataset\\Interactions\\"+str(interaction)+"\\"+str(interaction)+".eaf"
    eaf = Eaf(elan_file)
    annotations = eaf.get_annotation_data_for_tier("Trust")
    audio = AudioSegment.from_file(audio_file)

    for i, annotation in enumerate(annotations):
        start_time = annotation[0]
        end_time = annotation[1]
        segment_audio = audio[start_time:end_time]

        # Sauvegarder le segment audio dans un fichier
        segment_audio.export("C:\\Users\\lisar\\Documents\\paf\\"+str(interaction)+"\\segment_"+str(i)+".wav", format="wav")
for interaction in [9,10,12,15,18,19,24,26,27,30]:
    extract_segments(interaction)


def getData(interaction, segment) :
    
    smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

# on récupère le segment 
    audio_file = "C:\\Users\\lisar\\Documents\\paf\\"+str(interaction)+"\\segment_"+str(segment)+".wav"
#fonctionnalités qu'on veut extraire 
    smile.feature_names = [
    "frameIndex",
    "F0semitoneFrom27.5Hz_sma3nz_mean",
    "F0semitoneFrom27.5Hz_sma3nz_stddev",
    "F0semitoneFrom27.5Hz_sma3nz_minimum",
    "F0semitoneFrom27.5Hz_sma3nz_maximum",
    "F0semitoneFrom27.5Hz_sma3nz_range",
    "voiceProb_sma3nz_mean",
    "pcm_LOGenergy_sma3nz_mean",
    "pcm_fftMag_fband250-650_sma3_stddev",
    "pcm_zcr_sma3_stddev",
    "pcm_fftMag_spectralRollOff25.0_sma3_stddev",
    "pcm_fftMag_spectralCentroid_sma3_stddev",
]

    features = smile.process_file(audio_file) 
    return features; 

for interaction in [9,10,12,15,18,19,24,26,27,30]:
    file ="C://Users//lisar//Documents//PAF//PAF_2023//Dataset//Interactions//"+str(interaction)+"//"+str(interaction)+".eaf"
    eaf = pympi.Elan.Eaf(file)
    annots = sorted(eaf.get_annotation_data_for_tier('Trust'))
    num_segment=0
    for segment in annots:
        saved_file="C://Users//lisar//Documents//paf//Data_prosodie//"+str(interaction)+"//segment_"+str(num_segment)
        data = getData(interaction, num_segment)
        np.save(saved_file, data)

        num_segment+=1