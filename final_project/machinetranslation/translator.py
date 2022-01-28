'''
    imprting the required modules
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


VERSION='2020-10-24'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """ function to translate english to french """
    if english_text is None or len(english_text)<1:
        return english_text
    translation_response = language_translator.translate(\
    text=english_text, model_id='en-fr')
    translation=translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """ function to translate french to english """
    if french_text is None or len(french_text)<1:
        return french_text
    translation_response = language_translator.translate(\
    text=french_text, model_id='fr-en')
    translation=translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
