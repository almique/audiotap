from enum import Enum

class audioFileType(str, Enum):
    Song = "Song"
    Podcast = "Podcast"
    Audiobook = "Audiobook"

    