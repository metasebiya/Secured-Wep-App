"""feedback_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user import views as user_views
from feedback import views as feedback_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='index'),
    path('signup/', user_views.signup, name='signup'),
    path('login/', user_views.login, name='login'),
    path('dashboard/', feedback_views.dashboard, name='dashboard'),
    path('dash/', feedback_views.IndexView.as_view(), name="list_post"),
    path('dash/detail_view', feedback_views.DetailedView.as_view(), name="post_detail_view"),
    path('signup_request/', user_views.signup_request, name='signup_request'),
    path('login_request/', user_views.login_request, name='login_request'),
    path('logout_request/', user_views.logout_request, name='logout_request'),
    path('feedback/manage_post_list/', feedback_views.ManagePostList.as_view(), name="manage_post_list"),
    path('feedback/add_post/', feedback_views.PostCreateView.as_view(), name="add_post"),
    path('feedback/<pk>/edit_post/', feedback_views.UpdatePostView.as_view(), name="edit_post"),
    path('feedback/<pk>/delete_post/', feedback_views.DeletePostView.as_view(), name="delete_post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
