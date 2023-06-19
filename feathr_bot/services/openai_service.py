import openai
import os


class OpenAIService(object):
    API_KEY = os.environ.get("OPENAI_API_KEY")

    def __init__(
        self,
        mode: str = "Completion",
        engine: str = "gpt-3.5-turbo",
    ) -> None:
        self.mode = mode
        self.engine = engine
        self.openai = openai
        self.openai.api_key = self.API_KEY

    def analyze(self, prompt: str) -> dict:
        response = self.openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            temperature=0.6,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        return response

    def chat(self, messages: list) -> dict:
        response = self.openai.ChatCompletion.create(
            model=self.engine, messages=messages
        )

        return response
