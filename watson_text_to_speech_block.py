import uuid
from enum import Enum
from watson_developer_cloud import TextToSpeechV1

from nio.block.base import Block
from nio.properties import (VersionProperty, Property, FileProperty,
                            SelectProperty)


class Voices(Enum):
    enUSLisa = "en-US_LisaVoice"
    enUSMichael = "en-US_MichaelVoice"
    enUSAllison = "en-US_AllisonVoice"


class WatsonTextToSpeech(Block):

    version = VersionProperty('1.0.0')
    username = Property(title='Username', default='')
    password = Property(title='Password', default='')
    data_attr = Property(title='Text to Convert',
                         default='{{ $text }}')
    speech_file_location = FileProperty(title='Directory to save audio files',
                                        default='etc/')
    voice = SelectProperty(Voices, default=Voices.enUSLisa, title="Voice")

    def __init__(self):
        self.tts_engine = None
        super().__init__()

    def start(self):
        self.tts_engine = TextToSpeechV1(username=self.username(),
                                         password=self.password())
        super().start()

    def process_signals(self, signals):
        for signal in signals:
            try:
                filename = str(uuid.uuid4()) + ".wav"
                with open(self.speech_file_location() + filename, 'wb') as audio_file:
                    audio_file.write(
                        self.tts_engine.synthesize(
                            text=self.data_attr(signal),
                            voice=self.voice().value,
                            accept="audio/wav"))
            except Exception:
                self.logger.exception("Failed to write speech file: ")
            else:
                self.logger.info("Wrote speech file to {}")
