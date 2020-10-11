import json

def saveSources():
    with open("sources.json") as f:
        sources = json.load(f)

    sources["Ubuntu"] = "PLACEHOLDER"

    with open("sources.json", "w") as f:
        json.dump(sources, f, indent=2)
