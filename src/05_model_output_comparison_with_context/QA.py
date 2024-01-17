# Importing the necessary packages
from langchain.chains import RetrievalQA
import textwrap

# Creating the chain for Question Answering
def load_qa_chain(retriever, llm, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever, # here we are using the vectorstore as a retriever
        chain_type="stuff",
        return_source_documents=True, # including source documents in output
        chain_type_kwargs={'prompt': prompt}, # customizing the prompt
    )

# Prettifying the response
def get_response(query, chain):
    # Getting response from chain
    response = chain({'query': query})

    # response = chain({
    #     'first_text': query['first_text'], 
    #     'second_text': query['second_text'],
    #     'query': query['query']
    #     })

    # Wrapping the text for better output in Jupyter Notebook
    wrapped_text = textwrap.fill(response['result'], width=100)
    return(wrapped_text)
