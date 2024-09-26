import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

# Function to send markdown file to a Slack channel
def send_markdown_to_slack(channel, markdown_file):
    try:
        response = client.files_upload(
            channels=channel,
            file=markdown_file,
            title="Scraped Markdown Content",
            initial_comment="Here is the scraped content in markdown format."
        )
        return response
    except SlackApiError as e:
        print(f"Error uploading file to Slack: {e}")
