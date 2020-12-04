#Bot Framework is a web application based framework which requires Flask
#now we ill write base code of Flask to run basic application
from flask import Flask, request, Response
#Activity is schema of bot framework
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
#import echbot function here to get the turn_on context
from echobot import EchoBot

#since the function should not come out of the async function prematurely
import asyncio

app = Flask(__name__)
#This lopp will run until end of async function ends
loop = asyncio.get_event_loop()

#give appid and passowrd
botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)
ebot = EchoBot()

#We will be posting HTTP message
@app.route("/api/messages", methods=["POST"])

def messages():
    #check the message format (bot supporting file format)
    #check whether the HTTP type header is json or not
    if "application/json" in request.headers["content-type"]:
        jsonmessage = request.json
    else:
        #415 is unsupported media type
        return Response(status=415)

    
    #convert json message to activity
    activity = Activity().deserialize(jsonmessage)

    #method to send the activity to bot and get the turn_context
    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

    #Pass this activity to Adapter object
    #botadapter.process_activity(activity, "",turn_call)

    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)

    #Now the message has reached the bot, now bot will have to send response activity back

if __name__ == '__main__':
    app.run('localhost', 3978)
    
        
