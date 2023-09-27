import requests
from django.http import JsonResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import PortfolioAssetsUpdateSerializer, AssetsSerializer
from accounts.models import User
from market.models import Portfolio, Market, Assets, Comment, Like, DisLike
from market.serializer import PortfolioSerializer, CommentSerializer, LikeSerializer, DisLikeSerializer, \
    MarketSerializer, PortfolioUpdateSerializer


class MarketList(viewsets.GenericViewSet, mixins.ListModelMixin):
    # permission_classes = (IsAuthenticated,)

    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketDetail(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, **kwargs):
        return Market.objects.get(id=request.data['id'])


# ---------------------------------------------------------------
# --------------------- Portfolio View Classes ------------------
# ---------------------------------------------------------------

# -------------------- Create Portfolio View --------------------


class CreatePortfolioApiView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create a portfolio for request.user
    """
    serializer_class = PortfolioSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.get(pk=request.user.pk)
        queryset = Portfolio.objects.create(user=user.user,
                                            name=data['name']
                                            , market=Market.objects.get(pk=int(request.POST.get('market', ''))))

        queryset.save()
        """
        list of assets user want to have in the portfolio when create it
        
        """
        for asset in data['assets']:
            asset_obj = Assets.objects.get(asset_name=asset['asset_name'])
            queryset.assets.add(asset_obj)

        serializer = PortfolioSerializer(queryset)
        return Response(serializer.data)


# -------------------- Portfolio's List View --------------------

class PortfolioList(viewsets.GenericViewSet, mixins.ListModelMixin):
    # permission_classes = (IsAuthenticated,)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        current_user = self.request.user.pk
        return Portfolio.objects.filter(user=current_user)


# --------------- Detail and Delete Portfolio View ---------------

class PortfolioDetailDestroy(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin, viewsets.GenericViewSet
                             ):
    
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)


class AssetsDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet
                   ):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer


# --------------------- Update Portfolio name View --------------------

class PortfolioNameUpdate(mixins.UpdateModelMixin, viewsets.GenericViewSet
                          ):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioUpdateSerializer

    def put(self, request, pk):
        return self.update(request, pk)


class PortfolioAssetsUpdate(mixins.UpdateModelMixin, viewsets.GenericViewSet
                            ):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioAssetsUpdateSerializer


# ---------------------------------------------------------------
# ---------------------- Comment View Class----------------------
# ---------------------------------------------------------------

"""
only when comment be active users can see the comment,admin can see comments and active it after active=True,
show comment in specific asset's comment 
"""


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def queryset(self, request, **kwargs):
        user = User.objects.get(id=request.data['id'])
        print(user)
        new_comment = Comment.objects.create(name=user['name']
                                             , asset=Assets.objects.get(pk=int(request.POST.get('asset', '')))
                                             , users=user)

        new_comment.save()
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)


# --------------------- Active Comment View ---------------------
"""
show list of every asset's comment list if active=True
"""


class ActiveComment(mixins.ListModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(active=True)


# ---------------------------------------------------------------
# ----------------------- Like View Class------------------------
# ---------------------------------------------------------------

class LikeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.order_by('created_at')

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.Like_count = obj.like_count + 1
        obj.save(update_fields=("like_count",))
        return super().retrieve(request, *args, **kwargs)


# ---------------------------------------------------------------
# ---------------------- Dislike View Class----------------------
# ---------------------------------------------------------------


class DisLikeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = DisLikeSerializer
    queryset = DisLike.objects.order_by('created_at')

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.Like_count = obj.dislike_count + 1
        obj.save(update_fields=("dislike_count",))
        return super().retrieve(request, *args, **kwargs)


# _________________________ Latest Price _________________________

class LatestPriceViewSet(viewsets.GenericViewSet):

    @action(methods=['GET'], detail=False, url_name='price',
            url_path='(?P<symbol>[^/.]+)/(?P<type>[^/.]+)')
    def get_last_price(self, request, **kwargs):
        symbol = kwargs.get('symbol')
        time_frame = kwargs.get('type')
        # limit = kwargs.get('limit')
        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/all_data/all_data?symbol={symbol}&time_frame={time_frame}'
            f'&limit={100}')

        crypto_data = data.json()
        latest_price = crypto_data[list(crypto_data.keys())[2]]['latest_price']

        return JsonResponse(data={'latest_price': latest_price})
