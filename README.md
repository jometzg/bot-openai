# Teams bot that uses Azure OpenAI to answer questions

An OpenAI bot for Teams integration. Presents itself as a Teams channel.

### Run locally 

Docker run
```
docker run -p 3978:3978 -e MICROSOFT_APP_ID=<your-bot_id> -e MICROSOFT_APP_PASSWORD=<your-bot-secret> -e AZURE_OPENAI_ENDPOINT=<your-full-url> -e AZURE_OPENAI_KEY=<your-key> f-bot
```
Note that the ID and password are not quoted at all in the command line, otherwise the quotes will be sent too

The OpenAI endpoint is the full chat completions URL e.g. https://test.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-06-01

NGrok for the port forwarding
```
ngrok http 3978
```

The ngrok URL then needs to be put in to the bot configuration messaging endpoint
e.g.
```
https://jjbotcont-ddddd.westeurope-01.azurewebsites.net/api/messages
```
## ToDo
1. system message
2. chat history
3. own data
4. intent gathering and potentially more than one agent e.g. one for HR docs and one for another department
