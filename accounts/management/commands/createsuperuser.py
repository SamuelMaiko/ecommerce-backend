from django.contrib.auth import get_user_model
from django.core.management.commands import createsuperuser
from django.core.exceptions import ValidationError

class Command(createsuperuser.Command):
    help = 'Create a superuser.'

    def handle(self, *args, **options):
        username_field = get_user_model().USERNAME_FIELD
        email = None

        # Prompt for phone number
        while email is None:
            email = input("Email: ")
            try:
                get_user_model()._default_manager.get(**{username_field: email})
            except get_user_model().DoesNotExist:
                pass
            else:
                self.stderr.write("Error: That phone number is already taken.")
                email = None

        # Set username to phone number
        options['username'] = email

        # Call the original createsuperuser command
        return super().handle(*args, **options)
