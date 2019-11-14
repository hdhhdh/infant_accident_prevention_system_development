import boto3
import time
import telepot
import os

from telepot.loop import MessageLoop

genietoken = "995744506:AAET7sM5GvDTBlWQHhkaxUuGlHxsva7Zkng"
bot = telepot.Bot(genietoken)

InfoMsg = "press the Number\n" \
          "1. Streaming URL"

status = True


STREAM_ARN = 'arn:aws:kinesisvideo:ap-northeast-1:775569069943:stream/mystream/1571636767275'
kvs = boto3.client("kinesisvideo","ap-northeast-1")
#kvs = boto3.client("kinesisvideo")
# Grab the endpoint from GetDataEndpoint
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamARN=STREAM_ARN
)['DataEndpoint']
# Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media", endpoint_url=endpoint)
url = kvam.get_hls_streaming_session_url(
    StreamARN=STREAM_ARN,
    PlaybackMode='LIVE'
)['HLSStreamingSessionURL']
print(url)


from IPython.display import HTML
HTML(data='<video src="{0}" autoplay="autoplay" controls="controls" width="300" height="400"></video>'.format(url))

def handle(msg):
    content, chat, id = telepot.glance(msg)
    print(content, chat, id)

    global url

    if content == 'text':
        if msg['text'] == '1':
            bot.sendMessage(id, url)
        else:
           bot.sendMessage(id, InfoMsg)

#bot.message_loop(handle)
MessageLoop(bot, handle).run_as_thread()
while status == True:
    time.sleep(10)
