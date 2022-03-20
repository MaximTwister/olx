from rest_framework import serializers

from olx.models import (
    Advertisement,
    Account,
    AdvCategory,
    AdvSubCategory
)


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="title")

    class Meta:
        model = AdvCategory
        fields = ("category",)

    def validate(self, data):
        print(f"### Category DATA before validation: {data}")
        validated_data = super().validate(data)
        print(f"### Category DATA after validation: {data}")
        cat = validated_data.get("title")
        try:
            AdvCategory.objects.get(title=cat)
        except AdvCategory.DoesNotExist:
            print(f"Category:{cat} DoesNotExist")
        else:
            raise serializers.ValidationError(
                {"error": f"Category:{cat} already exists"}
            )
        return validated_data
