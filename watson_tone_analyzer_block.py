from watson_developer_cloud import ToneAnalyzerV3

from nio.block.base import Block
from nio.properties import (VersionProperty, Property, PropertyHolder,
                            StringProperty, ObjectProperty)
from nio.block.mixins.enrich.enrich_signals import EnrichSignals


class AuthCreds(PropertyHolder):
    username = StringProperty(title="Username", default="",
                              allow_none=False)
    password = StringProperty(title="Password", default="",
                              allow_none=False)


class WatsonToneAnalyzer(EnrichSignals, Block):

    version = VersionProperty("1.0.0")
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
                                            version='2017-09-21')

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            out_sig = self.get_output_signal(
                self.tone_analyzer.tone_chat(self.data_attr(signal)), signal)
            new_signals.append(out_sig)
        self.notify_signals(new_signals)
