from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Parameters for the Watson API
import config

base_url = config.base_url
api_key =  config.api_key

# Authentication
authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(base_url)
text_to_speech.set_default_headers({'x-watson-learning-opt-out': "true"})

#text_to_speech.set_disable_ssl_verification(True)
speaker = ['en-US_HenryV3Voice','en-US_KevinV3Voice','en-GB_JamesV3Voice','en-US_MichaelV2Voice']

for s in speaker:
    with open('output\linkedin_'+s+'.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                "Hi, I'm playing with the Watson Text to Speech service, and it's really incredible. Oh Yeah!",
                voice=s,
                accept='audio/wav'        
            ).get_result().content)

#try:
    # Invoke a method
#except ApiException as ex:
#    print "Method failed with status code " + str(ex.code) + ": " + ex.message

