from llama_index.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from translator import translate_text


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


def llama(temperature: float):

    nature = ("Ваша цель изменить текст, новый текст должен быть максимально похож на исходный. Оставь задание без "
              "решения! Не добавляй заголовки!")

    context = (
        "Каждый из двух рабочих одинаковой квалификации может выполнить заказ за 12 часов. Через 4 часа после того, "
        "как один из них приступил к выполнению заказа, к нему присоединился второй рабочий, и работу над заказом они "
        "довели до конца уже вместе. За сколько часов был выполнен весь заказ?"
    )

    query = "Измени сюжет задачи, убрав рабочих и заменив их на Карлсона и Малыша, которые пекут торт. Измени цифры!"

    return generate_text(
        nature=nature, context=context, query=query, temperature=temperature
    )
