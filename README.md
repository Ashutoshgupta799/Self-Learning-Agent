# Self-Learning-Agent

Small examples of Mem0 Cloud and Mem0 OSS memory-backed assistants.

## Setup

Use Python 3.10 or newer, install the dependencies, and create a `.env` file in
the project root:

```bash
python -m pip install -r requirements.txt
cp -n .env.example .env
```

Set `OPENAI_API_KEY` for the OSS examples and `MEM0_API_KEY` for the Cloud
examples in `.env`. Keep that file private; it is excluded from Git.

## Run

Run commands from the project root. The OSS demos that use local Qdrant need
Docker:

```bash
docker compose -f docker/docker-compose.yml up -d
python oss/memory_demo.py
```

Other examples:

```bash
python 01-mem0-cloud-quickstart.py
python 02-mem0-oss-quickstart.py
python oss/support_agent.py
python cloud/email_example.py
```

The quickstart OSS script uses Mem0's default local configuration; `memory_demo`
and `support_agent` use the Qdrant service above. The cloud examples require a
Mem0 Cloud API key. Running an example makes API calls and may incur charges.
