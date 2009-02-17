from django.db import models
from whoosh.fields import STORED, ID, KEYWORD, TEXT

field_mapping = {
    models.AutoField: ID(unique=True, stored=True),
    models.BooleanField: STORED,
    models.CharField: TEXT,
    models.CommaSeparatedIntegerField: STORED,
    models.DateField: ID,
    models.DateTimeField: ID,
    models.DecimalField: STORED,
    models.EmailField: ID,
    models.FileField: ID,
    models.FilePathField: ID,
    models.FloatField: STORED,
    models.ImageField: ID,
    models.IntegerField: STORED,
    models.IPAddressField: ID,
    models.NullBooleanField: STORED,
    models.PositiveIntegerField: STORED,
    models.PositiveSmallIntegerField: STORED,
    models.SlugField: KEYWORD,
    models.SmallIntegerField: STORED,
    models.TextField: TEXT,
    models.TimeField: ID,
    models.URLField: ID,
    models.XMLField: TEXT,
}

class ModelSearch(object):
    pass
