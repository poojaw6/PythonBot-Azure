from botbuilder.core import TurnContext, ActivityHandler, RecognizerResult, MessageFactory
from botbuilder.ai.luis import LuisApplication, LuisPredictionOptions, LuisRecognizer


class LuisBot(ActivityHandler):
    def __init__(self):
        #Application id, endpoint key and endpoint url of LUIS from luis.ai
        luis_app = LuisApplication("7f01b098-aa58-4b4d-883d-9437b4c76c90","3ebb4461514e49cab8142d2df7e18561","https://westus.api.cognitive.microsoft.com/")
        luis_option = LuisPredictionOptions(include_all_intents=True, include_instance_data=True)
        self.LuisReg = LuisRecognizer(luis_app,luis_option,True)

    #whenever text arrives from client send the text to luis model
    async def on_message_activity(self, turn_context:TurnContext):
        luis_result = await self.LuisReg.recognize(turn_context)
        #extract top intent
        intent = LuisRecognizer.top_intent(luis_result)
        await turn_context.send_activity(f"Top Intent: {intent}")
        result = luis_result.properties["luisResult"]
        await turn_context.send_activity(f"Luis Result: {result.entities[0]}")