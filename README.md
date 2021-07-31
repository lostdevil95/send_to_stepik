# sendToStepik


Немного надоело вручную копировать и вставлять число (типа такого 28.95479603721765) и воодушевленный простотой Python&Selenium рашил этот процесс автоматизировать. Простота улетучилась практически мгновенно ))

В общем, модуль втоматом закидывает ответы c числами на курс Автоматизация тестирования с помощью Selenium и Python на сайте [stepik.org](https://stepik.org/)

## Как работает

Всё сложить в папку, где лежат файлы с выполняемыми заданиями.

Модуль `auth.py` - сохраняет сеанс браузера в `chrome_options` в текущей папке.


Выполнить один раз в начале, он запустит браузер, даст время 30 секунд залогиниться и сохранит сеанс в папку chrome_options.



Далее модуль `sendToStepik.py`

Принимает два аргумента ссылку на задание и число-ответ.
```python
sendToStepik(task_link, answer)
```

Вызывается из файла с заданием так:
```python

from sendToStepik import sendToStepik

# в переменную task_link вставить адрес страницы с заданием
task_link = 'https://stepik.org/lesson/165493/step/5?unit=140087'


# тут основное решение задачи


#в конце решения добавить строки:
# Копирование числа из алерта
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
answer = alert_text.split(': ')[-1]

time.sleep(1)
browser.quit()

# Отправка решения на Stepik:
sendToStepik(task_link, answer)

```

