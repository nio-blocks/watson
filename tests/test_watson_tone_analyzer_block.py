from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from watson.watson_tone_analyzer_block import WatsonToneAnalyzer


class TestWatsonToneAnalyzer(NIOBlockTestCase):

    def test_process_signals(self):
        """Make sure that tone is called"""
        blk = WatsonToneAnalyzer()
        self.configure_block(blk, {})
        blk.start()
        with patch.object(blk, "tone_analyzer") as patched_analyzer:
            patched_analyzer.tone.return_value = {"frustration": "90%"}
            blk.process_signals([Signal({
                "text": "patching attributes makes me FRUSTRATED"
            })])

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"frustration": "90%"})
