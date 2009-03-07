from django.db import models
from whoosh.fields import STORED, ID, KEYWORD, TEXT

SEARCHFIELD_FOR_DBFIELD_DEFAULTS = {
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
    fields = None
    exclude = None
    searchfield_overrides = {}

    def __init__(self, model, engine):
        # TODO: not sure what admin is doing here with the dict.
        self.searchfield_overrides = None
        self._model = model
        self._engine = engine

    def searchfield_for_dbfield(self, db_field, **kwargs):
        """
        Hook for specifying the search Field instance for a given database Field
        instance.

        If kwargs are given, they're passed to the search Field's constructor.
        """
        if db_field.__class__ in self.searchfield_overrides:
            pass # use any custom mappings specificed
        elif db_field.__class in SEARCHFIELD_FOR_DBFIELDS_DEFAULTS
            pass # use the default mappings
        else:
            pass # raise an exception that this field could not be natively mapped.

    def post_save_callback(self, sender, instance, created, raw, **kwargs):
        """
        Hook for adding/updating documents in the whoosh index whenever a
        model instance is saved.
        """
        pass

    def post_delete_callback(self, sender, instance, **kwargs):
        """
        Hooke for deleting documents from the whoosh index whenever a model
        instance is deleted.
        """
        pass