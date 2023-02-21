from fastapi import FastAPI, Request
from dto.requestDto import RobotsRequestDto
from dto.responseDto import *
from service.robotService import RobotService
from service.robotSlicingService import *

app = FastAPI()
robotService = RobotService()


@app.post("/api/v1/find/robot")
async def findRobot(request: Request, requestBody: RobotsRequestDto):
    try:
        robotText = await robotService.findRobotText(requestBody.url)
        robotText = cleanData(robotText)
        return RobotsSuccessResponseDto(200, robotText)
    except:
        dto = RobotsFailResponseDto(status=500, errorCode=1, errorUrl=requestBody.url)
        return dto
