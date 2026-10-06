from rest_framework import serializers

from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            "id",
            "name",
            "internal_length",
            "internal_width",
            "internal_height",
            "max_weight",
            "cost",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, data):
        dimensions = [
            "internal_length",
            "internal_width",
            "internal_height",
            "max_weight",
            "cost",
        ]

        for field in dimensions:
            if data[field] <= 0:
                raise serializers.ValidationError(
                    {field: f"{field} must be greater than zero."}
                )

        return data