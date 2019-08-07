from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin
from .viewsets import viewjoin
from .viewsets import OfertaViewSets
from .viewsets import VistaPrueba


router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)

router.register('Oferta',OfertaViewSets)
router.register('test',viewjoin)
router.register('test1',VistaPrueba)






urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


