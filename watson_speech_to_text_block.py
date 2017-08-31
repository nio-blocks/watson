from watson_developer_cloud import SpeechToTextV1, WatsonException

from nio.block.base import Block
from nio.signal.base import Signal
from nio.properties import (VersionProperty, ObjectProperty, FileProperty,
                            PropertyHolder, StringProperty)


class AuthCreds(PropertyHolder):
    username = StringProperty(title="Username", default="",
                              allow_none=False)
    password = StringProperty(title="Password", default="",
                              allow_none=False)


class WatsonSpeechToText(Block):

    version = VersionProperty('1.0.0')
    creds = ObjectProperty(AuthCreds, title="Bluemix Credentials",
                           default=AuthCreds())
    speech_file_location = FileProperty(title='Path to audio file (.wav)',
                                        default='etc/speech.wav',
                                        mode='rb')

    def __init__(self):
        self.stt_engine = None
        super().__init__()

    def configure(self, context):
        super().configure(context)
        self.stt_engine = SpeechToTextV1(username=self.creds().username(),
                                         password=self.creds().password())

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            try:
                with self.speech_file_location(signal) as speech_file:
                    speech_data = speech_file.read()
                    text_dict = self.stt_engine.recognize(
                        audio=speech_data, content_type='audio/wav')
            except WatsonException:
                self.logger.exception("Invalid Bluemix credentials: ")
            except Exception:
                self.logger.exception(
                    "Failed to open speech file: {}".format(
                        self.speech_file_location().file)
                )
            else:
                new_signals.append(Signal(text_dict))
                self.logger.debug("Successfully read speech file '{}'"
                                  .format(self.speech_file_location().file))
        self.notify_signals(new_signals)
