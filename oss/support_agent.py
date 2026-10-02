from openai import OpenAI
from mem0 import Memory
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class CustomerSupportAIAgent:
    def __init__(self):
        """
        Initialize the CustomerSupportAIAgent with memory configuration and OpenAI client.
        """
        # ! Make sure qdrant is running (see docker-compose.yml)
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                },
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        self.app_id = "customer-support"

    def handle_query(self, query, user_id="default_user"):
        """
        Handle a customer query and store the relevant information in memory.

        :param query: The customer query to handle.
        :param user_id: Optional user ID to associate with the memory.
        """
        relevant_memories = self.memory.search(
            query=query, user_id=user_id, top_k=3
        )
        memories_text = "\n".join(
            f"- {entry['memory']}" for entry in relevant_memories.get("results", [])
        )
        response = self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a customer support AI agent. Use relevant customer "
                        f"history when helpful.\nCustomer memories:\n{memories_text}"
                    ),
                },
                {"role": "user", "content": query},
            ],
        )
        assistant_response = response.choices[0].message.content or ""
        self.memory.add(
            [
                {"role": "user", "content": query},
                {"role": "assistant", "content": assistant_response},
            ],
            user_id=user_id,
            metadata={"app_id": self.app_id},
        )
        return assistant_response

    def get_memories(self, user_id="default_user"):
        """
        Retrieve all memories associated with the given customer ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)


def main():
    support_agent = CustomerSupportAIAgent()
    customer_id = "default_user"
    response = support_agent.handle_query(
        "I need help with my recent order. It hasn't arrived yet.",
        user_id=customer_id,
    )
    print(response)


if __name__ == "__main__":
    main()