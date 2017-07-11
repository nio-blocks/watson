import json

from watson_developer_cloud import SpeechToTextV1

from nio.block.base import Block
from nio.properties import VersionProperty, Property, FileProperty


class WatsonSpeechToText(Block):

    version = VersionProperty('1.0.0')
    username = Property(title='Username', default='')
    password = Property(title='Password', default='')
    speech_file_location = FileProperty(title='Path to audio file',
                                        default='etc/speech.wav')

    def __init__(self):
        self.stt_engine = None
        super().__init__()

    def start(self):
        self.stt_engine = SpeechToTextV1(username=self.username(),
                                         password=self.password())
        super().start()

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            try:
                with open(self.speech_file_location(), 'rb') as speech_file:
                    speech_data = speech_file.read()
                    text_dict = self.stt_engine.recognize(audio=speech_data,
                                              content_type='audio/wav')
            except Exception:
                self.logger.exception("Failed to open speech file: ")
            else:
                self.logger.debug("Successfully read speech file {}"
                                  .format(self.speech_file_location()))
        self.notify_signals(new_signals)
