import json
import os.path
import wget

def checkJSON():
    if os.path.isfile("sources.json") == False:
        with open("sources.json","w") as f:
            f.write("{}")

def saveSources():
    with open("sources.json") as f:
        sources = json.load(f)

    sources["Distro"] = "PLACEHOLDER"

    with open("sources.json", "w") as f:
        json.dump(sources, f, indent=2)

def downloadFile(url):
    wget.download(url)
