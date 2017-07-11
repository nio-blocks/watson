from nio.block.base import Block
from nio.properties import VersionProperty, Property
from nio.signal.base import Signal
from watson_developer_cloud import ToneAnalyzerV3


class WatsonToneAnalyzer(Block):

    version = VersionProperty('1.0.0')
    username = Property(title='Username', default='')
    password = Property(title='Password', default='')
    data_attr = Property(title='Data Field',
                         default='{{ $text }}',
                         visible=False)

    def __init__(self):
        self.tone_analyzer = None
        super().__init__()

    def start(self):
        self.tone_analyzer = ToneAnalyzerV3(username=self.username(),
                                            password=self.password(),
                                            version='2016-05-19')
        super().start()

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            new_signals.append(
                Signal(self.tone_analyzer.tone(self.data_attr(signal))))
        self.notify_signals(new_signals)
