FROM python:3.7
WORKDIR /app

COPY setup.py .
COPY setup.cfg .

RUN pip3 install -e '.[install_requires]'
RUN pip3 install -e '.[dev]'

COPY . ./users

CMD ["python3", "users/run.py"]

