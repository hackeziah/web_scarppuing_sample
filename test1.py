import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www14.mp4upload.com:282/d/qwx5v3taz3b4quuo4wuqe2ssjoju6xzot6adisbglapt7l6blnxslrob/video.mp4'

r = requests.get(url, stream = True,verify=False)
with open('test.mp4', 'wb') as f:
     for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
            f.write(chunk)
