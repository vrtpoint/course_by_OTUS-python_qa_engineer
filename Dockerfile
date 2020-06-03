FROM python:3.7

WORKDIR /app

COPY . .

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["http://localhost"]
CMD ["pytest", "tests/"]