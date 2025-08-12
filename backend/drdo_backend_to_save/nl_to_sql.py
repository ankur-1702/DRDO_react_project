from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Step 1: Connect to your local LLM (llama3)
llm = Ollama(model="llama3")

# Step 2: Create a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Convert the following natural language question into an SQL query:\n\nQuestion: {question}\n\nSQL:"
)

# Step 3: Create a LangChain chain with the prompt and model
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: Ask a sample question
user_question = "How much fuel did jet ID 2 consume last month?"
response = chain.run(user_question)

# Step 5: Print the SQL output
print("Generated SQL Query:\n", response)
