# LangGraph with LangSmith Integration

This repository demonstrates an integration between LangGraph and LangSmith for building and monitoring language model applications.

## Features

- Stateful graph implementation using LangGraph
- LangSmith integration for observability and monitoring
- Simple example graph showing input processing and output generation

## Prerequisites

- Python 3.11 or higher
- LangSmith API Key (required for observability)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd my-langgraph-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with your LangSmith API key:
```
LANGSMITH_API_KEY=your_api_key_here
```

## Running Locally

1. Start the LangGraph development server:
```bash
langgraph dev
```

2. The server will start and be accessible at `http://localhost:8080`

3. You can test the graph by sending a POST request to the endpoint:
```bash
curl -X POST http://localhost:8080/my_graph -H "Content-Type: application/json" -d '{"input": "Hello"}'
```

## Project Structure

- `graph.py`: Contains the main graph implementation
- `langgraph.json`: Configuration file for LangGraph
- `langgraph_config.py`: Configuration for LangSmith integration
- `requirements.txt`: Project dependencies

## Monitoring with LangSmith

The application is configured to send traces and events to LangSmith. You can monitor the application's behavior in the LangSmith dashboard using your API key.

## Development

The project uses Python-dotenv to load environment variables. Make sure to create a `.env` file with your API keys before running the application.

## License

MIT License
