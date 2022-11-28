import csv
from email import charset

with open('c:/Users/pauld/git/textToSpeechWatson/data/professornet-episode002-02.csv', newline='',  encoding="utf8") as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = list(reader)

# Parameters for the Watson API
import config

base_url = config.base_url
api_key =  config.api_key

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
    print('Importing file: ' + row[0].replace(':','-'))
    print('output\episode002\\'+ (row[0]).replace(':','-').replace('"','')+'.wav')
    with open('output\episode002\corrections\\' + (row[0]).replace(':','-').replace('"','')+'.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                row[1],
                voice='en-US_KevinV3Voice',
                accept='audio/wav'        
            ).get_result().content)

#try:
    # Invoke a method
#except ApiException as ex:
#    print "Method failed with status code " + str(ex.code) + ": " + ex.message

