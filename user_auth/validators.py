from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MaxLengthValidator:
    def __init__(self, max_length=16):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("Password must be at most %(max_length)d characters long."),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "Your password must be at most %(max_length)d characters long."
        ) % {'max_length': self.max_length}
