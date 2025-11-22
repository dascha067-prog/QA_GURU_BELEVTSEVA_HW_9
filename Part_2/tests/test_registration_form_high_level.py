from Part_2.models.user import User
from Part_2.pages.registration_page import RegistrationPage


def test_registration_form_high_level():
    user = User(
        first_name='Daria',
        last_name='Tester',
        email='daria.tester@example.com',
        gender='Female',
        phone='9001234567',
        birth_day='03',
        birth_month='November',
        birth_year='1995',
        subject='Maths',
        hobby='Reading',
        picture='avatar.png',
        address='Amsterdam Keizersgracht 123',
        state='NCR',
        city='Delhi'
    )

    page = RegistrationPage()

    page.open()
    page.register(user)
    page.should_have_registered(user)


