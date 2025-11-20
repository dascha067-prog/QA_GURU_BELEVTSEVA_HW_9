class LeftPanel:
    def __init__(self, app):
        self.app = app

    def open(self, category, item):
        # Здесь имитация перехода, если нужно
        print(f'Открываю раздел {category} -> {item}')

    def open_simple_registration_form(self):
        # Шорткат: вызывает другой метод того же объекта
        self.open('Elements', 'Text Box')
