from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, View

from core.models import ProductModel

class CartView(ListView):
    """
        カート情報を閲覧する
    """
    model = ProductModel
    template_name = 'main/cart.html'


    def get_queryset(self):
        cart = self.request.session.get('cart', None)
        self.queryset = []
        for id, quantity in cart['products'].items():
            obj = ProductModel.objects.get(pk=id)
            obj.quantity  = quantity
            self.queryset.append(obj)
        return super().get_queryset()


class AddCartView(View):
    """
        カートに商品を追加する 
        現在セッションに格納されているカート情報を読み出し
        存在が無ければ新規作成、あれば追加して再度書き込み
    """

    def post(self, request):
        # FIXME: バリデーションしていない。
        id = request.POST.get('id')
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', None)
        if cart is None:
            cart = {'products':{}}

        if id in cart['products']:
            cart['products'][id] += quantity
        else:
            cart['products'][id] = quantity
    
        request.session['cart'] = cart
        return redirect('/cart/')


class RemoveCartView(View):
    """
        カートから商品を削除する
    """

    def post(self, request):
        # FIXME: バリデーションしていない。
        id = request.POST.get('id')

        cart = request.session.get('cart', None)

        if cart is None:
            redirect('/')

        if id in cart['products']:
            del cart['products'][id]
    
        request.session['cart'] = cart
        return redirect('/cart/')