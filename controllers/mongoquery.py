import pymongo
import datetime
from datetime import timedelta
from typing import List, Optional
from model.enumerations import *
from model.audioTypes import *
from model.exceptions import *
import configparser

conf = configparser.ConfigParser()
conf.read("config/server.conf")

client = pymongo.MongoClient(conf.get("database", "url"))
db = client[conf.get("database", "db")]
collection = db[conf.get("database", "collection")]


def getAllAudioQuery(audioFileType):
    """
    Fetches all Audio from the database for a given file type 

    Args:
        audioFileType (AudioFileType): file type
    Returns:
        audioRecord(s)
    """
    try:
        rawRecs = list(collection.find({"audioFileType": audioFileType.name}))
        audioRecords = []
        for audioRec in rawRecs:
            audioRec.pop('_id', None)
            audioRecords.append(audioRec)
        return audioRecords if audioRecords else None
    except Exception as e:
        return None

def getAudioQuery(audioFileType, audioId):
    """
    Fetches an Audio from the database for a given file type and audioId

    Args:
        audioFileType (AudioFileType): file type
        audioId (int): audioId

    Returns:
        audioRecord
    """
    try:
        cursor = collection.find({"audioFileType": audioFileType.name, "audioId": audioId})
        audioRecord = cursor.next()
        audioRecord.pop('_id', None)
        return audioRecord if audioRecord else None
    except Exception as e:
        return None


def createAudioQuery(audioFileType, audioFileMetadata, audioId):
    """
    Creates an Audio in the database for a given file type and audioId. Audio Id is first checked for uniqueness.

    Args:
        audioFileType (AudioFileType): file type
        audioFileMetadata (AudioFilemetadata): Audio Information
        audioId (int): audioId

    Returns:
        audioRecord if successful else raises exception
    """
    if getAudioQuery(audioFileType, audioId) is None:
        audioObj = audioFileMetadata.__dict__
        audioObj["audioFileType"] = audioFileType
        audioObj["audioId"] = audioId
        collection.insert_one(audioObj)
        return audioObj
    raise AudioTapNotFound(audioId)


def deleteAudioQuery(audioFileType, audioId):
    """
    Deletes an Audio in the database for a given file type and audioId. Audio Id is first checked for uniqueness.

    Args:
        audioFileType (AudioFileType): file type
        audioId (int): audioId

    Returns:
        Boolean True if successful else raises exception
    """
    if getAudioQuery(audioFileType, audioId) is not None:
        collection.delete_one({"audioFileType": audioFileType, "audioId": audioId})
        return True
    raise AudioTapNotFound(audioId)


def updateAudioQuery(audioFileType, audioId, audioFileMetadata):
    """
    Updates an Audio in the database with new audioFileMetadata for a given file type and audioId. Audio Id is first checked for uniqueness.

    Args:
        audioFileType (AudioFileType): file type
        audioId (int): audioId
        audioFileMetadata (AudioFilemetadata): Audio Information

    Returns:
        audioRecord if successful else raises exception
    """
    if getAudioQuery(audioFileType, audioId) is not None:
        if deleteAudioQuery(audioFileType, audioId):
            audioQ = createAudioQuery(audioFileType, audioFileMetadata, audioId)
            return audioQ
    raise AudioTapNotFound(audioId)
