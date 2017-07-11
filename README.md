WatsonToneAnalyzer
==================

This block takes in text and sends it through Watson's tone analyzer API,
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
