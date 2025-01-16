from django.urls import reverse_lazy, reverse
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect

class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product




class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})
