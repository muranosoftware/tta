FROM python:2.7
COPY ./src /app
WORKDIR /app
RUN python setup.py install
ENTRYPOINT ["tta"]
