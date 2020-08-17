FROM python:slim

COPY ./ /rss

RUN pip install -r /rss/requirements.txt
RUN sudo chmod +x /rss/rss.sh
ENTRYPOINT ['/rss/rss.sh']


