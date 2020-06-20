FROM python:3.7

LABEL author=vrtpoint

WORKDIR /course_by_OTUS-python_qa_engineer

COPY . /course_by_OTUS-python_qa_engineer

RUN pip3 install -r requirements.txt

CMD tail -f /dev/null



