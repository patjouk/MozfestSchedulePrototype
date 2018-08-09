import requests
import os

REPO = "mozfest-program-2018"
ORG = "MozillaFestival"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

def create_tracks_list():
    tracks = []
    r = requests.get(f"https://api.github.com/repos/{ORG}/{REPO}/milestones?access_token={GITHUB_TOKEN}")

    r = r.json()

    for i in r:
        tracks.append(i["title"])

    print(tracks)
    return tracks

if __name__ == '__main__':
    create_tracks_list()
