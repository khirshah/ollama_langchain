# Importing the necessary packages
from langchain.chains import LLMChain
import textwrap

# Creating the chain for Question Answering
def load_qa_chain(llm, prompt):
    return LLMChain(
        llm = llm,
        prompt = prompt
    )

# Prettifying the response
def get_response(query, chain):
    # Getting response from chain
    response = chain({'first_text': query['first_text'], 'second_text': query['second_text']})

    return(response)
