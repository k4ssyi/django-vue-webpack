from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='vue/index.html')),
    path('todo/', include('apps.todo.urls'))
)

if settings.DEBUG:
    import debug_toolbar
    # デバッグツールバーを表示
    # 無効なURLがきたらリダイレクトする
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
