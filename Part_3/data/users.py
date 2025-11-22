import dataclasses


@dataclasses.dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = SimpleUser(
    full_name='Darya Tester',
    email='darya.tester@example.com',
    current_address='Test street, 10',
    permanent_address='QA city'
)
