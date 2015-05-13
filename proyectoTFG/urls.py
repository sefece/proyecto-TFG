from django.conf.urls import patterns, include, url
from django.contrib import admin

from backend.views import UserViewSet, AdministratorViewSet, ApplicantViewSet, BidderViewSet, RevisorViewSet, OfferViewSet, ApplicationViewSet, TagViewSet, ItemViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'administrator', ApplicationViewSet)
router.register(r'applicant', ApplicantViewSet)
router.register(r'bidder', BidderViewSet)
router.register(r'offer', OfferViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'tag', TagViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectoTFG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     url(r'^admin/', include(admin.site.urls)),
)
