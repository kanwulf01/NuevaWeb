from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin

from .viewsets import OfertaViewSets



router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)

router.register('Oferta',OfertaViewSets)






urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


