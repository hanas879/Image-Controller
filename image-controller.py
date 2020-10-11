import json
import os.path

if os.path.isfile("sources.json") == False:
    with open("sources.json","w") as f:
        f.write("{}")

def saveSources():
    with open("sources.json") as f:
        sources = json.load(f)

    sources["Ubuntu"] = "PLACEHOLDER"

    with open("sources.json", "w") as f:
        json.dump(sources, f, indent=2)
