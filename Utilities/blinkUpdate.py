import requests
moduleName = requests.head("https://raw.githubusercontent.com/Blinkhub/blinkModules/master/" + args.install + ".zip")
if moduleName.status_code == requests.codes.ok:
