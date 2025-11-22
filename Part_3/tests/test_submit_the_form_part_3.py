from Part_3.data.users import student
from Part_3.pages.application import app


def test_simple_registration_form(windows_size):
    app.left_panel.open_simple_registration_form()  # shortcut
    app.simple_registration.open()  # загрузка формы
    app.simple_registration.register(student)
    app.simple_registration.should_have_registered(student)
