from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    use_form = models.DateTimeField()
    use_to = models.DateTimeField()
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])  # 제약조건 값 0~100000
    active = models.BooleanField()

    def __str__(self):
        return self.code