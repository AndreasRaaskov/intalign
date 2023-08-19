import requests
import openai
import dotenv
from typing import List

#MODEL_ID = "gpt-3.5-turbo-0301"
MODEL_ID = "gpt-4-0613"

keys = dotenv.dotenv_values("keys.env")
openai.api_key = keys["OPENAI_API_KEY"]
translate_api_key = keys["TRANSLATE_API_KEY"]


def translate(
    text: List[str] | str, source_language: str, target_language: str
) -> List[str] | str:
    translations = requests.post(
        "https://translation.googleapis.com/language/translate/v2",
        params={
            "q": text,
            "target": target_language,
            "format": "text",
            "source": source_language,
            "key": translate_api_key,
        },
    ).json()["data"]["translations"]
    return [translation["translatedText"] for translation in translations]


def translate_single(text: str, source_language: str, target_language: str) -> str:
    return translate(text, source_language, target_language)[0]


def chat(message: str) -> str:
    return (
        openai.ChatCompletion.create(
            model=MODEL_ID, messages=[{"role": "user", "content": message}]
        )
        .choices[0]
        .message.content
    )
