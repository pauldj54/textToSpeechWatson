# Parameters for the Watson API
import config

base_url = config.base_url
api_key =  config.api_key

# Authentication
from ibm_watson import TextToSpeechV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(base_url)
text_to_speech.set_default_headers({'x-watson-learning-opt-out': "true"})

#text_to_speech.set_disable_ssl_verification(True)

voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=2))

#try:
    # Invoke a method
#except ApiException as ex:
#    print "Method failed with status code " + str(ex.code) + ": " + ex.message

