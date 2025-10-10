import os
import re
import json

video_folder = "./videos"
tv_show_pattern = re.compile(r"(?P<title>.+)_S(?P<season>\d+)E(?P<episode>\d+)_?(?P<quality>HD|720p|1080p)?", re.IGNORECASE)
movie_pattern = re.compile(r"(?P<title>.+)\.(?P<year>\d{4})\.(?P<quality>1080p|720p|HD)", re.IGNORECASE)

video_metadata = []

for filename in os.listdir(video_folder):
    if not filename.lower().endswith(('.mp4', '.mkv')):
        continue
    match = tv_show_pattern.match(filename)
    if match:
        data = match.groupdict()
        data['type'] = 'TV Show'
        data['filename'] = filename
        video_metadata.append(data)
        continue
    match = movie_pattern.match(filename)
    if match:
        data = match.groupdict()
        data['type'] = 'Movie'
        data['filename'] = filename
        video_metadata.append(data)
        continue
    video_metadata.append({"filename": filename, "type": "Unknown"})

with open("video_library.json", "w") as f:
    json.dump(video_metadata, f, indent=4)

print("Metadata extracted and saved to video_library.json")