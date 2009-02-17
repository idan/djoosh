
class MyModelSearch(djoosh.ModelSearch):
    ....
    
djoosh.search.register(MyModel, MyModelSearch)