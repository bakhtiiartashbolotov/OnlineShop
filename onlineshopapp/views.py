from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, DetailView

from onlineshopapp.models import Category, Product;

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data();
        context['products'] = Product.objects.all();
        context['categories'] = Category.objects.all();
        return context;

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_object(self, queryset=None):
        return get_object_or_404(Category, id=self.kwargs.get('category_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        context['categories'] = Category.objects.all()
        return context