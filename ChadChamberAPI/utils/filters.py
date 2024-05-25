from django_filters.filters import Filter
from django.forms.fields import MultipleChoiceField


class MultipleValueField(MultipleChoiceField):
    """
    Field for selecting multiple values.
    """

    def __init__(self, *args, field_class, **kwargs):
        """
        Initialize the field.

        :param field_class: The field class used inside MultipleValueField.
        """
        self.inner_field = field_class()
        super().__init__(*args, **kwargs)

    def valid_value(self, value):
        """
        Check the validity of the value.

        :param value: The value to validate.
        :return: The result of the validation.
        """
        return self.inner_field.validate(value)

    def clean(self, values):
        """
        Clean the values.

        :param values: The values to clean.
        :return: The cleaned values.
        """
        return values and [self.inner_field.clean(value) for value in values]


class MultipleValueFilter(Filter):
    """
    Filter for selecting multiple values.
    """
    field_class = MultipleValueField

    def __init__(self, *args, field_class, **kwargs):
        """
        Initialize the filter.

        :param field_class: The field class used inside MultipleValueFilter.
        """
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, field_class=field_class, **kwargs)
