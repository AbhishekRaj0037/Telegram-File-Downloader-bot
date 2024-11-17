import asyncio
from pyrogram import Client,filters

api_id = 27690446
api_hash = "d56f7ac259b7c1dab704103ee45b0927"
bot_token = "7244121655:AAHbyHRnT2KA98TnYP1K8tvDblPICU7Gp7g"

# app = Client("UFDBOT0037", api_id=api_id, api_hash=api_hash)
app = Client("UFDBOT0037")

@app.on_message(filters.command('start'))
def welcome(app,message):
    app.send_message(message.chat.id,"Welcome to UFDBot")
    app.send_message(message.chat.id,"Please send link to upload file")
        


app.run()
