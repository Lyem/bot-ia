#!/bin/bash

poetry install

cd /home/python/.cache/pypoetry/virtualenvs/

for d in */ ; do
    cd "$d"
done

cd lib/python3.8/site-packages/chatterbot/

rm tagging.py

cp /home/python/app/.docker/tagging.py .

cd /home/python/.cache/pypoetry/virtualenvs/

for d in */ ; do
    cd "$d"
done

source ./bin/activate

python -m spacy download en_core_web_sm

python -m spacy download pt_core_news_sm

tail -f /dev/null
