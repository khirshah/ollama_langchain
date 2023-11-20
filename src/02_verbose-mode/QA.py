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

    for document in response['source_documents']:
      content = document.page_content
      metadata = document.metadata
      print('---------------------------------------------------------------')
      print(content)
      print('---------------------------------------------------------------')
      for key in metadata:
        print(key,': ', metadata[key])

    # Wrapping the text for better output in Jupyter Notebook
    wrapped_text = textwrap.fill(response['result'], width=100)
    print('\nResult:\n')
    print(wrapped_text)