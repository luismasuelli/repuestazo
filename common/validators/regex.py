from django.core.validators import RegexValidator as _RegexValidator
import unicodedata
import six


class AccentsAgnosticRegexValidator(_RegexValidator):
    """
    This validator performs a validation after normalizing the unicode
      string. This means: will validate as if the string value did not
      have accents in letters.
    """

    def __call__(self, value):
        return super(AccentsAgnosticRegexValidator, self).__call__(
            ''.join(c for c in unicodedata.normalize('NFD', six.text_type(value)) if unicodedata.category(c) != 'Mn')
        )