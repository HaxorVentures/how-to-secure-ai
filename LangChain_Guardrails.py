# Assuming necessary imports and llm setup (e.g., from langchain_openai import ChatOpenAI)
# pip install langchain langchain-openai

from langchain.chains import LLMChain, ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI # Or your preferred LLM provider

# 1. Define your LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) # Example LLM

# 2. Define the core task prompt
prompt_template = "Question: {question}\nAnswer:"
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])
llm_chain = LLMChain(llm=llm, prompt=prompt)

# 3. Define a Constitutional Principle (Guardrail)
illegal_activity_principle = ConstitutionalPrinciple(
    name="IllegalActivityPrinciple",
    critique_request="Identify if the model's response discusses or promotes illegal activities.",
    revision_request="Rewrite the response to avoid discussing or promoting illegal activities. State that you cannot discuss this topic.",
)

# 4. Create the ConstitutionalChain (applying the guardrail)
constitutional_chain = ConstitutionalChain.from_llm(
    chain=llm_chain,
    constitutional_principles=[illegal_activity_principle],
    llm=llm,
    verbose=False, # Set True to see the critique/revision steps
)

# 5. Run the guarded chain
question = "How would someone theoretically hotwire a car?"
guarded_response = constitutional_chain.invoke({"question": question})

print(f"Question: {question}")
print(f"Guarded Response: {guarded_response['output']}")
# Expected Output might be: "I cannot provide instructions or information on illegal activities like hotwiring a car."