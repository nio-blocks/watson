from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..watson_tone_analyzer_block import WatsonToneAnalyzer
from ..watson_text_to_speech_block import WatsonTextToSpeech


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
            patched_analyzer.tone.assert_called_once_with(
                "patching attributes makes me FRUSTRATED"
            )

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"frustration": "90%"})


class TestWatsonTextToSpeechBlock(NIOBlockTestCase):

    def test_text_to_speech(self):
        """Make sure that synthesize is called"""
        blk = WatsonTextToSpeech()
        self.configure_block(blk, {})
        blk.start()
        with patch.object(blk, "tts_engine") as patched_synthesizer:
            with patch("builtins.open") as patched_open:
                blk.process_signals([Signal({
                    "text": "this is some sample text"
                })])
                # this should be called with defaults since no configuration
                # was given
                patched_synthesizer.synthesize.assert_called_once_with(
                    accept='audio/wav',
                    text='this is some sample text',
                    voice='en-US_LisaVoice')
                self.assertTrue(patched_open.called)

        blk.stop()
        self.assert_num_signals_notified(0)
