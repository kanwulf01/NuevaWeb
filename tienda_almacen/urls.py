from rest_framework import routers
from .viewsets import ProductoViewSets, ListaProductos2
from .viewsets import CategoriaViewSets


router = routers.SimpleRouter()
router.register('listaproducto',ListaProductos2)
router.register('producto', ProductoViewSets)
router.register('categoria', CategoriaViewSets)


urlpatterns = router.urls