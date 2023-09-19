
from .models import ClassicCafeFeedbackModel
from rest_framework import serializers

class UserFeedbackSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = ClassicCafeFeedbackModel
            fields = ['name', 'feedback', 'rate']
      def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep['rate'] = instance.get_rate_display()
            return rep