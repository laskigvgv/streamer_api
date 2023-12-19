from flask import Flask, render_template, request, Response, send_file
from pytube import YouTube, Search
from utils import spotify_client
from utils.spotify_client import stream_to_buffer, audio_from_buffer, get_tracks
from io import BytesIO
import json
import base64
import time
import threading


app = Flask(__name__, template_folder="templates")


@app.route("/get")
def play_audio():
    tracks = get_tracks()
    print(type(tracks))
    buffer = BytesIO()
    # urls = [
    #     "https://www.youtube.com/watch?v=sqSA-SY5Hro",
    #     "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    #     "https://www.youtube.com/watch?v=sYC0B7-NLUg",
    # ]

    # threads = []
    # for url in urls:
    #     thread = threading.Thread(target=stream_to_buffer, args=(buffer, url))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    yt_url = "https://www.youtube.com/watch?v=sqSA-SY5Hro"
    stream_to_buffer(buffer, yt_url)

    audio = audio_from_buffer(buffer)

    buffer_base64 = b"".join(audio)
    base64_data = base64.b64encode(buffer_base64).decode()
    print("test ", len(base64_data))

    return render_template("index.html", audio_file=base64_data)
    # return "da dad aaaaaaa"


if __name__ == "__main__":
    host = "0.0.0.0"
    app.run(debug=True, host=host, port=5444)
