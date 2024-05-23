from report import create_report
from ollama import llama


answer, temperature = llama(temperature=0.0)
create_report(answer, temperature)
