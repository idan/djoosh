from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.db.models.base import ModelBase
from djoosh.options import ModelSearch

class AlreadyRegistered(Exception):
    pass

class NotRegistered(Exception):
    pass

class SearchEngine(object):
    
    def __init__(self, name=None):
        self._registry = {} # model_class class -> search_class instance
        if name is None:
            name = ''
        else:
            name += '_'
        self.name = name

    def register(self, model_or_iterable, search_class=None, **options):
        """
        Registers the given model(s) with the given search class.

        The model(s) should be Model classes, not instances.

        If an search class isn't given, it will use ModelSearch (the default
        search options). If keyword arguments are given -- e.g., exclude --
        they'll be applied as options to the search class.

        If a model is already registered, this will raise AlreadyRegistered.
        """
        if not search_class:
            search_class = ModelSearch
        if isinstance(model_or_iterable, ModelBase):
            model_or_iterable = [model_or_iterable]
        for model in model_or_iterable:
            if model in self._registry:
                raise AlreadyRegistered('The model %s is already registered' % model.__name__)
            # If we got **options then dynamically construct a subclass of
            # search_class with those **options.
            if options:
                # For reasons I don't quite understand, without a __module__
                # the created class appears to "live" in the wrong place,
                # which causes issues later on.
                options['__module__'] = __name__
                search_class = type("%sSearch" % model.__name__, (search_class,), options)            
            self._registry[model] = search_class(model, self)
            # TODO: make sure that signals are attached
            

    def unregister(self, model_or_iterable):
        """
        Unregisters the given model(s).
    
        If a model isn't already registered, this will raise NotRegistered.
        """
        if isinstance(model_or_iterable, ModelBase):
            model_or_iterable = [model_or_iterable]
        for model in model_or_iterable:
            if model not in self._registry:
                raise NotRegistered('The model %s is not registered' % model.__name__)
            del self._registry[model]