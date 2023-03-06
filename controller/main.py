from fastapi import FastAPI, Request
from dto.requestDto import RobotsRequestDto
from dto.responseDto import *
from service.robotService import RobotService
from service.robotSlicingService import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
robotService = RobotService()

origins = [
    "http://52.79.49.1:8000",
    "http://52.79.49.1:8080",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/find/robot")
async def findRobot(request: Request, requestBody: RobotsRequestDto):
    try:
        robotText = await robotService.findRobotText(requestBody.url)
        robotText = cleanData(robotText)
        return RobotsSuccessResponseDto(200, robotText)
    except:
        dto = RobotsFailResponseDto(status=500, errorCode=1, errorUrl=requestBody.url)
        return dto
