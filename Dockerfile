FROM python:slim

COPY ./ /rss

RUN pip install -r /rss/requirements.txt
RUN chmod +x /rss/rss.sh
ENTRYPOINT ['/rss/rss.sh']


