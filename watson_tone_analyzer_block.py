from watson_developer_cloud import ToneAnalyzerV3

from nio.block.base import Block
from nio.properties import (VersionProperty, Property, PropertyHolder,
                            StringProperty, ObjectProperty)
from nio.signal.base import Signal


class AuthCreds(PropertyHolder):
    username = StringProperty(title="Username", default="",
                              allow_none=False)
    password = StringProperty(title="Password", default="",
                              allow_none=False)


class WatsonToneAnalyzer(Block):

    version = VersionProperty('1.0.0')
    creds = ObjectProperty(AuthCreds, title="Bluemix Credentials",
                           default=AuthCreds())
    data_attr = Property(title='Data Field',
                         default='{{ $text }}')

    def __init__(self):
        self.tone_analyzer = None
        super().__init__()

    def configure(self, context):
        super().configure(context)
        self.tone_analyzer = ToneAnalyzerV3(username=self.creds().username(),
                                            password=self.creds().password(),
                                            version='2016-05-19')

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            new_signals.append(
                Signal(self.tone_analyzer.tone(self.data_attr(signal))))
        self.notify_signals(new_signals)
