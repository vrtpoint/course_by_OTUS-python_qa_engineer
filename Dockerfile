FROM python:3.7

LABEL author=vrtpoint

WORKDIR /course_by_OTUS-python_qa_engineer

COPY . /course_by_OTUS-python_qa_engineer

RUN apt-get update -y
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt

CMD tail -f /dev/null



