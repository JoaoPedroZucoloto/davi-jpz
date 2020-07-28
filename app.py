import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
#WP_API_URL  = 'https://graph.facebook.com/v2.6/me?fields=id,name?access_token=DQVJ2aGJTemxSZAXhpNU5TZAVdxNFk2a0FYRzFHd2FqS3MwVFBRMkJVeFhudVBnS3ZAwWjRBOU41alpDbXlIUnN0ejNBZA0ZARSUV1NWE5dTN5dDVNTzlMazlEMWRweHBYbDVaTENOQWFrcE5mWmlEamU2cWtwRTVWSklkR050aEN0SFVhamV4ZAEY4RndJZA0QtakFUVEtyMUQxRmFaVVh6OHdxLWNjZAVJQUDk0RXlJQ2lkdW1YUFZAQSkJXSF9Ed2UyRkJnLTl1ZAW9R'

r = requests.get("https://graph.facebook.com/v7.0/me?fields=id%2Cname&access_token=DQVJ2aGJTemxSZAXhpNU5TZAVdxNFk2a0FYRzFHd2FqS3MwVFBRMkJVeFhudVBnS3ZAwWjRBOU41alpDbXlIUnN0ejNBZA0ZARSUV1NWE5dTN5dDVNTzlMazlEMWRweHBYbDVaTENOQWFrcE5mWmlEamU2cWtwRTVWSklkR050aEN0SFVhamV4ZAEY4RndJZA0QtakFUVEtyMUQxRmFaVVh6OHdxLWNjZAVJQUDk0RXlJQ2lkdW1YUFZAQSkJXSF9Ed2UyRkJnLTl1ZAW9R")


def send_message(recipient_id, text): 
    response = requests.post(WP_API_URL, headers=WP_HEADER, data=json.dumps({
        'recipient' : {'id'   : recipient_id},
        'message'   : {'text' : text}
    }))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
