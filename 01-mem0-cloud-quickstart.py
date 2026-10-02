from mem0 import MemoryClient
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent / ".env")

def main():
    api_key = os.getenv("MEM0_API_KEY")
    if not api_key:
        raise RuntimeError("Set MEM0_API_KEY in the project root .env file")

    client = MemoryClient(api_key=api_key)

    messages = [
        {"role": "user", "content": "Hi, I'm Dave. I like to build AI automations!"},
        {
            "role": "assistant",
            "content": "Hello Dave! I'll keep your interest in AI automations in mind.",
        },
    ]

    client.add(messages, user_id="default_user")
    response = client.search("What shall we build today?", user_id="default_user")
    print(response)

if __name__ == "__main__":
    main()