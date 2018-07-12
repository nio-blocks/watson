import uuid
from enum import Enum
from watson_developer_cloud import TextToSpeechV1, WatsonException

from nio import TerminatorBlock
from nio.properties import (VersionProperty, Property, FileProperty,
                            SelectProperty, PropertyHolder, StringProperty,
                            ObjectProperty)


class Voices(Enum):
    EnglishUSLisa = "en-US_LisaVoice"
    EnglishUSMichael = "en-US_MichaelVoice"
    EnglishUSAllison = "en-US_AllisonVoice"


class AuthCreds(PropertyHolder):
    username = StringProperty(title="Username", default="",
                              allow_none=False,
                              order=0)
    password = StringProperty(title="Password", default="",
                              allow_none=False,
                              order=1)


class WatsonTextToSpeech(TerminatorBlock):

    version = VersionProperty("1.0.0")
    creds = ObjectProperty(AuthCreds, title="Bluemix Credentials",
                           default=AuthCreds())
    data_attr = Property(title='Text to Convert',
                         default='{{ $text }}')
    speech_file_location = FileProperty(title='Directory to save audio files',
                                        default='etc/')
    voice = SelectProperty(Voices, default=Voices.EnglishUSLisa, title="Voice")

    def __init__(self):
        self.tts_engine = None
        super().__init__()

    def configure(self, context):
        super().configure(context)
        self.tts_engine = TextToSpeechV1(username=self.creds().username(),
                                         password=self.creds().password())

    def process_signals(self, signals):
        for signal in signals:
            try:
                data = self.tts_engine.synthesize(text=self.data_attr(signal),
                                                  voice=self.voice().value,
                                                  accept="audio/wav")
            except WatsonException:
                self.logger.exception("Invalid Bluemix credentials: ")
            else:
                filename = str(uuid.uuid4()) + ".wav"
                with open(self.speech_file_location().value + filename, 'wb') \
                        as audio_file:
                    audio_file.write(data)
                self.logger.info(
                    "Wrote speech file to {} for input text "
                    "starting with '{}'".format(
                        self.speech_file_location.value + filename,
                        self.data_attr(signal)[:30])
                )
