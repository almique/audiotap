# audiotap

<p align="center"><img src="https://github.com/almique/audiotap/raw/main/assets/audiotap.png" width="150px"></p>
<br/>

AudioTap is a simulator app for an Audio FileServer

## Swagger 

Swagger / OpenAPI can be accessed at `localhost:8000/docs`

<img src="https://github.com/almique/audiotap/raw/main/assets/screenshot.png">


## Running the service

1. Clone the repository, install dependencies and start the service
```bash
git clone https://github.com/almique/audiotap
./bin/install_deps
./bin/start_service
```

2. Use Postman or CLI or Swagger UI to query 


## Running the tests

1. Clone the repository, install dependencies and run the tests
```bash
git clone https://github.com/almique/audiotap
./bin/install_deps
./bin/run_tests
```

2. If the tests are successful you should see the following

<img src="https://github.com/almique/audiotap/raw/main/assets/tests.png">


## API Endpoints

### `/create` Endpoint
Uploads an Audio for a given File Type and Audio ID to the database

#### Examples

#### **Request** 
- Create a new Song

```bash
curl -X 'POST' \
  'http://localhost:8000/create?audioId=1&audioFileType=Song' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Yellow",
  "uploadTime": "2021-04-04T01:17:09.017Z",
  "duration": 3278
}'
```
- Create a new Audiobook
  
```bash
curl -X 'POST' \
  'http://localhost:8000/create?audioId=1&audioFileType=Audiobook' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Nonviolent Communication",
  "uploadTime": "2021-04-04T01:17:09.017Z",
  "duration": 3278,
  "author": "Marshall Rosenberg",
  "narrator": "Marshall Rosenberg",
}'
```
- Create a new Podcast

```bash
curl -X 'POST' \
  'http://localhost:8000/create?audioId=1&audioFileType=Podcast' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Leadership Skills",
  "uploadTime": "2021-04-04T01:17:09.017Z",
  "duration": 3278,
  "host": "Jay Cornwall",
  "participants": ["John", "Bob"]
}'
```

#### **Response**

```json
{
  "msg": "Success",
  "audioId": 1,
  "audioFileType": "Song"
}
```

### `/delete/{audioFileType}/{audioId}` Endpoint
Deletes an Audio for a given File Type and Audio ID

```bash
curl -X 'GET' \
  'http://localhost:8000/delete/Song/1' \
  -H 'accept: application/json'
```

### `/update/{audioFileType}/{audioId}` Endpoint
Updates an Audio for a given File Type and Audio ID with new data

#### **Request**
```bash
curl -X 'POST' \
  'http://localhost:8000/update/Song/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Cemeteries of London",
  "uploadTime": "2021-04-04T01:23:11.847Z",
  "duration": 3279
}'
```

#### **Response**
```json
{
  "name": "Cemeteries of London",
  "uploadTime": "2021-04-04T01:23:11.847000",
  "duration": 3279,
  "audioFileType": "Song",
  "audioId": 1
}
```

### `/get/{audioFileType}/{audioId}` Endpoint

Fetches an Audio for a given File Type and Audio ID

#### **Request**
```bash
curl -X 'GET' \
  'http://localhost:8000/get/Song/1' \
  -H 'accept: application/json'
```
#### **Response**
```json
{
  "name": "Cemeteries of London",
  "uploadTime": "2021-04-04T01:23:11.847000",
  "duration": 3279,
  "audioFileType": "Song",
  "audioId": 1
}
```

### `/get/{audioFileType}/` Endpoint

Fetches all Audio for a given File Type

#### **Request**
```bash
curl -X 'GET' \
  'http://localhost:8000/get/Song/' \
  -H 'accept: application/json'
```
#### **Response**
```json
[
  {
    "name": "Levitating",
    "uploadTime": "2022-04-03T22:47:00.028000",
    "duration": 1243,
    "audioFileType": "Song",
    "audioId": 1
  },
  {
    "name": "Good Life",
    "uploadTime": "2021-04-04T02:01:18.493000",
    "duration": 2782,
    "audioFileType": "Song",
    "audioId": 2
  }
]
```
