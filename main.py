from pyrogram import filters,Client
from pyromod import listen
import validators
import asyncio

api_id = 27690446
api_hash = "d56f7ac259b7c1dab704103ee45b0927"
bot_token = "7244121655:AAHbyHRnT2KA98TnYP1K8tvDblPICU7Gp7g"

# app = Client("UFDBOT0037", api_id=api_id, api_hash=api_hash)
app = Client("UFDBOT0037")


async def upload_file(url):
    async def progress(current, total):
        print(f"{current * 100 / total:.1f}%")
    await app.send_document("@UFD0037Bot", document=url, progress=progress)


@app.on_message(filters.command(["start"]))
async def my_handler(client, message):
    chat=message.chat
    await app.send_message("@UFD0037Bot", "UDF Bot is Alive !")
    URL = await chat.ask('Please send URL to upload file', filters=filters.text)
    is_url_valid=validators.url(URL.text)
    while is_url_valid != True:
        await app.send_message("@UFD0037Bot", "URL is invalid !")
        URL=await chat.ask('Please send URL again to upload file', filters=filters.text)
        is_url_valid=validators.url(URL.text)
    await upload_file(URL.text)

    

app.run()
