from collections import defaultdict
from random import sample

import attr
import os
import requests
import re

REPO = "mozfest-program-2018"
ORG = "MozillaFestival"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

TRACKS = [
    "Decentralisation",
    "Digital Inclusion",
    "Openness",
    "Privacy and Security",
    "Web Literacy",
    "Youth Zone",
    "Queering MozFest"
]

@attr.s
class MozfestEvent(object):
    id = attr.ib()
    title = attr.ib()
    # Only getting one speaker for now
    speakers = attr.ib()
    # milestone
    track = attr.ib()
    duration = attr.ib()


def download_events_list():
    r = requests.get(f"https://api.github.com/repos/{ORG}/{REPO}/issues?access_token={GITHUB_TOKEN}")

    events = r.json()

    # Uncomment when want to run on all proposals (700+ issues)
    # while r.links.get("next"):
    #     r = requests.get(r.links["next"]["url"])
    #     events.extend(r.json())

    return events

def get_speaker(event):
    body = event["body"]
    speaker_regex = re.search("(?<=\[\sSubmitter's Name\s\]\*\*\s).*(?=\s\*\*)", body)

    speaker = speaker_regex.group(0)

    return speaker

# Multiple format: "90 min", "less than 90 min" or "All weekend, as an installation, exhibit or drop-in session"
def get_duration():
    pass

# parse list to create MozfestEvent objects
def create_mozfest_event(json_data):
    all_events = []

    for event in json_data:
        # Skipping it for now because someone entered an issue manually and it messes things around!
        if event["milestone"] is None:
            pass
        else:
            speaker = get_speaker(event)
            all_events.append(MozfestEvent(
                id=event["id"],
                title=event["title"],
                speakers=speaker,
                track=event["milestone"]["title"],
                # Set the same time for all. Fixing this later.
                duration=30,
            ))

    return all_events

# Separate all tracks per tracks
def split_per_tracks(all_events):
    result = defaultdict(list)

    for event in all_events:
        result[event.track].append(event)

    return result

# Create a json file with 42 events: sample (random)
# Get 6 events per 7 days (42 events)
def select_events(events):
        return sample(events, 2)

# Create Event object from the selected events
"""
>>> from conference_scheduler.resources import Event
>>>
>>> events = {'talk': [
...     Event(
...         talk['title'], talk['duration'], demand=None,
...         tags=talk.get('tags', None))
...     for talk in events]}

>>> pprint(events['talk'][0:3])"""

# Create a venue with rooms

# Generate conflict for speakers, rooms, events

# Generate schedule

# export it in a tab?

if __name__ == '__main__':
    # prepare data sample
    events_list = download_events_list()
    events_list = create_mozfest_event(events_list)
    events_grouped_by_tracks = split_per_tracks(events_list)

    # Select events randomly to create our schedule
    selected_events = select_events(events_grouped_by_tracks)



