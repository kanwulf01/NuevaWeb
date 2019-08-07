from rest_framework import routers
from .viewsets import ProductoViewSets, ListaProductos2



router = routers.SimpleRouter()
router.register('listaproducto',ListaProductos2)
router.register('producto', ProductoViewSets)


urlpatterns = router.urls