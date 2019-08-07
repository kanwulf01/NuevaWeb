from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin
<<<<<<< HEAD
from .viewsets import viewjoin
from .viewsets import OfertaViewSets
from .viewsets import VistaPrueba
=======

from .viewsets import OfertaViewSets

>>>>>>> b33096b293b252160e6f4f3ea609da2e58199d33


router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)

router.register('Oferta',OfertaViewSets)
<<<<<<< HEAD
router.register('test',viewjoin)
router.register('test1',VistaPrueba)
=======
>>>>>>> b33096b293b252160e6f4f3ea609da2e58199d33






urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


