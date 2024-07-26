import re

def process_sentence(sentence):
    # Найти все цифры в предложении
    digits = re.findall(r'\d+', sentence)
    
    # Обработать каждую найденную цифру
    processed_digits = []
    for digit in digits:
        if len(digit) == 1:
            processed_digits.append('0' + digit)
        elif len(digit) == 2:
            processed_digits.append(digit)
        else:
            processed_digits.append(digit)
    
    # Заменить цифры в предложении на обработанные цифры
    for original, processed in zip(digits, processed_digits):
        sentence = sentence.replace(original, processed, 1)
    
    return sentence

# Пример использования
sentence = "сегодня, 2 июля в 3 часа дня было 20 градусов тепла."
result = process_sentence(sentence)
print(result)
