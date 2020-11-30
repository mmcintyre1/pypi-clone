from pypi_org.services import user_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)
        self.name = self.request_dict.name.strip()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name:
            self.error = 'You must provide a name'
        elif not self.email:
            self.error = 'You must provide an email.'
        elif len(self.password) < 5:
            self.error = 'Your password must be at least 5 characters.'
        elif user_service.find_user_by_email(self.email):
            self.error = 'An account with that email already exists.'
