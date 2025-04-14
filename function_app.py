import azure.functions as func
from openai import AzureOpenAI
import logging
import os

app =func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="SecretGarden")
def SecretGarden(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    client = AzureOpenAI(
       azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2025-02-01-preview"
)

    bot_role = req.get("bot_role", "You are a helpful assistant.")
    words_limit = req.get("words_limit", 100)
    prompt = req.get("prompt", "What is the best food?")
    temperature = req.get("temperature", 0.1)

    response = client.responses.create(
        model="gpt-4o",
        instructions=bot_role,
        input=prompt,
        max_output_tokens=words_limit,
        temperature=temperature)

    return func.HttpResponse(
            "This HTTP triggered function executed successfully." + response.output_text,
            status_code=200
    )