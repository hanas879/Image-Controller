import json
import os
import os.path
import wget
from bs4 import BeautifulSoup
import requests

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def grabIso(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")

    news = soup.find("td", class_="NewsText")
    links = news.find_all("a")
    for i in links:
        if ".iso" in i["href"] and "64" in i["href"]:
            return i["href"]
            break


def checkJSON():
    if os.path.isfile("sources.json") == False:
        with open("sources.json","w") as f:
            f.write("{}")


def saveSources(distro, url):
    with open("sources.json") as f:
        sources = json.load(f)

    sources[distro] = url

    with open("sources.json", "w") as f:
        json.dump(sources, f, indent=2)


def downloadFile(url):
    print("Downloading: " + url)
    print()
    wget.download(url)


def menu():
    clear()
    print("What would you like to do?")
    print()
    print("1. Add URL to JSON")
    print("2. Download a specific URL one time")
    print("3. Exit")
    print()
    choice = input()
    clear()
    if choice == "1":
        print("Enter distro NAME:")
        distroName = input()
        clear()
        print("Enter URL:")
        distroUrl = input()
        clear()
        saveSources(distroName,distroUrl)
        menu()
    elif choice == "2":
        clear()
        downloadFile(input("Enter URL to file:"))
        menu()
    elif choice == "3":
        pass
    else:
        menu()


checkJSON()
menu()
