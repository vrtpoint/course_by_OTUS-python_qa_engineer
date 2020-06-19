FROM python:3.7
MAINTAINER vrtpoint@gmail.com
COPY . /course_by_OTUS-python_qa_engineer
WORKDIR /course_by_OTUS-python_qa_engineer
RUN pip install -r requirements.txt
CMD tail -f /dev/null

