WatsonSpeechToText
==================
This block reads a .wav file and sends it through Watson's speech to text API, returning a dictionary of the recognized speech from the audio file, along with alternative interpretations with confidence values.

Properties
----------
- **creds**: IBM Bluemix API credentials
- **speech_file_location**: Speech file to read.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: A dictionary of the recognized speech from the audio file, along with alternative interpretations with confidence values.

Commands
--------
None

Dependencies
------------
watson_developer_cloud

Output Example
--------------
Sample output signal:
```
{
  'results': [
    {
      'final': True,
      'alternatives': [
        {
          'confidence': 0.972,
          'transcript': 'hello world again '
        }
      ]
    }
  ],
  'result_index': 0,
  'warnings': [
    'Unknown arguments: continuous.'
  ]
}
```

WatsonTextToSpeech
==================
This block takes in text and sends it through Watson's text to speech API, outputting a .wav audio file that is the speech of the given text.

Properties
----------
- **creds**: IBM Bluemix API credentials
- **data_attr**: An expression that should evaluate to a string, to be converted into speech.
- **speech_file_location**: Location to save converted speech files.
- **voice**: Select which voice to use when sysnthesizing input text.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
None

Commands
--------
None

Dependencies
------------
watson_developer_cloud

WatsonToneAnalyzer
==================
This block takes in text and sends it through Watson's tone analyzer API and returns an analysis of the emotions that could possibly be portrayed by the text.

Properties
----------
- **creds**: IBM Bluemix API credentials
- **data_attr**: An expression that should evaluate to a string which will be analyzed for the tone.
- **enrich**: *enrich_field:* The attribute on the signal to store the results from this block. If this is empty, the results will be merged onto the incoming signal. This is the default operation. Having this field allows a block to 'save' the results of an operation to a single field on an incoming signal and notify the enriched signal.  *results field:* The attribute on the signal to store the results from this block. If this is empty, the results will be merged onto the incoming signal. This is the default operation. Having this field allows a block to save the results of an operation to a single field on an incoming signal and notify the enriched signal.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: A signal with attributes of emotions and associated confidence values.

Commands
--------
None

Dependencies
------------
watson_developer_cloud

Output Example
--------------
Sample output signal:
```
{
  'document_tone': {
    'tone_categories': [
      {
        'category_name': 'Emotion Tone',
        'tones': [
          {
            'score': 0.0,
            'tone_id': 'anger',
            'tone_name': 'Anger'
          },
          {
            'score': 0.0,
            'tone_id': 'disgust',
            'tone_name': 'Disgust'
          },
          {
            'score': 0.0,
            'tone_id': 'fear',
            'tone_name': 'Fear'
          },
          {
            'score': 0.0,
            'tone_id': 'joy',
            'tone_name': 'Joy'
          },
          {
            'score': 0.0,
            'tone_id': 'sadness',
            'tone_name': 'Sadness'
          }
        ],
        'category_id': 'emotion_tone'
      },
      {
        'category_name': 'Language Tone',
        'tones': [
          {
            'score': 0.0,
            'tone_id': 'analytical',
            'tone_name': 'Analytical'
          },
          {
            'score': 0.0,
            'tone_id': 'confident',
            'tone_name': 'Confident'
          },
          {
            'score': 0.0,
            'tone_id': 'tentative',
            'tone_name': 'Tentative'
          }
        ],
        'category_id': 'language_tone'
      },
      {
        'category_name': 'Social Tone',
        'tones': [
          {
            'score': 0.113626,
            'tone_id': 'openness_big5',
            'tone_name': 'Openness'
          },
          {
            'score': 0.27939,
            'tone_id': 'conscientiousness_big5',
            'tone_name': 'Conscientiousness'
          },
          {
            'score': 0.478219,
            'tone_id': 'extraversion_big5',
            'tone_name': 'Extraversion'
          },
          {
            'score': 0.591115,
            'tone_id': 'agreeableness_big5',
            'tone_name': 'Agreeableness'
          },
          {
            'score': 0.226618,
            'tone_id': 'emotional_range_big5',
            'tone_name': 'Emotional Range'
          }
        ],
        'category_id': 'social_tone'
      }
    ]
  }
}
```

