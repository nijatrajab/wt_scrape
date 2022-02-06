# W-T scrape project

## Setup for local development

### Dependencies

* [Docker](https://www.docker.com/get-started)

### Installing

* Clone the repo
```
git clone https://github.com/nijatrajab/wt_scrape.git
```
* Open `cmd` on cloned directory then follow commands:
```
docker-compose up --abort-on-container-exit
```
_Make sure Docker is running as an administrator. For the first time it may take a few minutes to start because of creating containers_

It will create docker images and then start containers for a service. When execution ends it will create `data.csv` and `data.json` on cloned directory
