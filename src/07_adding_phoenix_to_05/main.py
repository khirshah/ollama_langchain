import phoenix as px
from phoenix.trace.langchain import OpenInferenceTracer, LangChainInstrumentor
import pandas as pd
import numpy as np
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from data_handling import *
from embedding import *
from prompt_template import *
from QA  import * 

## SETUP
# Parameter setup
chain_type = "stuff"
chat_model_name='orca-mini'

# Read data from files 
questions = load_json_data('questions.json')
model_answers = load_json_data('model_answers.json')

## FINE TUNING SETUP
# Loading the Embedding Model
embed = load_embedding_model(model_path="all-MiniLM-L6-v2")

# Loading and splitting the PDF documents
docs = load_pdf_data(file_path="./../../data/hp1.pdf")
documents = split_docs(documents=docs)

# Creating vectorstore
vectorstore = create_embeddings(documents, embed)

# Converting vectorstore to a retriever
retriever = vectorstore.as_retriever()

# Creating the prompt from the template
prompt=PromptTemplate.from_template(template)


## LAUNCH
# Launch phoenix
session = px.launch_app()

# If no exporter is specified, the tracer will export to the locally running Phoenix server
tracer = OpenInferenceTracer()
LangChainInstrumentor(tracer).instrument()


# Loading model from Ollama
llm = Ollama(model=chat_model_name, temperature=0)

# Creating the chain
chain = load_qa_chain(retriever, llm, prompt)


# Calling the chain
for item in model_answers[chat_model_name]:
    model_answer = item['answer']
    correct_answer = [x['answer'] for x in questions if x['id'] == item['id']]
    print('\n')
    print('Question:\n',item['question'])
    print('Answer (model):\n', model_answer)
    print('Answer (correct):\n', correct_answer[0])
    response = get_response(
       '''first_text: {model_answer}second_text: {correct_answer[0]}''', 
       chain,
       tracer
      )

    print('Evaulation:\n', response)
