from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=1000, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    subcategory = models.ForeignKey(
        "AdvSubCategory",
        null=True,
        on_delete=models.SET_NULL,
        related_name="advertisements"
    )
    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        related_name="advertisements",
    )


class AdvCategory(models.Model):
    title = models.CharField(max_length=120)


class AdvSubCategory(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        "AdvCategory",
        on_delete=models.CASCADE,
        related_name="subcategories",
    )


class Account(models.Model):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nickname} : {self.pk}"
