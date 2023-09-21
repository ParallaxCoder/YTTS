import os
import argparse
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import re


async def is_youtube_url(url):
    youtube_watch_url_pattern = r"https?://www.youtube.com/watch\?v=[\w-]+"
    youtube_short_url_pattern = r"https?://youtu.be/[\w-]+"

    return re.match(youtube_watch_url_pattern, url) or re.match(youtube_short_url_pattern, url)


async def replace_youtube_url(url):
    youtube_watch_url = "https://www.youtube.com/watch"
    youtube_short_url = "https://youtu.be/"
    transcript_url = "https://youtubetranscript.com/"

    if youtube_watch_url in url:
        video_id = url.split("=")[-1]
        new_url = transcript_url + "?v=" + video_id
        return new_url, video_id
    elif youtube_short_url in url:
        video_id = url.split("/")[-1]
        new_url = transcript_url + "?v=" + video_id
        return new_url, video_id

    return None, None


async def scrape_transcript(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    # Wait for the transcript to load (modify the sleep duration as needed)
    await asyncio.sleep(5)
    transcript_html = await page.evaluate("document.getElementById('demo').innerHTML")
    await browser.close()

    soup = BeautifulSoup(transcript_html, "html.parser")
    transcript_text = soup.get_text(separator="\n")
    transcript_text = transcript_text.replace("\n", " ")  # Replace newlines with spaces
    return transcript_text


async def process_youtube_url(url):
    is_youtube = await is_youtube_url(url)

    if not is_youtube:
        print(f"Unsupported URL: {url}")
        return False

    transcript_url, video_id = await replace_youtube_url(url)

    try:
        transcript_text = await scrape_transcript(transcript_url)

        if not transcript_text:
            print(f"No transcript available for URL: {url}")
            with open("failed/no_cc_list.txt", "a", encoding="utf-8") as file:
                file.write(url + "\n")
            return False

        if video_id:
            file_name = f"transcripts/{video_id}_transcript.txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(transcript_text)
            print(f"Transcript saved to {file_name}")
            return True

    except Exception as e:
        print("Error occurred while processing the URL:", str(e))
        return False


async def main():
    ascii_art = r"""
__   _______ _____ _____ 
\ \ / /_   _|_   _/  ___|
 \ V /  | |   | | \ `--. 
  \ /   | |   | |  `--. \
  | |   | |   | | /\__/ /
  \_/   \_/   \_/ \____/ 
                         
                         
"""
    print(ascii_art)
    print("{:^20}".format("Version 0.1"))
    print()
    parser = argparse.ArgumentParser(description="YouTube Transcript Scraper")
    parser.add_argument("-i", "--input", type=str, help="Input file with YouTube URLs")

    args = parser.parse_args()

    os.makedirs("transcripts", exist_ok=True)
    os.makedirs("failed", exist_ok=True)

    if args.input:
        try:
            with open(args.input, "r") as file:
                urls = [url.strip() for url in file.readlines() if url.strip()]
        except Exception as e:
            print("Error occurred while reading the input file:", str(e))
            return

        for url in urls:
            print(f"Processing URL: {url}")
            await process_youtube_url(url)

    else:
        while True:
            youtube_url = input("Enter the YouTube URL (or press Ctrl+C to exit): ")

            if not youtube_url:
                continue

            print(f"Processing URL: {youtube_url}")
            await process_youtube_url(youtube_url)


asyncio.get_event_loop().run_until_complete(main())