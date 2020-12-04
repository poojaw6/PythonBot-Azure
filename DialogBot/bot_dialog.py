#In this dialog get username phonenum and emailid

from botbuilder.core import TurnContext, ActivityHandler, ConversationState, MessageFactory
from botbuilder.dialogs import DialogSet, WaterfallDialog, WaterfallStepContext
#Username and email id are text and mobile number is number prompt
from botbuilder.dialogs.prompts import TextPrompt, NumberPrompt, PromptOptions, PromptValidatorContext
#PromptOptions is an Activity Object. MessageFactory converts prompt text to activity
#PromptValidatorContext for custom validations

class BotDialog(ActivityHandler):
    def __init__(self, conversation:ConversationState):
        #get the state of conversation and store in a variable
        self.con_state = conversation
        
        #state property needs to be created from con state of conversation
        self.state_prop = self.con_state.create_property("dialog_set")
        #create dialogset - stateproperty is needed
        self.dialog_set = DialogSet(self.state_prop)
        #define dialog set, what all dialogs are going to be used
        self.dialog_set.add(TextPrompt("text_prompt"))
        self.dialog_set.add(NumberPrompt("number_prompt",self.IsValidMobileNumber)) #Adding custom validation logic
        #define the steps, which question will be asked in sequence
        self.dialog_set.add(WaterfallDialog("main_dialog",[self.GetUserName,self.GetMobileNumber, self.GetEmailId, self.Completed]))

    async def IsValidMobileNumber(self, prompt_valid:PromptValidatorContext):
        if(prompt_valid.recognized.succeeded is False):
            await prompt_valid.context.send_activity("Hey please enter the number")
        else:
            value = str(prompt_valid.recognized.value)
            if len(value)<10:
                await prompt_valid.context.send_activity("Please enter a valid mobile number")
                return False
        return True

    
    async def GetUserName(self, waterfall_step:WaterfallStepContext):
        return await waterfall_step.prompt("text_prompt",PromptOptions(prompt=MessageFactory.text("Please enter the name")))

    async def GetMobileNumber(self, waterfall_step:WaterfallStepContext):
        #bot has got username from previous step
        name = waterfall_step._turn_context.activity.text
        waterfall_step.values["name"] = name
        return await waterfall_step.prompt("number_prompt",PromptOptions(prompt=MessageFactory.text("Please enter the mobile number")))

    async def GetEmailId(self, waterfall_step:WaterfallStepContext):
        #bot has got mobile number from previous step
        mobile = waterfall_step._turn_context.activity.text
        waterfall_step.values["mobile"] = mobile
        return await waterfall_step.prompt("text_prompt", PromptOptions(prompt=MessageFactory.text("Please enter the email id")))

    #End dialog to close the conversation
    async def Completed(self, waterfall_step:WaterfallStepContext):
        #bot has got email from previous step
        email = waterfall_step._turn_context.activity.text
        waterfall_step.values["email"] = email
        #Retrieve the stored data
        name = waterfall_step.values["name"]
        mobile = waterfall_step.values["mobile"]
        email = waterfall_step.values["email"]

        #send profile info to back to the user
        profileinfo = f"name : {name}, email: {email}, mobile : {mobile}"
        await waterfall_step._turn_context.send_activity(profileinfo)
        return await waterfall_step.end_dialog()

    
    #Check what is the current context of the dialog. If the conversation is going on then continue the dialog elsebegin a new chat
    async def on_turn(self, turn_context:TurnContext):
        dialog_context = await self.dialog_set.create_context(turn_context)

        if(dialog_context.active_dialog is not None):
            await dialog_context.continue_dialog()
        else:
            await dialog_context.begin_dialog("main_dialog") #start of Waterfalldialog
        #always save the conversation state to keep the context else it will always assume that its the begining of the chat
        await self.con_state.save_changes(turn_context)



        