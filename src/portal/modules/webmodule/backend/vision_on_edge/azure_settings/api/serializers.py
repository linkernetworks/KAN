# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""App API serializers.
"""

import logging

from rest_framework import serializers

from ..models import Setting

logger = logging.getLogger(__name__)


class SettingSerializer(serializers.ModelSerializer):
    """SettingSerializer."""

    class Meta:
        model = Setting
        fields = "__all__"

    def create(self, validated_data):
        """create.

        Args:
            validated_data:
        """

        obj, _ = Setting.objects.get_or_create(
            endpoint=validated_data["endpoint"],
            training_key=validated_data["training_key"],
            defaults={
                "name": validated_data["name"],
                "iot_hub_connection_string": validated_data[
                    "iot_hub_connection_string"
                ],
                "device_id": validated_data["device_id"],
                "module_id": validated_data["module_id"],
                "is_collect_data": validated_data["is_collect_data"],
                "subscription_id": validated_data["subscription_id"],
                "storage_account": validated_data["storage_account"],
                "storage_container": validated_data["storage_container"],
                "tenant_id": validated_data["tenant_id"],
                "client_id": validated_data["client_id"],
                "client_secret": validated_data["client_secret"],
            },
        )
        return obj


class ListProjectProjectSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    exportable = serializers.BooleanField()


class ListProjectSerializer(serializers.Serializer):
    projects = ListProjectProjectSerializer(many=True)
