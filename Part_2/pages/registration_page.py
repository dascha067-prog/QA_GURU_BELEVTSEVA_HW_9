import os

from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        # Имя
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)

        # Пол
        browser.all('.custom-control-label').element_by(have.exact_text(user.gender)).click()

        # Телефон
        browser.element('#userNumber').type(user.phone)

        # Дата рождения
        browser.element('#dateOfBirthInput').click()

        # Год
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(
            have.exact_text(user.birth_year)
        ).click()

        # Месяц
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(
            have.exact_text(user.birth_month)
        ).click()

        # День
        browser.all('.react-datepicker__day').element_by(
            have.exact_text(str(int(user.birth_day)))
        ).click()

        # Предмет
        browser.element('#subjectsInput').type(user.subject).press_enter()

        # Хобби
        browser.all('.custom-control-label').element_by(have.text(user.hobby)).click()

        # Файл
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(current_dir, '..', 'resources', user.picture))

        browser.element('#uploadPicture').send_keys(file_path)

        browser.element('#uploadPicture').send_keys(file_path)

        # Адрес
        browser.element('#currentAddress').type(user.address)

        # Выбор штата
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=-option-]').element_by(have.text(user.state)).click()

        # Выбор города
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=-option-]').element_by(have.text(user.city)).click()

        # Отправка
        browser.element('#submit').click()

        return self

    def should_have_registered(self, user):
        results = browser.element('.table-responsive')

        results.should(have.text(f'{user.first_name} {user.last_name}'))
        results.should(have.text(user.email))
        results.should(have.text(user.gender))
        results.should(have.text(user.phone))
        results.should(have.text(f'{int(user.birth_day)} {user.birth_month},{user.birth_year}'))
        results.should(have.text(user.subject))
        results.should(have.text(user.hobby))
        results.should(have.text(user.picture))
        results.should(have.text(user.address))
        results.should(have.text(f'{user.state} {user.city}'))

        return self
