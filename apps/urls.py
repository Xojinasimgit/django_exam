from django.urls import path

from apps.views import about, agent_single, agents_grid, blog_grid, index, blog_single, contact, property_grid, \
    property_single, signin, signup, add_category, add_blog, log_out

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('agent_single/<pk>/', agent_single, name='agent_single'),
    path('agents_grid/', agents_grid, name='agents_grid'),
    path('blog_grid/', blog_grid, name='blog_grid'),
    path('blog_single/<int:pk>/', blog_single, name='blog_single'),
    path('contact/', contact, name='contact'),
    path('property_grid/', property_grid, name='property_grid'),
    path('property_single/<int:pk>/', property_single, name='property_single'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', log_out, name='logout'),
    path('add_category/', add_category, name='add_category'),
    path('add_blog/', add_blog, name='add_blog'),
]
