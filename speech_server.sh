#!/bin/bash

python start_speech_service.py &
python read_text_from_queue.py &

