import sys

def categorize_and_draft(message: str) -> tuple[str, str]:
    msg_lower = message.lower()
    
    rules = [
        {
            "keywords": ["справк", "где", "как"],
            "category": "справка",
            "draft_template": "Здравствуйте! Информацию по вашему вопросу ({}) можно найти на нашем портале или уточнить в инфоцентре."
        },
        {
            "keywords": ["очередь", "холодная", "пропал", "wi-fi", "wi‑fi"],
            "category": "жалоба",
            "draft_template": "Приносим извинения за неудобства. Мы зафиксировали проблему ({}) и уже передали профильным специалистам."
        },
        {
            "keywords": ["записаться", "хочу"],
            "category": "другое",
            "draft_template": "Добрый день! Пожалуйста, уточните детали (к кому и на какое время вы хотите попасть), чтобы мы могли вам помочь."
        }
    ]
    
    for rule in rules:
        if any(keyword in msg_lower for keyword in rule["keywords"]):
            context = "справки/навигации" if rule["category"] == "справка" else "инфраструктуры/сервиса"
            return rule["category"], rule["draft_template"].format(context)
            
    return "другое", "Здравствуйте! Ваше обращение принято в обработку."

def main():
    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            messages = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Ошибка: Файл messages.txt не найден.")
        sys.exit(1)

    print(f"Загружено обращений: {len(messages)}\n" + "="*50)

    for i, msg in enumerate(messages, 1):
        category, draft = categorize_and_draft(msg)
        print(f"📝 Сообщение {i}: {msg}")
        print(f"🏷  Категория: {category.upper()}")
        print(f"💬 Черновик: {draft}")
        print("-" * 50)

if __name__ == "__main__":
    main()
