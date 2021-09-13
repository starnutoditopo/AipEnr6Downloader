# AIP ENR-6 downloader

A simple utility to download [ENR-6 maps](https://www.enav.it/enavWebPortalStatic/AIP/AIP/enr/enr6/ENR6.htm) from ENAV, AIP, based on [Docker](https://www.docker.com/) with [Python 3.9.7 slim buster](https://hub.docker.com/_/python), [Selenium](https://selenium-python.readthedocs.io/index.html) and [ChromeDriver](https://chromedriver.chromium.org/).

# Usage

To use this utility, you must be registered on the [ENAV site](https://www.enav.it/); your username and password are required to download the maps.

# License

View [the LICENSE file](LICENSE.txt).

# Build the docker image

In Powershell, cd the project's root directory, then launch:

    docker build -t aipenr6downloader:1.0 -f AipEnr6Downloader.Dockerfile .

# Run

In your working folder, create a folder called Data, with a subfolder named AIP, then launch:

    docker run -it --rm -v "${PWD}/Data:/Data" aipenr6downloader:1.0 /usr/local/bin/python AipEnr6Downloader.py -u <username> -p <password>

Find the downloaded files in ./Data/AIP.