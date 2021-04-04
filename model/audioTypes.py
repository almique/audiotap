from typing import Optional
from datetime import datetime
from typing import List, Optional
from model.enumerations import *
from fastapi import FastAPI, Path
from pydantic import BaseModel, ValidationError, validator
from typing import Dict

class AudioFileMetadata(BaseModel):
    name: str
    uploadTime: datetime
    duration: int

    @validator('name')
    def name_cannot_be_larger_than_100_chars(cls, v):
        if len(v) > 100:
            raise ValueError('name cannot be larger than 100 characters')
        return v

    @validator('duration')
    def duration_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Duration must be positive')
        return v

class Song(AudioFileMetadata):
    class Config:
        extra = 'forbid'

class Podcast(AudioFileMetadata):
    host: str
    participants: List[str] = []

    @validator('participants')
    def participants_cannot_be_more_than_10(cls, v):
        if len(v) > 10:
            raise ValueError('maximum of 10 participants possible')
        return v
    @validator('participants')
    def participants_name_max_100_chars(cls, v):
        for i in v:
            if len(i) > 100:
                raise ValueError('participant names cannot be larger than 100 characters')
        return v

    
class Audiobook(AudioFileMetadata):
    author: str
    narrator: str

    @validator('narrator')
    def narrator_cannot_be_larger_than_100_chars(cls, v):
        if len(v) > 100:
            raise ValueError('narrator cannot be larger than 100 characters')
        return v

 