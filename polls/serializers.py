from rest_framework import serializers
from polls.models import DjangoDemo

class DjangoDemoSerializer(serializers.ModelSerializer):
  class Meta:
    model = DjangoDemo
    fields = [ 'a_asset_id', 'ad_client_id', 'ad_org_id', 'isactive' ]
