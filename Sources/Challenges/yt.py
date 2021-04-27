from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=5eDNvfhCmz0")
t=yt.streams.filter(only_audio=True).all()
t[0].download("H:")
