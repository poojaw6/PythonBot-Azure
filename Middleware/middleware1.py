#Middleware will be always invoked before the logic for bot is executed
from botbuilder.core import Middleware, TurnContext
from typing import Callable,Awaitable
from botbuilder.schema import ActivityTypes

#next() method is used to transfer control to the next middleware or bot for further steps

class Middleware1(Middleware):
    async def on_turn(self,turn_context:TurnContext,next:Callable[[TurnContext],Awaitable]):
        if turn_context.activity.type == ActivityTypes.message:
            await turn_context.send_activity("Hey I am Middleware 1")
            await next()
            await turn_context.send_activity("called after your bot")