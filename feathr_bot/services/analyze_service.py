from feathr_bot.services.openai_service import OpenAIService


class AnalyzeService(object):
    def __init__(self, prompt: str) -> None:
        self.prompt = prompt

    def analyze(self) -> str:
        """Process result from OpenAI"""
        full_prompt = f"Classify the sentiment in this email:\n\n{self.prompt}"

        service = OpenAIService(engine="text-davinci-003")
        results = service.analyze(full_prompt)
        return results["choices"][0]["text"].strip()
