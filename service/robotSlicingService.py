def cleanData(data):
    data = str(data[0])[2:-1]
    datas = data.split("\\n")
    result = dict()
    result["permit"] = []
    result["notAllowed"] = []
    result["permitBots"] = []
    check = False
    for d in datas:
        try:
            f, b = d.split(": ")
            if f == "User-agent" and b != "*":
                result["permitBots"].append(b)
            if f == "User-agent" and b == "*":
                check = True
                continue
            if check and f == "User-agent":
                check = False
            if check and f == "Disallow":
                result["notAllowed"].append(b)
            if check and f == "Allow":
                result["permit"].append(b)
        except:
            pass

    return result
