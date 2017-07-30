from django.conf.urls import url, include
from django.contrib import admin

from todo_list.views import UserCreateView, TodoView, TodoCreateView,\
                            TodoItemDetailView, TodoItemUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls'), name="login"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', TodoView.as_view(), name='todo_view'),
    url(r'^create_item/$', TodoCreateView.as_view(), name='todo_create_view'),
    url(r'^todo/item/(?P<pk>\d+)/$', TodoItemDetailView.as_view(), name='todo_detail_view'),
    url(r'^todo/item/(?P<pk>\d+)/update/$', TodoItemUpdateView.as_view(), name='todo_update_view'),
]
