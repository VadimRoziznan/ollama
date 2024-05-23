from core.report import create_report
from core.ollama import generate_text

nature = ("Ваша цель изменить текст, новый текст должен быть максимально похож на исходный. Оставь задание без "
          "решения! Не добавляй заголовки!")

context = (
    "Каждый из двух рабочих одинаковой квалификации может выполнить заказ за 12 часов. Через 4 часа после того, "
    "как один из них приступил к выполнению заказа, к нему присоединился второй рабочий, и работу над заказом они "
    "довели до конца уже вместе. За сколько часов был выполнен весь заказ?"
)

query = "Измени сюжет задачи, убрав рабочих и заменив их на Карлсона и Малыша, которые пекут торт. Измени цифры!"

temperature = 0.0

answer, temperature = generate_text(nature=nature, context=context, query=query, temperature=temperature)
create_report(answer, temperature)
