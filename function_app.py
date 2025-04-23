import azure.functions as func
from openai import AzureOpenAI
import logging
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="answernow")
def answernow(req: func.HttpRequest) -> func.HttpResponse:
    client = AzureOpenAI(
        api_version="2025-01-01-preview",
        azure_endpoint="https://polbot.openai.azure.com/",
        api_key="Auyd5BJFBhGfjvSvKeln4q27SseKhcoYuEFxmDJLHKZm5f3ge48DJQQJ99BDACE1PydXJ3w3AAABACOGgSMT",
    )

    body = req.get_json()

    bot_role = body.get("bot_role", "You are a helpful assistant.")
    words_limit = body.get("words_limit", 100)
    prompt = body.get("prompt", "What is the best food?")
    temperature = body.get("temperature", 0.1)

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=bot_role,
        input=prompt,
        max_output_tokens=words_limit,
        temperature=temperature,
    )

    return func.HttpResponse(
        response.output[0].content[0].text,
        status_code=200,
    )
