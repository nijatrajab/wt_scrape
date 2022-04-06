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

_Make sure Docker is running as an administrator. For the first time it may take a few minutes to start because of
creating containers_

It will create docker images and then start containers for a service. When execution ends, it will create [`data.csv`](https://github.com/nijatrajab/wt_scrape/tree/main/dummy/data.csv)
and [`data.json`](https://github.com/nijatrajab/wt_scrape/tree/main/dummy/data.json) on cloned directory



#### Dummy data
[CSV Format](https://github.com/nijatrajab/wt_scrape/tree/main/dummy/data.csv)
```
| brand   | model                                 | identification            | title                                       | full_title                                                            | memory | color         | price | discount_price | image                                                                  | link                                                                                                                    | category              | subcategory      |
| ------- | ------------------------------------- | ------------------------- | ------------------------------------------- | --------------------------------------------------------------------- | ------ | ------------- | ----- | -------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------- |
| Apple   | iPad Pro 12.9" Wi-Fi (5th Gen) (2021) | (MHNJ3LL/A) 256 GB Silver | Apple iPad Pro 12.9" Wi-Fi (5th Gen) (2021) | Apple iPad Pro 12.9" Wi-Fi (5th Gen) (2021) (MHNJ3LL/A) 256 GB Silver | 256GB  | darkgray      | 2799  |                | https://w-t.ams3.cdn.digitaloceanspaces.com/images/12.9white-min.jpg   | https://www.w-t.az/mehsul/60807ecea6bdf96cdb1b871d/apple-ipad-pro-12.9"-wi-fi-(5th-gen)-(2021)-(mhnj3lla)-256-gb-silver | Telefon və planşetlər | Planşetlər       |
| Samsung | Galaxy Z Flip 3 (F711)                | Cream                     | Samsung Galaxy Z Flip 3 (F711)              | Samsung Galaxy Z Flip 3 (F711) Cream                                  | 256GB  | palegoldenrod | 2499  |                | https://w-t.ams3.cdn.digitaloceanspaces.com/images/flip3-beige-min.jpg | https://www.w-t.az/mehsul/6113974f51e6c1659d6ebfa5/samsung-galaxy-z-flip-3-(f711)-cream                                 | Telefon və planşetlər | Mobil telefonlar |
| Apple   | iPhone 13 Pro Max                     | 1TB Sierra Blue           | Apple iPhone 13 Pro Max                     | Apple iPhone 13 Pro Max 1TB Sierra Blue                               | 1TB    | skyblue       | 4449  |                | https://w-t.ams3.cdn.digitaloceanspaces.com/images/sierra-blue-min.jpg | https://www.w-t.az/mehsul/613b3fc3f866c43ad90e0fb0/apple-iphone-13-pro-max-1tb-sierra-blue                              | Telefon və planşetlər | Mobil telefonlar |
| Xiaomi  | Mi 11T                                | 256GB Celestial Blue      | Xiaomi Mi 11T                               | Xiaomi Mi 11T 256GB Celestial Blue                                    | 256GB  | steelblue     | 1399  |                | https://w-t.ams3.cdn.digitaloceanspaces.com/images/blue11-min.jpg      | https://www.w-t.az/mehsul/6194d7e3c888e0314af2f6e0/xiaomi-mi-11t-256gb-celestial-blue                                   | Telefon və planşetlər | Mobil telefonlar |
```
[JSON Format](https://github.com/nijatrajab/wt_scrape/tree/main/dummy/data.json)
```json
[
  {
    "brand": "Xiaomi",
    "model": "Redmi Note 9 Pro",
    "identification": "128GB Gray",
    "title": "Xiaomi Redmi Note 9 Pro",
    "full_title": "Xiaomi Redmi Note 9 Pro 128GB Gray",
    "memory": "128GB",
    "color": "gray",
    "price": 639,
    "discount_price": null,
    "image": "https://w-t.ams3.cdn.digitaloceanspaces.com/images/note 9 pro gray-min.jpg",
    "link": "https://www.w-t.az/mehsul/5ee0cbf7d5ef910007c111de/xiaomi-redmi-note-9-pro-128gb-gray",
    "category": "Telefon və planşetlər",
    "subcategory": "Mobil telefonlar"
  },
  {
    "brand": "JBL",
    "model": "Tune 225",
    "identification": "Ghost Orange",
    "title": "JBL Tune 225",
    "full_title": "JBL Tune 225 Ghost Orange",
    "memory": null,
    "color": "orangered",
    "price": 249,
    "discount_price": null,
    "image": "https://w-t.ams3.cdn.digitaloceanspaces.com/images/orange-min.jpg",
    "link": "https://www.w-t.az/mehsul/60891c33c2eb734d6ed7e86e/jbl-tune-225-ghost-orange",
    "category": "TV, Audio və Əyləncə",
    "subcategory": "Qulaqlıqlar"
  }
]
```

<<<<<<< HEAD
# microservices

For Docker run this commands:

1) ```docker-compose build```
2) ```docker-compose up -d db```
3) ```docker exec -t models-microservices_db_1 pg_restore -U postgres -d h55 /docker-entrypoint-initdb.d/backup```
4) ```docker-compose up -d app```

DB will up with initial data. If you have another backup file and want to replace it please replace "backup" file with your backup.

Otherwise:

1) ```pip install -r requirements.txt```
2) ```alembic upgrade head```
2) ```uvicorn app.main:app --reload```

```console
app
├── api              - web related stuff.
│   ├── dependencies - dependencies for routes definition.
│   ├── errors       - definition of error handlers.
│   └── routes       - web URL's
├── core             - configuration, events, logging
├── db               - db related stuff.
│   ├── migrations   - manually written alembic file
│   └── repositories - CRUD stuff
├── models           - pydantic models 
│   ├── domain       - main models that we will use everywhere
│   └── schemas      - schemas for using in web routes( it is like a serializers.py in DRF )
├── resources        - strings that are used in web responses.
├── services         - logic that is not just crud related.
└── main.py          - FastAPI application creation
```
=======
