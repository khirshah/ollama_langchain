from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from data_handling import *
from embedding import *
from prompt import *
from QA  import * 
import json

with open('questions2.json') as questions:
  file_contents = questions.read()
questions.close()

parsed_questions = json.loads(file_contents)
models = ['mistral','orca-mini']
results = {}

for model in models:
    print(model)
    results[model] = []
  
    # Loading model from Ollama
    llm = Ollama(model=model, temperature=0)

    # Loading the Embedding Model
    embed = load_embedding_model(model_path="all-MiniLM-L6-v2")

    # loading and splitting the documents
    docs = load_pdf_data(file_path="./../data/hp1.pdf")
    documents = split_docs(documents=docs)

    # creating vectorstore
    vectorstore = create_embeddings(documents, embed)

    # converting vectorstore to a retriever
    retriever = vectorstore.as_retriever()

    # Creating the prompt from the template which we created before
    prompt = PromptTemplate.from_template(template)

    # Creating the chain
    chain = load_qa_chain(retriever, llm, prompt)

    for item in parsed_questions:
        print(item['question'])
        answer = get_response(item['question'], chain)
        print(answer)
        results[model].append({
          'id': item['id'],
          'question': item['question'],
          'answer': answer
        })

with open('output.json', 'w+', encoding='utf-8') as f:
  json.dump(results, f, ensure_ascii=False, indent=2)
f.close()
