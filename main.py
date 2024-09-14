import mesop as me
from data_model import State
from prompts import send_prompt
from conversations import model_conversation


ROOT_BOX_STYLE = me.Style(
    background="#e7f2ff",
    height="100%",
    font_family="Inter",
    display="flex",
    flex_direction="column",
)

STYLESHEETS = [
  "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
]


def header():
    def navigate_home(e: me.ClickEvent):
        me.navigate("/")
        state = me.state(State)
        state.conversations = []
    with me.box(
        on_click=navigate_home,
        style=me.Style(
            cursor="pointer",
            padding=me.Padding.all(16),
        ),
    ):
        me.text(
            text="Gemini Text to SQL",
            style=me.Style(
                font_weight=500,
                font_size=24,
                color="#3D3929",
                letter_spacing="0.3px",
            ),
        )

@me.page(path="/", stylesheets=STYLESHEETS)
def app():
    state = me.state(State)
    with me.box(style=ROOT_BOX_STYLE):
        header()
            
        with me.box(
            style=me.Style(
                display="flex",
                justify_content="center",
            )
        ):
            with me.box(
                style=me.Style(
                    width="min(680px, 100%)",
                    padding=me.Padding(top=24, bottom=24),
                )
            ):
                me.text(
                    text="SQL Database name : example, nama table sales_order,  kolom : (order_id, partner_id, item_id, item_quantity, total_selling_price, sales_channel, order_date, customer_id.)",
                    style=me.Style(
                        font_weight=500,
                        font_size=16,
                        color="#3D3929",
                        letter_spacing="0.3px",
                    ),
                )
                promp_input()
        
        models = len(state.conversations)
        models_px = models * 680
        with me.box(
            style=me.Style(
                 background="#e7f2ff",
                width=f"min({models_px}px, calc(100% - 32px))",
                height=500,
                display="grid",
                gap=16,
                grid_template_columns=f"repeat({models}, 1fr)",
                flex_grow=1,
                margin=me.Margin.symmetric(horizontal="auto"),
                padding=me.Padding.symmetric(horizontal=16),
            )
        ):
           model_conversation()
            
                
                        
                        
def promp_input():
    state = me.state(State)
    with me.box(
        style=me.Style(
            border_radius=16,
            padding=me.Padding.all(8),
            background="white",
            display="flex",
            width="100%",
        )
    ):
        with me.box(style=me.Style(flex_grow=1)):
            me.textarea(
                value=state.input,
                placeholder="Enter a prompt",
                on_blur=on_blur,
                style=me.Style(
                    padding=me.Padding(top=16, left=16),
                    outline="none",
                    width="100%",
                    border=me.Border.all(me.BorderSide(style="none")),
                ),
            )
            
            with me.box(
                style=me.Style(
                    padding=me.Padding(top=16, left=16),
                )
            ):
                me.button(
                    label="SUBMIT",
                    type="stroked",
                    on_click=send_prompt
                )           
                
  
def on_blur(e: me.InputBlurEvent):
    state = me.state(State)
    state.input = e.value
    
    

