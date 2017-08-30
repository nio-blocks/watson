from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..watson_tone_analyzer_block import WatsonToneAnalyzer
from ..watson_text_to_speech_block import WatsonTextToSpeech
from ..watson_speech_to_text_block import WatsonSpeechToText


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


class TestWatsonSpeechToTextBlock(NIOBlockTestCase):

    def test_speech_to_text(self):
        """Make sure that recognize is called"""
        blk = WatsonSpeechToText()
        self.configure_block(blk, {})
        blk.start()
        with patch.object(blk, "stt_engine") as patched_recognizer:
            with patch("nio.types.file.FileHolder") as patched_file_holder:
                # this is the data the file read returns
                patched_file_holder.return_value.__enter__.return_value.\
                    read.return_value = b'hello'
                # this is the recognized data from the recognizer
                patched_recognizer.recognize.return_value = {
                    "recognized": "hello"
                }

                blk.process_signals([Signal({
                    "trigger": "this has triggered a file read"
                })])
                patched_recognizer.recognize.assert_called_once_with(
                    audio=b'hello',
                    content_type="audio/wav")
                self.assertTrue(patched_file_holder.called)

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"recognized": "hello"})
