class RobotsSuccessResponseDto:
    status = None
    content = None

    def __init__(self, status, content):
        self.status = status
        self.content = content

    def getDto(self):
        dto = dict()
        dto["status"] = self.status
        dto["content"] = self.content
        return dto


class RobotsFailResponseDto:
    status = None
    errorCode = None
    errorContent = None
    errorUrl = None
    ERROR_1_MESSAGE = "해당 주소의 ROBOTS.TXT를 찾을 수 없습니다."

    def __init__(self, status, errorCode, errorUrl):
        self.status = status
        self.errorCode = errorCode
        self.errorUrl = errorUrl
        if errorCode == 1:
            self.errorContent = self.ERROR_1_MESSAGE

    def getDto(self):
        dto = dict()
        dto["status"] = self.status
        dto["errorCode"] = self.errorCode
        dto["errorContent"] = self.errorContent
        dto["errorUrl"] = self.errorUrl
        return dto
