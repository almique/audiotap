from fastapi.testclient import TestClient

from main import app
import logging


client = TestClient(app)

# ------------------ Tests for Songs -------------------------- #


def test_get_song_nonexisting():
    response = client.get("/get/Song/1")
    assert response.status_code == 400


def test_delete_song_nonexisting():
    response = client.get("/delete/Song/1")
    assert response.status_code == 400


def test_update_song_nonexisting():
    response = client.post("/update/Song/1",
        json={
            "name": "Levitating",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 1243,
        })
    assert response.status_code == 400
    
def test_create_song():
    response = client.post(
        "/create?audioId=1&audioFileType=Song",
        json={
            "name": "Makeba",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 2121,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "msg": "Success",
            "audioId": 1,
            "audioFileType": "Song",
            }


def test_get_song_existing():
    response = client.get("/get/Song/1")
    assert response.status_code == 200
    assert response.json() == {
                "name": "Makeba",
                "uploadTime": "2022-04-03T22:47:00.028000",
                "duration": 2121,
                "audioFileType": "Song",
                "audioId": 1
            }


def test_get_all_song_existing():
    response = client.get("/get/Song")
    assert response.status_code == 200
    assert response.json() == [{
                "name": "Makeba",
                "uploadTime": "2022-04-03T22:47:00.028000",
                "duration": 2121,
                "audioFileType": "Song",
                "audioId": 1
            }]
            
def test_update_song_existing():
    response = client.post("/update/Song/1",
        json={
            "name": "Levitating",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 1243,
        })
    assert response.status_code == 200
    assert response.json() == {
            "msg": "Success",
            "audioId": 1,
            "audioFileType": "Song",
            }

def test_delete_song_existing():
    response = client.get("/delete/Song/1")
    assert response.status_code == 200

  
def test_large_song_name():
    response = client.post(
        "/create?audioId=1&audioFileType=Song",
        json={
            "name": "A"*101,
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 2121,
        },
    )
    assert response.status_code == 422
  


# ------------------ Tests for Podcast -------------------------- #

def test_get_podcast_nonexisting():
    response = client.get("/get/Podcast/1")
    assert response.status_code == 400


def test_delete_podcast_nonexisting():
    response = client.get("/delete/Podcast/1")
    assert response.status_code == 400


def test_update_podcast_nonexisting():
    response = client.post("/update/Podcast/1",
        json={
            "name": "The Pale Blue Dot",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 72847,
            "host": "Carl Sagan",
            "participants": ["John", "Bob"]
        })
    assert response.status_code == 400
    
def test_create_podcast():
    response = client.post(
        "/create?audioId=1&audioFileType=Podcast",
        json={
            "name": "The Pale Blue Dot",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 72847,
            "host": "Carl Sagan",
            "participants": ["John", "Bob"]
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "msg": "Success",
            "audioId": 1,
            "audioFileType": "Podcast",
            }


def test_get_podcast_existing():
    response = client.get("/get/Podcast/1")
    assert response.status_code == 200
    assert response.json() == {
                "audioId": 1,
                "audioFileType": "Podcast",
                "name": "The Pale Blue Dot",
                "uploadTime": "2022-04-03T22:47:00.028000",
                "duration": 72847,
                "host": "Carl Sagan",
                "participants": ["John", "Bob"]
            }

def test_update_podcast_existing():
    response = client.post("/update/Podcast/1",
        json={
            "name": "Our Planet",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 32341,
            "host": "David Attenborough",
            "participants": ["Marie", "Alice"]
        })
    assert response.status_code == 200
    assert response.json() == {
            "msg": "Success",
            "audioId": 1,
            "audioFileType": "Podcast",
            }


def test_delete_podcast_existing():
    response = client.get("/delete/Podcast/1")
    assert response.status_code == 200
    

def test_max_ten_participants():
    response = client.post(
        "/create?audioId=1&audioFileType=Podcast",
        json={
            "name": "ABC",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 72847,
            "host": "AC",
            "participants": ["John"]*12
        },
    )
    assert response.status_code == 422



def test_participant_name_max_100_chars():
    response = client.post(
        "/create?audioId=1&audioFileType=Podcast",
        json={
            "name": "ABC",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": 72847,
            "host": "AC",
            "participants": ["A"*102]*5
        },
    )
    assert response.status_code == 422


def test_duration_must_be_positive():
    response = client.post(
        "/create?audioId=1&audioFileType=Podcast",
        json={
            "name": "ABC",
            "uploadTime": "2022-04-03T22:47:00.028Z",
            "duration": -1,
            "host": "AC",
            "participants": ["A"]
        },
    )
    assert response.status_code == 422

