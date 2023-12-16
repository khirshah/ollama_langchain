from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from prompt_template import *
from QA  import * 
import json

with open('questions.json') as questions:
  questions_file_contents = questions.read()
questions.close()

parsed_questions = json.loads(questions_file_contents)

with open('model_answers.json') as answers:
  answers_file_contents = answers.read()
answers.close()

parsed_answers = json.loads(answers_file_contents)


# Loading model from Ollama
llm = Ollama(model='orca-mini', temperature=0)

# Creating the prompt from the template which we created before
prompt = PromptTemplate(
   input_variables = ["first_text", "second_text"],
   template = template
  )

# Creating the chain
chain = load_qa_chain(llm, prompt)


# results = []

for item in parsed_answers['orca-mini']:
    first_text = item['answer']
    second_text = [x['answer'] for x in parsed_questions if x['id'] == item['id']]
    # print(first_text)
    # print(second_text)
    result = get_response({
       'first_text': first_text,
       'second_text': second_text
       }, chain)
    print(result)
    # results.append({
    #   'id': item['id'],
    #   'result': result
    # })

# with open('output.json', 'w+', encoding='utf-8') as f:
#   json.dump(results, f, ensure_ascii=False, indent=2)
# f.close()
