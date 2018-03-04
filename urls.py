from django.urls import path
from django.conf.urls.static import static
from alanard_web_node import settings

from . import views

urlpatterns = [] + static("/", document_root=settings.ALANARDTOOLMAINTAIN_HOME_ROOT)

