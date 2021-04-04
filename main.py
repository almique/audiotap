from typing import Optional
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Path, Request
from datetime import datetime
from model.enumerations import *
from model.audioTypes import *
from model.exceptions import *
from model.responseFormats import *
from typing import Dict
from pydantic import BaseModel
from typing import Dict, Union
from controllers.mongoquery import *
from fastapi.responses import JSONResponse

app = FastAPI(
    title="AudioTap", description="An Audio file server simulator on FastAPI."
)


@app.exception_handler(AudioTapNotFound)
async def audiotap_exception_handler(request: Request, exc: AudioTapNotFound):
    return JSONResponse(
        status_code=400,
        content={"message": f"AudioTap couldn't find that audio"},
    )


@app.post(
    "/create",
    summary="Create API",
    description="Uploads an Audio for a given File Type and Audio ID to the database",
    tags=["Create API"],
    response_model=SuccessResponse,
)
def createAudio(
    audioId: int,
    audioFileType: AudioFileType,
    audioFileMetadata: Union[Podcast, Song, Audiobook],
):
    try:
        audio = createAudioQuery(audioFileType, audioFileMetadata, audioId)
        return SuccessResponse(
            audioId=audioId, audioFileType=audioFileType
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/delete/{audioFileType}/{audioId}",
    summary="Delete API",
    description="Deletes an Audio for a given File Type and Audio ID ",
    tags=["Delete API"],
    response_model=SuccessResponse,
)
def deleteAudio(audioFileType: AudioFileType, audioId: int):
    try:
        deleteAudioQuery(audioFileType, audioId)
        return SuccessResponse(audioId=audioId, audioFileType=audioFileType)
    except AudioTapNotFound as e:
        raise AudioTapNotFound(audioId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post(
    "/update/{audioFileType}/{audioId}",
    summary="Update API",
    description="Updates an Audio for a given File Type and Audio ID with new data",
    tags=["Update API"],
    response_model=SuccessResponse,
)
def updateAudio(
    audioId: int, audioFileType: AudioFileType, audioFileMetadata: AudioFileMetadata
):
    try:
        audio = updateAudioQuery(audioFileType, audioId, audioFileMetadata)
        return SuccessResponse(
            audioId=audioId, audioFileType=audioFileType
        )
    except AudioTapNotFound as e:
        raise AudioTapNotFound(audioId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/get/{audioFileType}/{audioId}",
    summary="Get API",
    description="Fetches an Audio for a given File Type and Audio ID",
    tags=["Get API"],
)
def getAudio(audioFileType: AudioFileType, audioId: int):
    try:
        audio = getAudioQuery(audioFileType, audioId)
        if audio == None:
            raise AudioTapNotFound(audioId)
        return audio
    except AudioTapNotFound as e:
        raise AudioTapNotFound(audioId)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="AudioTap had trouble finding that audio"
        )


@app.get(
    "/get/{audioFileType}/",
    summary="Get All API",
    description="Fetches all Audio for a given File Type",
    tags=["Get All API"],
)
def getAllAudio(audioFileType: AudioFileType):
    try:
        audios = getAllAudioQuery(audioFileType)
        if audios == None or len(audios) == 0:
            raise AudioTapNotFound(audioId)
        return audios
    except AudioTapNotFound as e:
        raise AudioTapNotFound(audioId)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="AudioTap had trouble finding any audios of that type"
        )
