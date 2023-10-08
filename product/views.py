from itertools import product

from django.shortcuts import render, redirect

from product.models import Product, Category, Comment
from product.forms import CategoryCreate, ProductsCreate, CommentCreateForm

from product.constans import PAGINATION_LIMIT


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        posts = Post.objects.all().order_by('-create_date')
        # posts = Post.objects.all().order_by('-rate')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            posts = posts.filter(title__contains=search) | posts.filter(description__contains=search)

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'products': products
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=context_data)


def products_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': CommentCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = CommentCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                name=form.cleaned_data.get('name'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context_data = {'form': Product}
        return render(request, 'products/', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductsCreate(data, files)
        if form.is_valid():
            Product.objects.create(
                img=form.cleaned_data.get('img'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                category=form.cleaned_data.get('category'),
                prize=form.cleaned_data.get('prize'),
                phone_number=form.cleaned_data.get('phone_number')

            )
            return redirect('/products/')
        return render(request, 'products/categories.html', context={'form': form})


def create_category_view(request):
    if request.method == 'GET':
        context_data = {'form': CategoryCreate}

        return render(request, 'products/categories.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        f = CategoryCreate(data, files)

        if f.is_valid():
            Category.objects.create(
                title=f.cleaned_data.get('title')

            )
            return redirect('/category/')
        return render(request, 'products/categories.html', context={'form': f})