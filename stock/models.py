from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.apps.track.models import Trackable
from openpyxl import load_workbook
from openpyxl.utils.exceptions import CellCoordinatesException, InsufficientCoordinatesException, InvalidFileException


class ReplacementQueryset(models.QuerySet):
    """
    Queryset con algunas consultas para los repuestos.
    """

    def cheapest(self):
        """
        Los repuestos mas baratos.
        """
        return self.filter(score__in=['E', 'F'])


class Replacement(Trackable):
    """
    Un repuesto y su informacion asociada. Por ahora solamente ponemos los datos, sin indexar ni nada.
    """

    class LoadError(Exception):
        """
        Excepciones de carga.
        """

    SCORES = (
        ('A', u'A'),
        ('B', u'B'),
        ('C', u'C'),
        ('D', u'D'),
        ('E', u'E'),
        ('F', u'F'),
    )

    CATEGORIES = (
        ('REPUESTOS', u'Replacements'),
        ('ACCESORIOS', u'Accesories'),
    )

    objects = ReplacementQueryset.as_manager()

    dealer = models.CharField(max_length=20, blank=False, null=False, verbose_name=_(u'Dealer'))
    score = models.CharField(max_length=1, blank=False, null=False, verbose_name=_(u'Score'))
    category = models.CharField(max_length=20, blank=False, null=False, verbose_name=_(u'Category'))
    code = models.CharField(max_length=20, null=False, blank=False, verbose_name=_(u'Code'))
    product = models.CharField(max_length=40, null=False, blank=False, verbose_name=_(u'Product'))
    brand = models.CharField(max_length=20, blank=False, null=False, verbose_name=_(u'Brand'))
    model = models.CharField(max_length=255, blank=True, null=False, verbose_name=_(u'Model'))
    year = models.SmallIntegerField(validators=[MinValueValidator(2000)], null=True, blank=True, verbose_name=_(u'Year'))
    stock = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True, verbose_name=_(u'Stock'))
    cost = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True, verbose_name=_(u'Cost'))
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True, verbose_name=_(u'Price'))
    offer = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True, verbose_name=_(u'Offer'))

    @property
    def discount(self):
        """
        Estima cual es el descuento (entre 0 y 99.99... - si es negativo es un "sobrecuento" :p)
        """
        offer = self.offer or self.price or self.cost
        price = self.price or self.cost
        if not offer or not price:
            return None
        return "%1.2f%%" % ((offer - price) * Decimal(-100.0) / price)

    @classmethod
    def load_xls(cls, xls_file):
        """
        Limpia y carga todo desde un xml.
        """
        cls.objects.all().delete()

        def int_(v):
            try:
                return int(v)
            except Exception:
                return None

        def float_(v):
            try:
                return float(v)
            except Exception:
                return None

        try:
            workbook = load_workbook(xls_file, read_only=True, data_only=True)
            rows = workbook['rwservlet'].rows
            next(rows)  # descartamos la primera fila
            cls.objects.bulk_create([
                cls(dealer=dict_.get('A', ''),
                    score=dict_.get('B', ''),
                    category=dict_.get('C', ''),
                    code=dict_.get('D', ''),
                    product=dict_.get('E', ''),
                    brand=dict_.get('F', ''),
                    model=dict_.get('G', ''),
                    year=int_(dict_.get('H', '')),
                    stock=float_(dict_.get('I', '')),
                    cost=float_(dict_.get('J', '')),
                    price=float_(dict_.get('K', '')),
                    offer=float_(dict_.get('M', ''))) for dict_ in ({cell.column: cell.value for cell in row if cell.column} for row in rows)
            ])
        except (InvalidFileException, CellCoordinatesException, InsufficientCoordinatesException):
            raise cls.LoadError("An error occurred while loading xls")

    class Meta:
        verbose_name = _(u'Replacement')
        verbose_name_plural = _(u'Replacements')