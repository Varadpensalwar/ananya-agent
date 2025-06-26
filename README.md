# Ananya AI Companion

Ananya is your personal AI buddy built with LangGraph, Chainlit, and various AI services. This open-source project creates an intelligent agent that can interact through text and voice, with potential WhatsApp integration. Feel free to use, modify, and contribute to this project!

## Overview

Ananya is designed to be a versatile AI companion that can:
- Engage in natural conversations
- Process and respond to voice inputs using ElevenLabs
- Store and retrieve information using Qdrant vector database
- Run on multiple interfaces including Chainlit and FastAPI

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- Docker and Docker Compose (for running the full application stack)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Varadpensalwar/ananya-agent.git
cd ananya-agent
```

2. Install uv (if not already installed):
Follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

3. Create a virtual environment and install dependencies:
```bash
uv venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
. .\.venv\Scripts\Activate.ps1
uv pip install -e .
```

4. Set up environment variables:
```bash
# Create a .env file with your API keys
touch .env
```

5. Configure your `.env` file with the necessary API keys:
   - GROQ_API_KEY - [Groq Console](https://console.groq.com/docs/quickstart)
   - ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID - [ElevenLabs](https://elevenlabs.io/)
   - TOGETHER_API_KEY - [Together AI](https://www.together.ai/)
   - QDRANT_URL and QDRANT_API_KEY - [Qdrant Cloud](https://login.cloud.qdrant.io/)
   - WhatsApp credentials (optional, for WhatsApp integration)

For detailed instructions on obtaining these API keys, see the [Getting Started Guide](docs/GETTING_STARTED.md).

## Running the Application

The easiest way to run the application is using the provided [Makefile](Makefile):

```bash
make ananya-run
```

This command starts a Docker Compose application with three services:
- Qdrant Database: http://localhost:6333/dashboard
- Chainlit interface: http://localhost:8000
- FastAPI application: http://localhost:8080/docs

To stop and clean up the Docker containers and local folders:

```bash
make ananya-delete
```

## Project Structure

- `src/ai_companion/` - Core application code
  - `graph/` - LangGraph implementation
  - `interfaces/` - User interfaces (Chainlit, FastAPI)
- `docs/` - Documentation
- `img/` - Images for documentation
- `notebooks/` - Jupyter notebooks for development and testing

## Deployment

For instructions on deploying to Google Cloud Platform, see the [GCP Setup Guide](docs/gcp_setup.md).

## Contributing

Contributions are welcome! As an open-source project, Ananya thrives on community involvement. Feel free to:

- Fork the repository
- Create a feature branch
- Submit pull requests
- Report issues
- Suggest enhancements

No contribution is too small, and all are appreciated!

## License

This project is open source and free to use! It's licensed under the [MIT License](LICENSE), which means you can use, modify, and distribute it for personal or commercial purposes with minimal restrictions.
