from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    '''Class to generate a token for new user'''

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.profile.email_confirmed)
        )


accountactivationtoken=AccountActivationTokenGenerator()

