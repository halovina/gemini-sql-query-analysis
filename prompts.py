import mesop as me
from data_model import State, ChatMessage, Conversation
import gemini
from read_sql import read_sales_order


prompt_format = ["""
          Ubah pertanyaan bahasa indonesia ke SQL Query!
          SQL Database name nya adalah example dengan nama table sales_order mempunyai nama kolom order_id, partner_id, item_id, item_quantity, total_selling_price, sales_channel, order_date, customer_id.
          \nExample 1 - berapa banyak jumlah seluruh record yang ada ?
          \nExample 2 - ceritakan semua data sales channel yang ada, dengan contoh perintah SQL seperti 
          select * from sales_order where sales_channel = 'AAA'
          dan juga sql query tidak punya ``` di awal dan akhir
          serta hasilnya satu query SQL SAJA !
"""]


def send_prompt(e: me.ClickEvent):
    state = me.state(State)
    if not state.conversations:
        state.conversations.append(Conversation(messages=[]))
    
    input = state.input
    state.input = ""
    
    for conversation in state.conversations:
        messages = conversation.messages
        messages.append(ChatMessage(role="user", content=input))
        messages.append(ChatMessage(role="model", in_progress=True))
        yield
        
        me.scroll_into_view(key="end_of_messages")
        llm_message = gemini.send_prompt_flash(input, prompt_format)
        print(llm_message)
        sqldata = read_sales_order(llm_message)
        for row in sqldata:
            messages[-1].content += str(row)
            yield
            
        messages[-1].in_progress = False
        yield