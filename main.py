from typing import Optional
from typing import List
from fastapi import FastAPI, Path
from datetime import datetime
from classes.enumerations import *
from classes.adclass import *
from typing import Dict
from pydantic import BaseModel
from typing import Dict
from controllers.mongoquery import *

app = FastAPI(
    title="AudioTap",
    description="An Audio file server simulator on FastAPI."
)

#Implements create, read, upload, and delete endpoints for an audio file.


@app.post("/create",
summary = "Create API",
description = "",
tags=["Create API"]
) 
def create(FileType: audioFileType , audioFileMetadata: AudioTypeMeta):
    return createquery(FileType, audioFileMetadata)

@app.post("/delete",
summary = "Delete API",
description = "",
tags=["Delete API"]
) 
def deletead(FileType: audioFileType , audioid: str):
    return mongodelete(FileType, audioid) 

@app.post("/update",
summary = "Update API",
description = "",
tags=["Update API"]
) 
def updatead(FileType: audioFileType , audioid: str, audioFileMetadata: AudioTypeMeta):
    return updatequery(FileType, audioid, audioFileMetadata)

@app.get("/get",
summary = "Get API",
description = "",
tags=["Get API"]
) 
def getad(FileType: audioFileType , audioid: str):
    return getquery(FileType, audioid)


