# LLM data ingestion pipeline with Langchain & Robocorp

This example shows you how to implement a LLM data ingestion pipeline with Robocorp, using [Langchain](https://python.langchain.com/docs/get_started/introduction.html). The need for simple pipelines that run frequently have exploded, and one driver is [retrieval-augmented generation](https://www.promptingguide.ai/techniques/rag) (RAG) use cases, where the source data needs to be loaded in to a vector database as embeddings frequently.

The benefits of using Robocorp for RAG data ingestion:

- Zero infra: run and schdule workflows in the [Robocorp Control Room](https://cloud.robocorp.com) (4h/month runtime for free!)
- Also supports running the workflows [on-prem](https://robocorp.com/docs/control-room/unattended/worker-setups)
- Connect your git repo and your new updates deploy automatically to workers in the cloud
- Use Asset Storage to manage configurations - update without code changes.
- Easy management of Python environments between and dev and prod usage with simple [conda.yaml](conda.yaml)s
- Great and powerful tools for scraping data, e.g. with Playwright
- Tens of prebuilt connectors for accessing systems like Salesforce, SAP, HubSport etc
- It's all Python 🐍

## TODO FROM THIS POINT ONWARDS

## Setup

The following configurations are needed to run the ingestion pipeline.

- VS Code with [Robocorp Code](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code) connected to your Robocorp workspace (get a free account [here](https://cloud.robocorp.com))
- [OpenAI](https://platform.openai.com/) API key in Robocorp Vault called `OpenAI` with key named `key`.
- Configuration data stored in Control Room Asset Storage. Below is a sample that works.

```json
{
  "portal": {
    "url": "https://robocorp.com/portal/robots.json"
  },
  "robo": {
    "url": "https://github.com/robocorp/robo.git",
    "white_list": ["README.md"]
  },
  "rpa": {
    "url": "https://rpaframework.org/latest.json",
    "black_list": ["RPA.Dialogs", "RPA.Browser.common", "RPA.version"]
  }
}
```

## The bot

The bot contains three loaders as an example, each a class in [loaders directory](/loaders/):

- PortalLoader: Reads a JSON configuration file, and then traverses multiple github repo's to get descriptions and code examples.
- RoboLoader: Reads markdown from a gihub repo that contains python library documentation
- RPALoader: Reads a configuration JSON file, and documentation website contents using BeautifulSoup4.

For each of the loaders, the URL and black/whitelist data is read from the Control Room Asset Storage, meaning that you can add more white/blacklisted entries without code changes or deployments.

## Control Room

Short Control Room screen recording (coming soon)