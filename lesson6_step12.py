import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Функция для вычисления ответа
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждем, пока цена не станет равной $100 (ожидание не менее 12 секунд)
    # Используем text_to_be_present_in_element для проверки текста в элементе с id="price"
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Решаем математическую задачу на открывшейся странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 4. Вводим ответ и отправляем решение
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()

    # 5. Получаем проверочный код из alert
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()

    print("\n=== ПОЛНЫЙ ТЕКСТ В ОКНЕ ===")
    print(repr(alert_text))

    code = alert_text.split(': ')[-1].strip()
    print("\n=============================================")
    print(f"ВАШ КОД ДЛЯ STEPIK: {code}")
    print("=============================================\n")

finally:
    time.sleep(5)
    browser.quit()