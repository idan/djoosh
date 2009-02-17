
# dilemma: directly import woosh or not?
# We need access to the various index field types (TEXT, ID, KEYWORD, STORED)
# Plan A: We could "hide" woosh and only expose djoosh namespace, but this gets a
# little complex.
# Plan B: Alternately, we can import woosh into djoosh and then it is
# automatically pulled in when we do "import djoosh" here.
# Plan C: import woosh directly.

import djoosh
import woosh

class MyIndexOptions(djoosh.IndexOptions):
    field1 = woosh.TEXT(...woosh syntax...) # see above for import considerations
    field2 = djoosh.Keyword(...woosh syntax...)
    field2 = djoosh.Id(...woosh syntax...)
    field2 = djoosh.Stored(...woosh syntax...)
    

class MyModelSearch(djoosh.ModelSearch):
    # simple-style exclude, fields for people who just want to use automatic
    # mapping of django model fields to woosh fields.
    exclude = ("field1", "field2",) # exclude fields from indexing
    fields = ("field1", "field2",) # explicity include fields for indexing
    
    # if you want greater control over mapping of model fields to woosh fields
    # this is much like custom forms for admin.
    index_options = MyIndexOptions

# register the search definition for the model
djoosh.register(MyModel, MyModelSearch)
