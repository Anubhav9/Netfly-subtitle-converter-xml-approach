import os
from time import sleep
import threading

import requests
from playwright.sync_api import sync_playwright
import click

from app import translate_the_subtitles

subtitle_xml_file_link=[]

def handle_request(request):
    # Filter requests to match subtitle XML files
    if "/?o=" in request.url:
        print(f"Request URL is: {request.url}")
        subtitle_xml_file_link.append(request.url)


def fetch_the_subtitles(video_url):
    with sync_playwright() as playwright:
        browser=playwright.webkit.launch(headless=False,args=["--enable-eme", "--enable-media"])
        context=browser.new_context(accept_downloads=True)
        page=context.new_page()
        page.goto("https://www.netflix.com")
        username=os.environ.get("NETFLIX_USERNAME")
        password=os.environ.get("NETFLIX_PASSWORD")
        page.get_by_role("button",name="Sign In").click()
        sleep(10)
        page.get_by_label("Email or mobile number").fill(username)
        page.get_by_label("Password").fill(password)
        page.get_by_role("button",name="Sign In").click()
        sleep(10)
        page.goto(video_url)
        sleep(10)
        page.goto(video_url)
        page.on("request",handle_request)
        print("Waiting for subtitle XML file...")
        for _ in range(120):  
            if subtitle_xml_file_link:
                break
            page.wait_for_timeout(1000)  

        # If no subtitle link is found
        if not subtitle_xml_file_link:
            print("No subtitle file link was captured.")
            browser.close()
            return
        page.goto(subtitle_xml_file_link[0])
    response=requests.get(subtitle_xml_file_link[0])
    response.encoding = 'utf-8'
    content=response.text
    with open("subtitles.xml","w",encoding="utf-8") as f:
        f.write(content)

@click.command()
@click.option("-u","--username",required=True,help="Your NetFlix UserName")
@click.option("-p","--password",required=True,help="Your NetFlix Password")
@click.option("-v","--video_url",required=True,help="The Netflix Video URL")
def cli_command(username,password,video_url):
    os.environ["NETFLIX_USERNAME"]=username
    os.environ["NETFLIX_PASSWORD"]=password
    fetch_the_subtitles(video_url)
    thread = threading.Thread(target=translate_the_subtitles, args=("subtitles.xml",))
    thread.start()
    click.echo("Awesome, subtitles are being translated. Please wait for a while. It should be available in a file named translated_subtitles.json soon.")
if __name__=='__main__':
    cli_command()
