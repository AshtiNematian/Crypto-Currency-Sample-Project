from django.db import models
from accounts.models import User


class Assets(models.Model):
    image = models.ImageField(default='image', upload_to='media')
    name = models.CharField(max_length=50, unique=True, blank=False, null=True)
    core_key = models.CharField(max_length=10, blank=False, null=False, default='usdt')
    price = models.FloatField( blank=False, null=True)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    currency = models.CharField(max_length=25, blank=False, null=False)
    assets = models.ManyToManyField(Assets, related_name='market_assets')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True, default='portfolio')
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='investor')
    assets = models.ManyToManyField(Assets, related_name='portfolio_assets')

    def user_id(self):
        return self.user.pk

    def __str__(self):
        return self.name


class Comment(models.Model):
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='user')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on',)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def __str__(self):
        return f'Comment {self.body} by {self.author}'


class Like(models.Model):
    """ like  comment """

    comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.comment.asset)[:30]

    def get_total_likes(self, instance):
        return Like.like_count


class DisLike(models.Model):
    """ Dislike  comment """

    comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.comment.asset)[:30]
