import mesop as me
from data_model import State, ChatMessage

def model_conversation():
    state = me.state(State)
    for convesation in state.conversations:
        messages = convesation.messages
        with me.box(
            style=me.Style(
                overflow_y = "auto"
            )
        ):
            for message in messages:
                if message.role == "user":
                    user_message(message.content)
                else :
                    model_message(message)
                    
            me.box(
                    key="end_of_messages",
                    style=me.Style(
                        margin=me.Margin(
                            bottom="50vh" if messages[-1].in_progress else 0
                        )
                    ),
                )
                    
def user_message(content: str):
    with me.box(
        style=me.Style(
            background="#e7f2ff",
            padding=me.Padding.all(15),
            margin=me.Margin.symmetric(vertical=16),
            border_radius=16
            
        )
    ):
        me.text(
            text="User message: {}".format(content)
        )
        
def model_message(message: ChatMessage):
    with me.box(
        style=me.Style(
            background="white",
            padding=me.Padding.all(15),
            margin=me.Margin.symmetric(vertical=16),
            border_radius=16
            
        )
    ):
        me.markdown(
            text=message.content
        )
        
        if message.in_progress:
            me.progress_spinner()
        message.in_progress=False