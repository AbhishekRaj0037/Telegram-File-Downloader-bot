from pyrogram import filters,Client,idle
from urllib.parse import urlparse
from pyromod import listen
import urllib.request
import validators
import requests
import asyncio
import os


# api_id = 27690446
# api_hash = "d56f7ac259b7c1dab704103ee45b0927"
# bot_token = "7244121655:AAHbyHRnT2KA98TnYP1K8tvDblPICU7Gp7g"

# app = Client("UFDBOT0037", api_id=api_id, api_hash=api_hash)
app = Client("UFDBOT0037")

async def upload_file(filename):
    try:
        async def progress(current, total):
            print(f"Uploading file : {current * 100 / total:.1f}%  ↑...↑...↑")
        await app.send_document("@UFD0037Bot", document=filename, progress=progress)
        print(f"File Uploaded successfully as {filename} (＾▽＾)")
        await app.send_message("@UFD0037Bot", "File Uploaded successfully !")
        await app.send_message("@UFD0037Bot", "Here is your file")
        os.remove(filename)
    except:
        print("Some error occurred (×_×)")
        await app.send_message("@UFD0037Bot", "Some error occurred please try again")

async def download_file(url):
    try:
        print("Downloading file please wait  ↓...↓...↓")
        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an exception for bad status codes (e.g., 404 or 500)
        response.raise_for_status()
        
        # Get the content type from the response headers
        # content_type = response.headers.get('Content-Type')
        
        # Generate a filename based on the URL or content type if no filename is found
        filename = os.path.basename(urlparse(url).path) or 'downloaded_file'
        # breakpoint()
        # # If the content type suggests a specific type, try adding an appropriate extension
        # if 'image' in content_type:
        #     filename += '.jpg'
        # elif 'pdf' in content_type:
        #     filename += '.pdf'
        # elif 'text' in content_type:
        #     filename += '.txt'
        # elif 'zip' in content_type:
        #     filename += '.zip'
        # elif 'video' in content_type:
        #     filename+= '.mp4'
        # # Add other content types as necessary
        
        # # Save the file to the current directory
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"File downloaded successfully as {filename} (＾▽＾)")
        return filename
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e} (×_×)")
        await app.send_message("@UFD0037Bot", "Some error occurred please try again")
    

@app.on_message(filters.command(["start"]))
async def my_handler(client, message):
    chat=message.chat
    await app.send_message("@UFD0037Bot", "UDF Bot is Awake (•_•)")
    URL = await chat.ask('Please send URL to upload file', filters=filters.text)
    is_url_valid=validators.url(URL.text)
    current_attempt=1
    max_attempt=5
    while is_url_valid != True and current_attempt<=max_attempt:
        await app.send_message("@UFD0037Bot", "URL is invalid !")
        URL=await chat.ask('Please send a valid URL to upload file', filters=filters.text)
        is_url_valid=validators.url(URL.text)
        current_attempt=current_attempt+1
    if current_attempt>max_attempt:
        await app.send_message("@UFD0037Bot", "Sleeping (-_-)zzz")
        await idle()
    filename= await download_file(URL.text)
    await upload_file(filename)


    

app.run()
