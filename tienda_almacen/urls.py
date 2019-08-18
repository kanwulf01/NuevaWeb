from rest_framework import routers
from .viewsets import ProductoViewSets, ListaProductos2
from .viewsets import CategoriaViewSets, PCategoriaViewSets



router = routers.SimpleRouter()
router.register('listaproducto',ListaProductos2)
router.register('producto', ProductoViewSets)
router.register('categoria', CategoriaViewSets)
router.register('pCategoria', PCategoriaViewSets,basename='Producto')


urlpatterns = router.urls