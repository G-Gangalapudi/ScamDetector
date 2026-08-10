class AIProvider:
    def __init__(self, provider_name: str = "default"):
        self.provider_name = provider_name

    def generate(self, prompt: str):
        return {"provider": self.provider_name, "prompt": prompt}
