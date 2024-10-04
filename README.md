# bot-openai
An OpenAI bot for Teams integration

### Run locally 

Docker run
```
docker run -p 3978:3978 -e MICROSOFT_APP_ID=<your-bot_id> -e MICROSOFT_APP_PASSWORD=<your-bot-secret>  f-bot
```
Note that the ID and password are not quoted at all in the command line, otherwise the quotes will be sent too

NGrok for the port forwarding
```
ngrok http 3978
```

The ngrok URL then needs to be put in to the bot configuration messaging endpoint
e.g.
```
https://jjbotcont-ddddd.westeurope-01.azurewebsites.net/api/messages
```
