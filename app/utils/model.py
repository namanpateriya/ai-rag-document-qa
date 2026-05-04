import os
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ModelClient:

    def __init__(self):
        self.provider = os.getenv("PROVIDER", "openai").lower()
        self.model = os.getenv("MODEL")

    def generate(self, prompt):
        if self.provider == "openai":
            return self._openai(prompt)
        elif self.provider == "anthropic":
            return self._anthropic(prompt)
        elif self.provider == "gemini":
            return self._gemini(prompt)
        else:
            return f"error: unsupported provider {self.provider}"

    def _openai(self, prompt):
        try:
            from openai import OpenAI
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "error: missing OPENAI_API_KEY"

            client = OpenAI(api_key=api_key)

            model = self.model or "gpt-4o-mini"

            res = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return res.choices[0].message.content

        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            return "error"

    def _anthropic(self, prompt):
        try:
            import anthropic
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                return "error: missing ANTHROPIC_API_KEY"

            client = anthropic.Anthropic(api_key=api_key)

            model = self.model or "claude-3-haiku-20240307"

            res = client.messages.create(
                model=model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            if res.content:
                return res.content[0].text

            return "error"

        except Exception as e:
            logger.error(f"Anthropic error: {e}")
            return "error"

    def _gemini(self, prompt):
        try:
            import google.generativeai as genai
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return "error: missing GEMINI_API_KEY"

            genai.configure(api_key=api_key)

            model_name = self.model or "gemini-1.5-flash"
            model = genai.GenerativeModel(model_name)

            res = model.generate_content(prompt)

            if hasattr(res, "text") and res.text:
                return res.text

            return str(res)

        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return "error"
