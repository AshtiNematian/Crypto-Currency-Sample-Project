from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets, mixins
from membership.models import UserMembership
from rest_framework.response import Response
from membership.models import Membership
from membership.serializers import MemberShipSerializer, UserMemberShipSerializer


class MemberShipViewList(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Membership.objects.all()
    serializer_class = MemberShipSerializer


class MemberShipDetail(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Membership.objects.all()
    serializer_class = MemberShipSerializer

    def get(self, request, **kwargs):
        return Membership.objects.get(id=request.data['id'])


class MembershipView(viewsets.ViewSet):
    model = UserMembership
    serializer_class = MemberShipSerializer

    def list(self, request):
        try:
            user = self.request.user
            queryset = UserMembership.objects.get(user=user)
            serializer = MemberShipSerializer(queryset)
            active = serializer.data
            return Response(active)
        except ObjectDoesNotExist:
            return HttpResponse('You dont have any membership')


class CreateUserMembershipApiView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = UserMembership
    serializer_class = UserMemberShipSerializer

    def get_queryset(self, **kwargs):
        user = self.request.user
        membership = kwargs.pop('membership', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, user=user, membership=membership)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        serializer.save()
