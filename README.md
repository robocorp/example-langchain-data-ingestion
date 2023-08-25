# LLM data ingestion pipeline with Langchain & Robocorp

This example shows you how to implement a data ingestion pipeline with Robocorp, using [Langchain](https://python.langchain.com/docs/get_started/introduction.html). The need for simple pipelines that run frequently have exploded, and one driver is [retrieval-augmented generation](https://www.promptingguide.ai/techniques/rag) (RAG) use cases, where the source data often needs to be loaded in to a vector database as embeddings.

The benefits of using Robocorp bots:

- No infra needed: run and schdule workflows in the [Robocorp Control Room](https://cloud.robocorp.com) (4h/month runtime for free!)
- If you need the workflow to run on-prem, that works too!
- Easy management of Python environments between and dev and prod usage
- Great and powerful tools for scraping data, e.g. with Playwright
- Tens of prebuilt connectors for accessing systems like Salesforce, SAP, HubSport etc
- It's all Python 🐍

## TODO FROM THIS POINT ONWARDS

Contains three loaders:

- PortalLoader: Reads a JSON configuration file, and then traverses multiple github repo's to get descriptions and code examples.
- RoboLoader: Reads markdown from a gihub repo that contains python library documentation
- RPALoader: Reads a configuration JSON file, and documentation website contents using BeautifulSoup4.

Uses Chroma now in this example, just creates it but doesn't do anything. It's there because goes without any credentials. We use pgvector internally.

Short Control Room screen recording (coming soon)