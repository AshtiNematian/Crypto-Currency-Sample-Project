from market.serializer import AssetsSerializer
from paper_trading.models import PaperTrading, PropertyPaperTrading

from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class PropertyPaperTradingSerializer(serializers.ModelSerializer):
    side = ChoiceField(choices=PropertyPaperTrading.SIDE_CHOICES)
    status = ChoiceField(choices=PropertyPaperTrading.STATUS)

    class Meta:
        model = PropertyPaperTrading
        fields = ['id', 'side', 'status', 'average_price', 'quantity', 'created_at', 'closed_at', 'register',
                  'paper_trading_id']
        read_only_fields = ("id", "side")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['assets'] = AssetsSerializer(instance.assets).data
        return rep


class PaperTradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTrading
        fields = '__all__'
