# Python Text To Speech Server

Simple text to speech server that places text on a queue and reads the queue out loud one item at a time.

# Setup

Espeak must be on your path.

THe `rpyc` library is required, and can be installed via

```bash
pip install rpyc
```

## Usage

To run the server asynchronously:

```bash
./speech_server.sh
```

To add text to the queue to be read:

```python
from speak import speak, speak_synchronous

# Add an item to the queue to be read aloud
speak_synchronous('This is text to be read')

# Read text aloud directly using espeak
# This may be asynchronous, i.e. multiple calls will speak over other speech
speak('This is text to be read')
```
