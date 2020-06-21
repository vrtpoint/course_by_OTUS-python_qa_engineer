FROM python:3.7

LABEL author=vrtpoint

WORKDIR /course_by_OTUS-python_qa_engineer

COPY . /course_by_OTUS-python_qa_engineer

RUN python3 -m pip install -r requirements.txt
