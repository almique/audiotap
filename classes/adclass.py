from typing import Optional
from datetime import datetime
from typing import List, Optional
from classes.enumerations import *
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Dict


class Song(BaseModel):
    songname : str
    audioid : str
    uploadtime: datetime
    duration: int
class Podcast(BaseModel):
    audioid : str
    uploadtime: datetime
    duration: int
    podcastname: str
    host: List[str] = []
    participants: List[str] = []
    
class Audiobook(BaseModel):
    audioid : str
    uploadtime: datetime
    duration: int
    audiobookname: str
    author: str
    narrator: str

class AudioTypeMeta(Song, Podcast, Audiobook):
    FileType: audioFileType