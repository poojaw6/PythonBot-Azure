from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.components import TextBlock, Choice
from pyadaptivecards.actions import Submit

class FeedbackCard():
    def __init__(self):
        pass
    
    
    def create_feedback_card(self):
        greeting = TextBlock("Did you like the new chatbot?",size="medium",weight="bolder")
        act1 = Submit(title="Yes",data="yes")
        act2 = Submit(title="No", data="no")

        card1 = AdaptiveCard(body=greeting,actions=[act1,act2])
        card1_json = card1.to_json(pretty=True)
        return card1_json

