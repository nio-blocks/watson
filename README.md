Watson
======

This is a group of blocks that works with several of Watson's API services.
To use these blocks, you will need to have a Bluemix account and
set up a project for yourself: [Bluemix Account Setup](https://console.bluemix.net/registration/?)

For each service that you want to use you will need to set the service in bluemix,
which will give you a unique username and password for that service. These
will be the username and password you enter into the block.


WatsonToneAnalyzer
==================

This block takes in text and sends it through Watson's tone analyzer API and
returns an analysis of the emotions that could possibly be portrayed by the text.

Properties
--------------
- **username**(string): Bluemix account username
- **password**(string): Bluemix account password
- **data field**(expression): an expression that should evaluate to a string

Dependencies
----------------
watson_developer_cloud

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
A signal with attributes of emotions and associated confidence values

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


WatsonTextToSpeech
==================

This block takes in text and sends it through Watson's text to speech API,
outputting a .wav audio file that is the speech of the given text.

Properties
--------------
- **username**(string): Bluemix account username
- **password**(string): Bluemix account password
- **directory to save audio files**(path): location to save converted speech files
- **text to convert**(expression): an expression that should evaluate to a string, to be converted into speech
- **voice**(select): select which voice to use when sysnthesizing input text

Dependencies
----------------
watson_developer_cloud

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
A .wav file of the converted text in the specified directory.


WatsonSpeechToText
==================

This block reads a .wav file and sends it through Watson's speech to text
API, returning a dictionary of the recognized speech form the audio file,
along with alternative interpretations with confidence values.

Properties
--------------
- **username**(string): Bluemix account username
- **password**(string): Bluemix account password
- **speech file location**(path): speech file to read

Dependencies
----------------
watson_developer_cloud

Commands
----------------
None

Input
-------
A .wav file on the local machine.

Output
---------
A dictionary of the recognized speech form the audio file,
along with alternative interpretations with confidence values.

sample output signal:

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
