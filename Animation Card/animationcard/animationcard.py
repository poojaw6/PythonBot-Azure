from botbuilder.core import TurnContext, ActivityHandler,MessageFactory, CardFactory
#MessageFactory to turn card to activity
#CardFactory to convert card to message
from botbuilder.schema import AnimationCard,Attachment,MediaUrl

class SampleAnimationCard(ActivityHandler):
    def __init__(self):
        pass

    async def on_message_activity(self, turn_context:TurnContext):
        #convert animation card to attachments >> to message factory
        cardAtt = self.create_animation_card()
        #convert msg to activity
        msg_activity = MessageFactory.attachment(cardAtt)
        await turn_context.send_activity(msg_activity)


    def create_animation_card(self) -> Attachment:
        card = AnimationCard(media=[MediaUrl(url="https://media.giphy.com/media/fxe8v45NNXFd4jdaNI/giphy.gif")],title="Sample Animation Card",subtitle="Bye Bye")
        return CardFactory.animation_card(card)
