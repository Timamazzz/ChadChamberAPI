from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework import serializers
import re


class PhoneField(serializers.CharField):
    """
    Field for serializing and validating phone numbers.
    """
    PHONE_FIELD_DEFAULT_PLACEHOLDER = '+7'
    PHONE_FIELD_DEFAULT_MASK = '999 999-99-99'
    PHONE_FIELD_DEFAULT_REGEX = r'd{10}$'
    PHONE_FIELD_DEFAULT_LABEL = 'Phone number'

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.style = kwargs.get('style', {'placeholder': self.PHONE_FIELD_DEFAULT_PLACEHOLDER,
                                          'mask': self.PHONE_FIELD_DEFAULT_MASK})
        self.label = kwargs.get('label', self.PHONE_FIELD_DEFAULT_LABEL)

    def validate(self, value):
        """
        Overridden method for validating the field's value.
        """
        super().validate(value)
        phone_pattern = re.compile(self.PHONE_FIELD_DEFAULT_REGEX)
        if not phone_pattern.match(value):
            raise DRFValidationError("Invalid phone number format")

        return value


class PasswordField(serializers.CharField):
    """
    Field for serializing and validating passwords.
    """
    def __init__(self, *args, **kwargs):
        min_length = kwargs.pop('min_length', 8)
        super().__init__(*args, **kwargs)
        self.min_length = min_length
