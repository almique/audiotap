import pymongo
import datetime
from datetime import timedelta
from typing import List, Optional
from classes.enumerations import *
from classes.adclass import *
import configparser

conf = configparser.ConfigParser()
conf.read('config/server.conf')

myclient = pymongo.MongoClient(conf.get("database", "url"))
mydb = myclient[conf.get("database", "db")]
mycol = mydb[conf.get("database", "column")]


class song():
    songname : str
    audioid : str
    uploadtime: datetime
    duration: int
class podcast():
    audioid : str
    uploadtime: datetime
    duration: int
    podcastname: str
    host: List[str] = []
    participants: List[str] = []
    
class audiobook():
    audioid : str
    uploadtime: datetime
    duration: int
    audiobookname: str
    author: str
    narrator: str

class audiotypemeta(song, podcast, audiobook):
    FileType: audioFileType

def createquery(FileType, audioFileMetadata) -> AudioTypeMeta:
    x = audiotypemeta()
    if FileType == audioFileType.Song:
        x.FileType = FileType
        x.audioid = audioFileMetadata.audioid
        x.duration = audioFileMetadata.duration
        x.uploadtime = audioFileMetadata.uploadtime
        x.songname = audioFileMetadata.songname
    elif FileType == audioFileType.Podcast:
        x.FileType = FileType
        x.audioid = audioFileMetadata.audioid
        x.duration = audioFileMetadata.duration
        x.uploadtime = audioFileMetadata.uploadtime
        x.podcastname = audioFileMetadata.podcastname
        x.host = audioFileMetadata.host
        x.participants = audioFileMetadata.participants
    elif FileType == audioFileType.Audiobook:
        x.FileType = FileType
        x.audioid = audioFileMetadata.audioid
        x.duration = audioFileMetadata.duration
        x.uploadtime = audioFileMetadata.uploadtime
        x.audiobookname = audioFileMetadata.audiobookname
        x.author = audioFileMetadata.author
        x.narrator = audioFileMetadata.narrator

    ob = mycol.insert_one(x.__dict__)
    if ob:
        return x
    else:
        return 0

def mongodelete(FileType, audioid) -> bool:
    myquery = {"FileType": FileType , "audioid": audioid }
    if mycol.delete_one(myquery):
        return True
    else:
        return False

def updatequery(FileType, audioid, audioFileMetadata) -> Dict:
    myquery = {"FileType": FileType , "audioid": audioid }
    newvalues = { "$set": { "uploadtime": audioFileMetadata.uploadtime, "duration": audioFileMetadata.duration,
    "host": audioFileMetadata.host, "podcastname": audioFileMetadata.podcastname,
    "songname": audioFileMetadata.songname, "audiobookname": audioFileMetadata.audiobookname,
    "author": audioFileMetadata.author, "narrator": audioFileMetadata.narrator} }

    if mycol.update_one(myquery, newvalues):
        return newvalues
    else:
        return 0


def getquery(FileType, audioid) -> AudioTypeMeta:
    myquery = {"FileType": FileType , "audioid": audioid }
    ob = mycol.find(myquery)
    for x in ob:
        return x
