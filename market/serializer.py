from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from market.models import Portfolio, Assets, Comment, Like, DisLike, Market


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'name', 'currency', 'assets']


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['id', 'name', 'price', 'image']


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['user_id', 'id', 'name', 'user', 'assets']


class PortfolioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name']


class PortfolioAssetsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'assets']


class CommentSerializer(serializers.ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        ordering = ('-created_at',)
        model = Comment
        fields = ('id', 'author', 'reply_count', 'asset', 'body')

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'comment', 'like_count')


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = ('id', 'comment', 'dislike_count')
