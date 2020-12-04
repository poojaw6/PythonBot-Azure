from botbuilder.core import TurnContext, ActivityHandler
from botbuilder.schema import ActivityTypes,ChannelAccount

#AcivityHandler class is used to do the commented code - just override the methods with your logic

#returns same message back to the user that he/she has sent
class EchoBot(ActivityHandler):
    async def on_message_activity(self,turn_context:TurnContext):
        await turn_context.send_activity(turn_context.activity.text)
    #conversation update event
    async def on_members_added_activity(self,member_added : ChannelAccount, turn_context:TurnContext):
        await turn_context.send_activity("Hello and Welcome to Echo Bot!!")



    """async def on_turn(self,turn_context:TurnContext):
        if turn_context.activity.type == ActivityTypes.conversation_update:
            await turn_context.send_activity("Hello and Welcome to Echo Bot!")
        if turn_context.activity.type == ActivityTypes.message:
            await turn_context.send_activity(turn_context.activity.text)"""