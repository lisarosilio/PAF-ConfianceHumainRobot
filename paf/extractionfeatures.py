import opensmile
import csv

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

# Chemin vers le fichier audio que vous souhaitez traiter
audio_file = "C:\\Users\\lisar\\Downloads\\PAF_2023\\PAF_2023\\Dataset\\Interactions\\9\\person1.wav"

# Définir les noms des fonctionnalités que vous souhaitez extraire
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


# Extraire les fonctionnalités spécifiées à partir du fichier audio
features = smile.process_file(audio_file)
# Chemin vers le fichier CSV de sortie
output_file = "C:\\Users\\lisar\\Documents\\paf.csv"

# Écrire les fonctionnalités extraites dans le fichier CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Écrire l'en-tête (noms des fonctionnalités)
    writer.writerow(features.columns)

    # Écrire les valeurs des fonctionnalités
    writer.writerows(features.values)

print("Extraction terminée. Les résultats ont été enregistrés dans le fichier CSV.")
