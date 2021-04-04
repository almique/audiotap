from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class AudioTapNotFound(Exception):
    def __init__(self, audioTapId: str):
        self.audioTapId = audioTapId