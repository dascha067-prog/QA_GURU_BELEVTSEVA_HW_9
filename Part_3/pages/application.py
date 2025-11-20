from Part_3.pages.registration_page3 import SimpleRegistrationPage3
from Part_3.pages.left_panel import LeftPanel


class ApplicationManager:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage3()
        self.left_panel = LeftPanel(self)


app = ApplicationManager()
