from stub_io import StubIO
from repositories.user_repository import UserRepository
from services.user_service import UserService
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    #def create_user(self, username, password):
    #    self._user_service.create_user(username, password)
    def create_user(self, username, password):
        try:
            self._user_service.create_user(username, password)
            self._io.write("User registered successfully")
        except Exception as e:
            self._io.write(str(e))
