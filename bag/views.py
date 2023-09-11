from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from products.models import Product
from .models import WishList


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}'
            )
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


class WishListView(LoginRequiredMixin, generic.View):
    login_url = 'account_login'
    redirect_field_name = 'login'

    def get(self, *args, **kwargs):
        wish_items = WishList.objects.filter(user=self.request.user)
        context = {
            'wish_items': wish_items
        }
        return render(self.request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request):

    if request.method == "POST":
        product_wish_id = request.POST.get('product-id')
        product_wish = Product.objects.get(id=product_wish_id)

        try:
            wish_item = WishList.objects.get(user=request.user, product=product_wish)
            if wish_item:
                messages.info(request, f'{product_wish.name} is already in your Wishlist')
        except:
            WishList.objects.create(user=request.user, product=product_wish)
            messages.success(request, f'Added {product_wish.name} to your Wishlist')
        finally:
            return HttpResponseRedirect(reverse('wishlist'))


@login_required
def remove_from_wishlist(request):
    if request.method == "POST":
        item_id = request.POST.get('item-id')
        WishList.objects.filter(id=item_id).delete()
        return HttpResponseRedirect(reverse('wishlist'))
