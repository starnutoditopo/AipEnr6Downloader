# AIP ENR-6 downloader

A simple utility to download [ENR-6 maps](https://www.enav.it/enavWebPortalStatic/AIP/AIP/enr/enr6/ENR6.htm) from ENAV, AIP, based on [Docker](https://www.docker.com/) with [Python 3.9.7 slim buster](https://hub.docker.com/_/python), [Selenium](https://selenium-python.readthedocs.io/index.html) and [ChromeDriver](https://chromedriver.chromium.org/).

# License

View [the LICENSE file](LICENSE).

# Usage

**To use this utility, you must be registered on the [ENAV site](https://www.enav.it/); your username and password are required to download the maps.**

## Build the Docker image

After having cloned or downloaded this repository, in Powershell, cd the project's root directory, then launch:

    docker build -t aipenr6downloader:1.0 -f AipEnr6Downloader.Dockerfile .

## Run

After having built the Docker image, in your working folder, create a folder called Data, with a subfolder named AIP, then launch:

    docker run -it --rm -v "${PWD}/Data:/Data" aipenr6downloader:1.0 /usr/local/bin/python AipEnr6Downloader.py -u <username> -p <password>

Find the downloaded files in ./Data/AIP.

# Develop and debug

This project contains a .devcontainer folder, configured to create a Docker container to be used with Visual Studio Code: just launch VSC and open this folder in container.

For your convenience, create a .vscode/launch.json file with a content like this:

    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "args": [
                    "-u", "<your userName here>",
                    "-p", "<your password here>",
                    "-o", "./Data/AIP"
                ]
            }
        ]
    }

Open the AipNr6Downloader.py file and press the F5 key to start debugging.