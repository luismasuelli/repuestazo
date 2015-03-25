from django.forms import Form, FileField


class UploadReplacementsForm(Form):
    """
    Formulario para la carga de repuestos.
    """

    replacements = FileField(required=True)