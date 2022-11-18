from http.client import FOUND
from django.urls import reverse
#from django.core.urlresolvers import reverse
#este codigo de la linea 2 no sirve ya que es una version anterior
from django.test import TestCase
from django.urls import resolve
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

#EN CASO QUE SALIERA EL NUEMOR 500 EN LA CONSOLA INDICA QUE HUBO UN ERROR EN INTERNO DENTRO DEL CODIGO
# Create your tests here.
