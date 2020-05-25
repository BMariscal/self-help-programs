FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev
WORKDIR /app

# install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip==9.0.3

RUN pip install -r ./requirements.txt --disable-pip-version-check
RUN pip install python-dotenv --disable-pip-version-check

COPY . .

CMD [ "flask", "run"]

