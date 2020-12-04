from botbuilder.core import TurnContext, ActivityHandler, MessageFactory
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint

class QnABot(ActivityHandler):
    def __init__(self):
        qna_endpoint = QnAMakerEndpoint("ea9c386a-53e0-4dc4-95d5-ecae7cfa1a42","d777e3f4-52d1-4a86-a75d-a97ede3fa509","https://testqnamaker001.azurewebsites.net/qnamaker")
        self.qna_maker = QnAMaker(qna_endpoint)


    async def on_message_activity(self, turn_context:TurnContext):
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response)>0 :
            await turn_context.send_activity(MessageFactory.text(response[0].answer))