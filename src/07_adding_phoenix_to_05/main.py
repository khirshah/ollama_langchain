import phoenix as px
from phoenix.trace.langchain import OpenInferenceTracer, LangChainInstrumentor
import pandas as pd
import numpy as np
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from data_handling import *
from embedding import *
from prompt_template import *
from QA  import * 
import json

# Launch phoenix
session = px.launch_app()

# If no exporter is specified, the tracer will export to the locally running Phoenix server
tracer = OpenInferenceTracer()
LangChainInstrumentor(tracer).instrument()

with open('questions.json') as questions:
  questions_file_contents = questions.read()
questions.close()

parsed_questions = json.loads(questions_file_contents)

with open('model_answers.json') as answers:
  answers_file_contents = answers.read()
answers.close()

parsed_answers = json.loads(answers_file_contents)

chain_type = "stuff"
chat_model_name='orca-mini'

# Loading model from Ollama
llm = Ollama(model='orca-mini', temperature=0)

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
prompt=PromptTemplate.from_template(template)
# prompt = PromptTemplate(
#    template=template,
#    input_variables = ["first_text", "second_text", "query"]
#   )

# Creating the chain
chain = load_qa_chain(retriever, llm, prompt)


# results = []

for item in parsed_answers[chat_model_name]:
    first_text = item['answer']
    second_text = [x['answer'] for x in parsed_questions if x['id'] == item['id']]
    print(first_text)
    print(second_text[0])
    response = get_response('''first_text: {first_text}second_text: {second_text[0]}''', chain, tracer)
    # response = get_response({
    #   'first_text': first_text,
    #   'second_text': second_text,
    #   'query': 'Do these 2 texts have the same meaning?'
    #   }, chain)
    print(response)
    # results.append({
    #   'id': item['id'],
    #   'result': result
    # })

# with open('output.json', 'w+', encoding='utf-8') as f:
#   json.dump(results, f, ensure_ascii=False, indent=2)
# f.close()
