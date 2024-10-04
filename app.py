# Step 1: Set up the environment
# Run these commands in your terminal
# pip install botbuilder-core botbuilder-schema botbuilder-integration-aiohttp flask

# Step 2: Create the bot
import os
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
         await turn_context.send_activity(f"You said: {turn_context.activity.text}")

    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                 await turn_context.send_activity("Hello and welcome!")

# Step 3: Configure the bot
from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity

app = Flask(__name__)

# Bot configuration
MICROSOFT_APP_ID = os.getenv("MICROSOFT_APP_ID", "")
MICROSOFT_APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "")
SETTINGS = BotFrameworkAdapterSettings(MICROSOFT_APP_ID, MICROSOFT_APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = MyBot()

@app.route("/api/messages", methods=["POST"])
async def messages():
    print("api called")
    if "application/json" in request.headers["content-type"]:
        body = request.json
    else:
        return Response(status=415)
    
    print(body)
    activity = Activity().deserialize(body)
    auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return Response(status=response.status)
    return Response(status=201)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3978))
    app.run(host="0.0.0.0", port=port)
