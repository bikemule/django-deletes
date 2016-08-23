## Soft Deletes for Django. 

### Installation Instructions
1. pip install djangodeletes 
2. softdeletes will be available to import as ```from djangodeletes.softdeletes.models import SoftDeletable```

### Usage
1. Use Deletable class on the left most in the inhertance chain of the model. 
2. Use objects = DeletableManager.from_queryset(DeletableQuerySet)()
3. If you want to use a custom manager or a custom Queryset, make sure your custom manager inherits from DeletableManagerMixin and your custom QuerySet inherits from Deletable QuerySetMixin


### Caution
All cascading delete models should be made deletable, otherwise cascading delete would do a real delete to the foreignkey related models.
