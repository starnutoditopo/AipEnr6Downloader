FROM python:3.9.7-slim-buster

USER root

WORKDIR /src

RUN apt-get -yqq update \
    && apt-get -yqq install wget \
    && apt-get -yqq install gnupg
    
# See: https://stackoverflow.com/a/44698744/1288109    
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && /bin/sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get -yqq update \
    && apt-get -yqq install google-chrome-stable
    
RUN apt-get -yqq install unzip curl \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip -o /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && pip install selenium

COPY ./AipEnr6Downloader.py .

# Build:
#	docker build -t aipenr6downloader:1.0 -f AipEnr6Downloader.Dockerfile .
#
# Run:
#   docker run -it --rm -v "${PWD}/Data:/Data" aipenr6downloader:1.0 /usr/local/bin/python AipEnr6Downloader.py -u <username> -p <password>
