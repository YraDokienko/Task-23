from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PizzaHomeView.as_view(), name='home'),
    path('pizza-form-add/', views.PizzaFormAddView.as_view(), name='pizza_add'),
    path('cart/', views.PizzaCartView.as_view(), name='cart'),
    path('stop_spam_page/', TemplateView.as_view(template_name='stop_spam_page.html')),
    path('cart/shipping/', views.ShippingOrderView.as_view(), name='shipping'),
    path('pizza-price-update/', views.PizzaPriceUpdateView.as_view(), name='price_update'),
    path('add-pizza-to-order/', views.AddPizzaToOrderView.as_view()),
    path('del_instance/<int:id>', views.AddPizzaToOrderView.del_instance, name='delete'),
    path('pizza-update/<int:pk>/edit/', views.PizzaUpdateView.as_view(), name='pizza_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
