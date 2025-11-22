from pathlib import Path
from selene import browser, by, have, command


class RegistrationPage:

    def open(self):
        # Открываю страницу формы
        browser.open('/automation-practice-form')
        return self  # возвращаю self для Fluent-интерфейса

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, gender):
        browser.element('#genterWrapper').element(by.text(gender)).click()
        return self

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birth_date(self, month, year, day):
        # Открываю календарь
        browser.element('#dateOfBirthInput').click()

        # Выбор месяца (выпадающий <select> → внутри <option>)
        browser.element('.react-datepicker__month-select').element(
            f'option[value="{self._month_to_index(month)}"]'
        ).click()

        # Выбор года
        browser.element('.react-datepicker__year-select').element(
            f'option[value="{year}"]'
        ).click()

        # Выбор дня (нужный день, не серый)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

        return self

    def _month_to_index(self, month):
        months = {
            'January': '0', 'February': '1', 'March': '2',
            'April': '3', 'May': '4', 'June': '5',
            'July': '6', 'August': '7', 'September': '8',
            'October': '9', 'November': '10', 'December': '11'
        }
        return months[month]

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def choose_hobby(self, hobby):
        browser.element('#hobbiesWrapper').element(by.text(hobby)).click()
        return self

    def upload_picture(self, filename):
        # Путь к файлу внутри папки resources
        picture_path = str(Path(__file__).parent.parent / 'resources' / filename)
        browser.element('#uploadPicture').set_value(picture_path)
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def select_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    # Проверки результата
    def should_have_registered(self, *expected_values):
        # Проверяю, что модалка появилась
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        # Проверяю все значения в таблице результата
        browser.all('.modal-content table tbody tr td:nth-child(2)').should(
            have.exact_texts(*expected_values)
        )
        return self

    def register(self, user):
        return (
            self
            .fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_email(user.email)
            .select_gender(user.gender)
            .fill_phone(user.phone)
            .fill_birth_date(user.birth_month, user.birth_year, user.birth_day)
            .fill_subject(user.subject)
            .choose_hobby(user.hobby)
            .upload_picture(user.picture)
            .fill_address(user.address)
            .select_state(user.state)
            .select_city(user.city)
            .submit()
        )
