import os
import requests

def download_issues_github():
    repo = "mozfest-program-2018"
    org = "MozillaFestival"
    github_token = os.environ["GITHUB_TOKEN"]

    r = requests.get(f"https://api.github.com/repos/{org}/{repo}/issues?access_token={github_token}")

    issues_list = r.json()

    while r.links.get["next"]:
        r = requests.get(r.links["next"]["url"])
        issues_list.append(r.json())

# DL issue from github and create JSON file

# Select 6 talks * 7 days for each milestone

# Create a venue with rooms

# Generate conflict for speakers, rooms, talks

# Generate schedule

# export it in a tab?

if __name__ == '__main__':
    download_issues_github()
