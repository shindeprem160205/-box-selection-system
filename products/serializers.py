from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "length",
            "width",
            "height",
            "weight",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, data):
        dimensions = ["length", "width", "height", "weight"]

        for field in dimensions:
            if data[field] <= 0:
                raise serializers.ValidationError(
                    {field: f"{field} must be greater than zero."}
                )

        return data