import aiohttp
import asyncio


class RobotService:
    ROBOT_TEXT = "robots.txt"

    def addText(self, url):
        if url[-1] == "/":
            url += self.ROBOT_TEXT
        else:
            url += "/" + self.ROBOT_TEXT
        if url[:3] == "www":
            url = "https://" + url
        return url

    async def getText(self, session, url):
        async with session.get(url) as response:
            result = await response.read()
            return result

    async def findRobotText(self, url):
        url = self.addText(url)

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            return await asyncio.gather(self.getText(session, url))
