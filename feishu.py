import requests
import json
import os

FEISHU_URL = os.getenv("FEISHU_URL")

def send_feishu(text):

    if not FEISHU_URL:
        print("No FEISHU_URL")
        return

    data = {
        "msg_type": "text",
        "content": {
            "text": text
        }
    }

    r = requests.post(
        FEISHU_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )

    print(r.text)