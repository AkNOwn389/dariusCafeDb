from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class ClassicCafeFeedbackModel(models.Model):
      
      class status_choice(models.TextChoices):
            good = 'G', _('good')
            very_good = 'Vg', _('very-good')
            bad = 'B', _('Bad')
            very_bad = 'Vb', _('very-bad')
            
      name = models.CharField(max_length=255, null=False, blank=False, default="unknown")
      feedback = models.TextField(max_length=1000, null=True, blank=True)
      rate = models.CharField(choices=status_choice.choices, default=status_choice.good, max_length = 2)
      
      def __str__(self) -> str:
            return str(self.name)