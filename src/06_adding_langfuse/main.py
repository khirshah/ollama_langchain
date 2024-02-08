from langchain_community.llms import Ollama
from langchain_core.callbacks.manager import CallbackManager
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from data_handling import *
from embedding import *
from prompt import *
import os
from QA  import * 
from langfuse import CallbackHandler
import json

LANGFUSE_PUBLIC_KEY = "pk-lf-20c1c45f-94d4-43a4-95eb-447b69556191"
LANGFUSE_SECRET_KEY = "sk-lf-6f46d5dd-50bb-4a50-ba46-8b202c3ad5f8"
# Set LangFuse destination to localhost, i.e. our local docker containers running on localhost:3000
os.environ["LANGFUSE_HOST"] = "http://localhost:3000"

# Set PUBLIC_KEY and SECRET_KEY to empty OS vars#
os.environ["LANGFUSE_PUBLIC_KEY"] = LANGFUSE_PUBLIC_KEY
os.environ["LANGFUSE_SECRET_KEY"] = LANGFUSE_SECRET_KEY


### Langfuse debug on
langfuse = Langfuse(debug=True)

with open('questions2.json') as questions:
  file_contents = questions.read()
questions.close() 

parsed_questions = json.loads(file_contents)
results = []

  # Loading model from Ollama
llm = Ollama(
  model='codellama:7b',
  callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
  temperature=0
  )


# Loading the Embedding Model
embed = load_embedding_model(model_path="all-MiniLM-L6-v2")

# loading and splitting the documents
docs = load_pdf_data(file_path="./../../data/hp1.pdf")
documents = split_docs(documents=docs)

# creating vectorstore
vectorstore = create_embeddings(documents, embed)

# converting vectorstore to a retriever
retriever = vectorstore.as_retriever()

# Creating the prompt from the template which we created before
prompt = PromptTemplate.from_template(template)


# Create the handler with API Keys
handler = CallbackHandler()

# Creating the chain
# chain = load_qa_chain(retriever, llm, prompt)
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
question = "how are you?"
chain.invoke(question, config={"callbacks":[handler]})

# for item in parsed_questions:
#     print(item['question'])
#     answer = get_response(item['question'], chain)
#     print(answer)
#     results[model].append({
#       'id': item['id'],
#       'question': item['question'],
#       'answer': answer
#     })

# with open('output.json', 'w+', encoding='utf-8') as f:
#   json.dump(results, f, ensure_ascii=False, indent=2)
# f.close()
