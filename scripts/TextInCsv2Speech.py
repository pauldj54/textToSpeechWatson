import csv
from email import charset

with open(r'C:\Users\p.hernandez\git\textToSpeechWatson\data\professornet-episode005.csv', newline='',  encoding="utf8") as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = list(reader)

# Parameters for the Watson API
import config

base_url = config.base_url
api_key =  config.api_key
output_folder = r'C:/Users/p.hernandez/git/textToSpeechWatson/output/episode005/'

# Authentication
from ibm_watson import TextToSpeechV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(base_url)
text_to_speech.set_default_headers({'x-watson-learning-opt-out': "true"})

#text_to_speech.set_disable_ssl_verification(True)
speaker = ['en-US_HenryV3Voice','en-US_KevinV3Voice','en-GB_JamesV3Voice','en-US_MichaelV2Voice']

for row in data:
    output_file = output_folder+ (row[0])
    print('Importing file: ' + row[0])
    print('Output folder: ' + output_file )
    with open(output_file +'.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                row[1],
                voice='en-GB_KateVoice',
                accept='audio/wav'        
            ).get_result().content)

#try:
    # Invoke a method
#except ApiException as ex:
#    print "Method failed with status code " + str(ex.code) + ": " + ex.message

