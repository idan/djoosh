import djoosh
import woosh


class MyIndexOptions(djoosh.IndexOptions):
    field1 = woosh.TEXT(...woosh syntax...)
    field2 = djoosh.Keyword(...woosh syntax...)
    field2 = djoosh.Id(...woosh syntax...)
    field2 = djoosh.Stored(...woosh syntax...)
    

class MyModelSearch(djoosh.ModelSearch):
    exclude = ("field1", "field2",) # exclude fields from indexing
    fields = ("field1", "field2",) # explicity include fields for indexing
    index_options = MyIndexOptions
    
djoosh.search.register(MyModel, MyModelSearch)


-----------
    
class Text(djoosh.IndexField):
    def __init__(bool stored=false, analyzer=woosh.StandardAnalyzer):
        
        
admin.site.register(MyModel, admin.ModelAdmin)

TEXT: stored?, analyzer, 
KEYWORD
ID
STORED
