from collections.abc import Generator
import re


def question_generator() -> Generator[tuple[str, str], None, None]:
    yield ("Столица Франции?", "Париж")
    yield ("2 + 2?", "4")
    yield ("Главный герой 'Гамлета'?", "Гамлет")


def check_answer(answer: str, correct: str) -> bool:
    if re.match(r'^\d+$', correct):
        return bool(re.match(r'^\d+$', answer)) and answer == correct
    return bool(re.match(r'^[a-zA-Zа-яА-ЯёЁ]+$', answer)) and answer.lower() == correct.lower()


if __name__ == "__main__":
    score = 0
    test_cases = [
        (("Столица Франции?", "Париж"), "париж"),  # Правильно
        (("2 + 2?", "4"), "4"),  # Правильно
        (("Главный герой 'Гамлета'?", "Гамлет"), "Офелия"),  # Неправильно
        (("2 + 2?", "4"), "четыре"),  # Неправильно (не число)
        (("Столица Франции?", "Париж"), "Paris123"),  # Неправильно (не только буквы)
        (("Столица Франции?", "Париж"), ""),  # Неправильно (пустой ответ)
    ]
    for (question, correct), user_answer in test_cases:
        print(f"Вопрос: {question}")
        print(f"Ответ: {user_answer}")
        if check_answer(user_answer, correct):
            score += 1
            print(f"Результат: Правильно! Очки: {score}")
        else:
            score -= 1
            print(f"Результат: Неправильно. Правильный ответ: {correct}. Очки: {score}")
        print()
    print(f"Итоговый счет: {score}")