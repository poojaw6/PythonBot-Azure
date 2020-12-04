from botbuilder.core import TurnContext, ActivityHandler, CardFactory
from botbuilder.schema import Activity, Attachment,  ActivityTypes
#MessageFactory to turn card to activity
#CardFactory to convert card to message
import json
import os

CARD = "/Users/pwalavalkar/Downloads/PythonBot/Adaptive Card/adaptivecard/ratingcard.json"

class SampleAdaptiveCard(ActivityHandler):
    def __init__(self):
        pass

    async def on_message_activity(self, turn_context:TurnContext):
        message = Activity(
            text="Here is an adaptive card:",
            type= ActivityTypes.message,
            attachments=[self._create_feedbackcard_att()]
        )
        await turn_context.send_activity(message)

    def _create_feedbackcard_att(self) -> Attachment:
        card_path = os.path.join(os.getcwd(),CARD)
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)
        return CardFactory.adaptive_card(card_data)

      
