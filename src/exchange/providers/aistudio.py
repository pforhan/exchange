import os
from typing import Type

import httpx

from exchange.providers.openai import OpenAiProvider

AISTUDIO_HOST = "https://api.aistudio.com/"
AISTUDIO_MODEL = "gemini"


class AiStudioProvider(OpenAiProvider):
    """Provides chat completions for models hosted by Google Gemini (AiStudio)"""

    __doc__ += f"""

Here's an example profile configuration to try:

    aistudio:
      provider: aistudio
      processor: {AISTUDIO_MODEL}
      accelerator: {AISTUDIO_MODEL}
      moderator: passive
      toolkits:
      - name: developer
        requires: {{}}
"""

    def __init__(self, client: httpx.Client) -> None:
        print("PLEASE NOTE: the aistudio provider is experimental, use with care")
        super().__init__(client)

    @classmethod
    def from_env(cls: Type["AiStudioProvider"]) -> "AiStudioProvider":
        aistudio_url = os.environ.get("AISTUDIO_HOST", AISTUDIO_HOST)
        timeout = httpx.Timeout(60 * 10)

        client = httpx.Client(base_url=aistudio_url + "v1/", timeout=timeout)
        return cls(client)
