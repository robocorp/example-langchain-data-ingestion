# LLM data ingestion pipeline with Langchain & Robocorp

**Are you curious about what's happening behind the scenes with [ReMark💬](https://chat.robocorp.com), a code-gen assistant specifically trained to help developers build automation bots on Roboccorp? We are exposing (almost) everything here in how we create vector embeddings from various sources! ReMark💬 is trained on Robocorp documentation and examples, which are either on JSON files, GitHub repos or websites.**

This example shows you how to implement an LLM data ingestion pipeline with Robocorp using [Langchain](https://python.langchain.com/docs/get_started/introduction.html). The need for simple pipelines that run frequently has exploded, and one driver is [retrieval-augmented generation](https://www.promptingguide.ai/techniques/rag) (RAG) use cases, where the source data needs to be loaded into a vector database as embeddings frequently.

The benefits of using Robocorp for RAG data ingestion:

- Zero infra: run and schedule workflows in the [Robocorp Control Room](https://cloud.robocorp.com) (4h/month runtime for free!)
- Also supports running the workflows [on-prem](https://robocorp.com/docs/control-room/unattended/worker-setups)
- Connect your git repo, and your new updates deploy automatically to workers in the cloud
- Use Asset Storage to manage configurations - update without code changes.
- Easy management of Python environments between dev and prod usage with simple [conda.yaml](conda.yaml)s
- Great and powerful tools for scraping data, e.g. with Playwright
- Tens of prebuilt connectors for accessing systems like Salesforce, SAP, HubSpot, etc
- It's all Python 🐍

## Setup

The following configurations are needed to run the ingestion pipeline.

- Get [VS Code](https://code.visualstudio.com/) with [Robocorp Code](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code) connected to your Robocorp workspace (get a free account [here](https://cloud.robocorp.com))
- [OpenAI](https://platform.openai.com/) API key in Robocorp Vault called `OpenAI` with a key named `key`.
- Configuration data stored in Control Room Asset Storage with name `rag_loader_config`. Below is a sample that works.

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

- PortalLoader: Reads a JSON configuration file and traverses multiple GitHub repos to get descriptions and code examples.
- RoboLoader: Reads markdown from a GitHub repo that contains Python library documentation
- RPALoader: Reads a configuration JSON file and documentation website contents using BeautifulSoup4.

For each loader, the URL and black/whitelist data are read from the Control Room Asset Storage, meaning that you can add more white/blacklisted entries without code changes or deployments.

## Control Room

Follow the video to see how to set things up from a GitHub repo in Robocorp. This is what you'll see:

- Connect to your repo (updates will be automatically deployed)
- Create an Asset for config data (URLs, whitelist, blacklist)
- Create a Process that combines the repo with a worker, in this case, the Robocorp cloud container
- Configure a schedule
- Set alerts, for example, only for failed runs
- RUN IT!

https://github.com/robocorp/example-langchain-data-ingestion/assets/40179958/c1b81119-d4ff-4445-aba4-bd752247f733

