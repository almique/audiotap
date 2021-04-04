from typing import Optional
from datetime import datetime
from typing import List, Optional
from model.enumerations import *
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Dict, Union
from model.audioTypes import *

class SuccessResponse(BaseModel):
    msg: str = "Success"
    audioId: int
    audioFileType: AudioFileType


