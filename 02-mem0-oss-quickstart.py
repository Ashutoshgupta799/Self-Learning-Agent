from mem0 import Memory
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent / ".env")

def main():
    memory = Memory()  # Requires OpenAI API key

    messages = [
        {
            "role": "user",
            "content": "I'm planning to watch a movie tonight. Any recommendations?",
        },
        {
            "role": "assistant",
            "content": "How about a thriller movie? They can be quite engaging.",
        },
        {
            "role": "user",
            "content": "I'm not a big fan of thriller movies but I love sci-fi movies.",
        },
        {
            "role": "assistant",
            "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future.",
        },
    ]

    memory.add(
        messages,
        user_id="default_user",
        metadata={"category": "movie_recommendations"},
    )
    all_memories = memory.get_all(user_id="default_user")
    related_memories = memory.search(
        query="What do you know about me?", user_id="default_user"
    )

    print("All memories:", all_memories)
    print("Related memories:", related_memories)


if __name__ == "__main__":
    main()