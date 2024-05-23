from llama_index.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from core.translator import translate_text


def generate_text(nature: str, context: str, query: str, temperature=0.75):

    nature = translate_text(nature, "ru", "en")
    context = translate_text(context, "ru", "en")
    query = translate_text(query, "ru", "en")

    template = """{nature}

    Context:  {context}

    Question: {query}

    Answer:"""

    promt_template = PromptTemplate(input_variables=["query"], template=template)
    input_text = promt_template.format(nature=nature, context=context, query=query)

    llm = Ollama(model="llama3", temperature=temperature, request_timeout=600000.0)
    generated_text = llm.complete(input_text)
    return translate_text(generated_text.text, "en", "ru"), temperature
