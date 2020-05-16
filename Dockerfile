FROM python:alpine3.7
COPY ./hackernews ./hackernews
WORKDIR /hackernews
RUN pip install -r requirements.txt
CMD python ./hackernews.py hackernews --posts 50