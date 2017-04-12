from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cms_put.views.show', name='Paginas disponibles'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(.+)', 'cms_put.views.show_content', name='Vamos a la pagina o añadimos')
)

