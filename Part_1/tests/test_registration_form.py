from Part_1.pages.registration_page import RegistrationPage


def test_registration_form():
    # Создаю объект страницы
    registration_page = RegistrationPage()

    # Выполняю цепочку шагов
    registration_page.open() \
        .fill_first_name('Daria') \
        .fill_last_name('Tester') \
        .fill_email('daria.tester@example.com') \
        .select_gender('Female') \
        .fill_phone('9001234567') \
        .fill_birth_date('November', '1995', '03') \
        .fill_subject('Maths') \
        .choose_hobby('Reading') \
        .upload_picture('avatar.png') \
        .fill_address('Amsterdam, Keizersgracht 123') \
        .select_state('NCR') \
        .select_city('Delhi') \
        .submit() \
        .should_have_registered(
        # Проверяю значения в таблице результатов
        'Daria Tester',
        'daria.tester@example.com',
        'Female',
        '9001234567',
        '03 November,1995',
        'Maths',
        'Reading',
        'avatar.png',
        'Amsterdam, Keizersgracht 123',
        'NCR Delhi'
    )
