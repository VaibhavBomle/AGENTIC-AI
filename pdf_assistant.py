import typer
from typing import Optional,List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import Pgvector2

import os
from dotenv import load_dotenv
load_dotenv()

os.getenv['GROQ_API_KEY']
## Need to install docker image from  https://docs.phidata.com/vectordb/pgvector
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowlwdge_base = PDFUrlKnowledgeBase(
    urls= ["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=Pgvector2(table_name = "recipes",db_url=db_url)
)

knowlwdge_base.load()

storage = PgAssistantStorage(table_name="pdf_assistant",db_url=db_url)

def pdf_assisntat(new: bool = False,user = "user"):
    run_id: Optional[str] = None

    if not new:
        exsiting_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(exsiting_run_ids) > 0:
            run_id = exsiting_run_ids[0]
        
        assistant = Assistant(
            run_id=run_id,
            user_id=user,
            knowledge_base=knowlwdge_base,
            storage=storage,
            show_tool_calls=True, # Show tools calls in the response
            search_knowledge=True, # Enable the assistant to search the knowledge base
            read_chat_history=True, # Enable the assistant to read the chat history
        )

        if run_id is None:
            run_id = assistant.run_id
            print(f"Started Run : {run_id}\n")
        else:
            print(f"Counting Run : {run_id}\n")

        assistant.cli_app(markdown=True)

if __name__ == "__main__":
    typer.run(pdf_assisntat)