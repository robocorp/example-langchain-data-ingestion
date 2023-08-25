from typing import List
from robocorp.tasks import task
from robocorp import vault

from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma

from loaders.RPA import RPALoader
from loaders.Robo import RoboLoader
from loaders.Portal import PortalLoader



@task
def prepare_docs():
    openai_secrets = vault.get_secret("OpenAI")
    docs: List[Document] = []

    # Load RPA Framework from a documentation JSON file
    rpaLoader = RPALoader(
        url="https://rpaframework.org/latest.json",
        blacklist=["RPA.Dialogs", "RPA.Browser.common", "RPA.version"],
    )
    rpaDocs = rpaLoader.load()
    docs.extend(rpaDocs)

    # Load Robo Framework docs from Git repo
    roboLoader = RoboLoader(
        repo_url="https://github.com/robocorp/robo.git",
        white_list=[
            "README.md",
        ],
    )
    roboDocs = roboLoader.load()
    docs.extend(roboDocs)

    # Load Portal robot examples based on configuration file and git repos.
    portalLoader = PortalLoader(url="https://robocorp.com/portal/robots.json")
    portalDocs = portalLoader.load()
    docs.extend(portalDocs)

    # NOTE: This just cratest the embeddings locally, doesn't actually do anyt
    # anything with them afterwards.
    # TODO: Use a hosted vectordb as a showcase.
    create_embeddings(docs, openai_secrets)


def create_embeddings(documents, openai_secrets):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_secrets["key"])

    db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="ROBOCORP_DOCS_TEST"
    )

    return db