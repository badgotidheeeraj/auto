
from django.contrib import admin
from django.conf import settings
from django.urls import path
from home import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login/", views.login),
    # path('convert-to-pdf/', views.convert_to_pdf, name='convert_to_pdf'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
