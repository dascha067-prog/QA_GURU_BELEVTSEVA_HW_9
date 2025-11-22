# 8. Page Objects
 
1. [Page Object](#Page Object)
2. [Модульная парадигма](#Модульная парадигма)
3. [Объектно-ориентированная парадигма](#Объектно-ориентированная парадигма)
4. [Различие между модульной и объектно-ориентированной парадигмой](Различие между модульной и объектно-ориентированной парадигмой)
5. [Steps Object](#Steps Object)
6. [Fluent Page Object](#Fluent Page Object)
7. [Application Manager](#Application Manager)
8. [Property](#Property)
9. [Assertion-free page objects](Assertion-free page objects)
10. [Принцип композиции(Composition over inheritance)](Принцип композиции(Composition over inheritance))

# Page Object 
Паттерн Page Object - это шаблон проектирования, который позволяет абстрагировать взаимодействие с веб-страницей.
Он позволяет разделить тесты и логику взаимодействия с элементами страницы. 
Это позволяет упростить поддержку тестов, так как при изменении страницы, вам нужно будет внести изменения только в одном месте.

Пример Page Object:
```
 from selene import browser, have

class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self
   ```

Пример использования Page Object:
```
# file: test_registration_form.py

def test_registration():
    registration_page = RegistrationPage()
    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Doe')
```
В данном примере мы создали класс RegistrationPage, который содержит методы для взаимодействия с элементами страницы.
Затем мы создали объект registration_page(переменную которая проинициализированная классом) и вызвали методы fill_first_name и fill_last_name для заполнения формы регистрации.

# Модульная парадигма
Модульная парадигма - это парадигма программирования, в которой программа разделяется на отдельные модули, каждый из которых выполняет определенную функцию. 
Это позволяет упростить разработку, тестирование и поддержку программы. 
Инкапсуляция в контексте использования модульной парадигмы - это способность модуля скрывать свою реализацию от других модулей.

Пример модульной парадигмы:
```
# module1.py
def func1():
    pass
    
# module2.py
def func2():
    pass
    
# main.py
import module1
import module2

module1.func1()
module2.func2()
```
В данном примере мы создали два модуля(файлы): module1 и module2, каждый из которых содержит определенную функцию. 
Затем мы импортировали эти модули в файл main.py и вызвали функции из них.

# Объектно-ориентированная парадигма
Объектно-ориентированная парадигма - это парадигма программирования, в которой программа разделяется на отдельные объекты.
Каждый из которых содержит данные и методы для их обработки.
Это позволяет упростить разработку, тестирование и поддержку программы.

# Различие между модульной и объектно-ориентированной парадигмой
Основное различие между модульной и объектно-ориентированной парадигмой заключается в том, что в модульной парадигме программа разделяется на отдельные модули, каждый из которых выполняет определенную функцию. 
В то время как в объектно-ориентированной парадигме программа разделяется на отдельные объекты, каждый из которых содержит данные и методы для их обработки.

# Steps Object
Steps Object - это когда мы инкапсулируем шаги пользователя, а именно не только скрытие поиска локаторов, но и скрытие логики взаимодействия с элементами страницы(проверки, клики, вводы и т.д.).

Пример использования Steps Object:
```
class RegistrationSteps:
    def __init__(self):
        self.registratered_user_data= browser.element('.table').all('td').even.should(have.exact_texts('John', 'Doe'))


# file: test_registration_form.py

def test_registration():
    registration_steps = RegistrationSteps()
    registration_steps.registratered_user_data
```
# Fluent Page Object
Fluent Page Object - это подход к созданию Page Object, при котором методы возвращают сам объект, что позволяет использовать цепочку вызовов.

Пример Fluent Page Object:
```
from selene import browser, have

class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
    
    def open(self):
        browser.open('https://example.com/registration')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self
```
Пример использования Fluent Page Object:
```
# file: test_registration_form.py

def test_registration():
  (RegistrationPage()
    .open()
    .fill_first_name('John')
    .fill_last_name('Doe')
    )
```
# Application Manager
Application Manager - это класс, который инкапсулирует в себе все Page Object и другие объекты, необходимые для взаимодействия с приложением.

Пример Application Manager:
```
# file: application.py

from selene import browser
from registration_page import RegistrationPage
from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.profile = ProfilePage()

app = Application()
```
Пример использования Application Manager:
```
# file: test_registration_form.py
from application import app

def test_registration():
    app.registration_page.open()
    app.registration_page.fill_first_name(users.admin)
    app.profile.should_have_user(users.admin)
```
# Property
Property - это специальный атрибут класса, который позволяет управлять доступом к данным.

Пример использования property:
```
class RegistrationPage:

    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').even
```
В данном примере мы создали атрибут registered_user_data, который возвращает элементы таблицы с данными зарегистрированного пользователя. 
При его использовании, мы можем обращаться к нему как к обычному атрибуту класса, без указания скобок().
```
registration_page = RegistrationPage()
registration_page.registered_user_data.should(have.exact_texts('John', 'Doe'))
```
Метод registered_user_data стал похожим на переменную, которую можно использовать в тестах.

Также можно вместо @property использовать init метод:
```
class RegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even
```
Таким образом, мы можем использовать атрибут registered_user_data как обычную переменную.

# Assertion-free page objects
```Assertion-free page objects``` - это подход к созданию Page Object, при котором в них отсутствуют проверки(Page Object свободные от assert-ов).

Пример подхода ```assertion-free page objects``` представлен выше в разделе Property, где мы создали ``` registered_user_data``` как атрибут класса, который возвращает элементы таблицы с данными зарегистрированного пользователя, но без проверок.

# Принцип композиции(Composition over inheritance)
```Принцип композиции(Composition over inheritance)``` это принцип программирования, который гласит, что лучше использовать композицию объектов, чем наследование. 
Это позволяет уменьшить связанность между классами и упростить их взаимодействие.

Пример использования Принципа композиции:
```
class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')

class ProfilePage:
    def __init__(self):
        self.user_data = browser.element('.table').all('td').even

class Application
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.profile_page = ProfilePage()
```
В данном примере мы создали классы ```RegistrationPage``` и ```ProfilePage```, которые содержат методы для взаимодействия с элементами страницы. 
Затем мы создали класс ``` Application```, который содержит объекты```RegistrationPage``` и ```ProfilePage```. 
Таким образом, мы использовали композицию объектов, чтобы упростить взаимодействие между классами.