from enum import Enum

class AudioFileType(str, Enum):
    Song = "Song"
    Podcast = "Podcast"
    Audiobook = "Audiobook"

    