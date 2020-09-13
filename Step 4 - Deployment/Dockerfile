FROM ubuntu:latest

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip

COPY requirements.txt /requirements.txt

RUN pip install --requirement requirements.txt

ADD src /src
ADD tests /tests
ADD run_app.py run_app.py

# run tests
RUN chmod +x tests/test_all.sh
RUN tests/test_all.sh
RUN rm -r /tests

EXPOSE 5000
CMD ["python3",  "-u" , "run_app.py"]
