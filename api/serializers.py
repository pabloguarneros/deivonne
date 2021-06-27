from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from contracts.models import SmartContract
from conseil import conseil

class ContractSerializer(serializers.ModelSerializer):

    contract_data = serializers.SerializerMethodField('is_count')

    def is_count(self, foo):

        Operation = conseil.tezos.alphanet.operations

        query = Operation.query(Operation.block_level, Operation.operation_group_hash.count()) \
        .filter(Operation.timestamp.between(1554076800000, 1556668799000),
                Operation.kind.in_(Operation.kind.transaction,
                                   Operation.kind.origination,
                                   Operation.kind.delegation,
                                   Operation.kind.activation,
                                   Operation.kind.reveal)) \
        .order_by(Operation.operation_group_hash.count().desc()) \
        .limit(100)
    
        return query[0](output='csv')

    class Meta:
        model = SmartContract
        fields = ('title','pk','short_description','contract_data')