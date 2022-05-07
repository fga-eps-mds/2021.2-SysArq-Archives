from rest_framework import serializers
from .fields_models import BoxAbbreviations, FrontCover
from .fields_models import DocumentName, Shelf, Unity, Rack, PublicWorker, FileLocation


class DocumentNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentName
        fields = '__all__'


class UnitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Unity
        fields = '__all__'


class BoxAbbreviationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoxAbbreviations
        fields = '__all__'


class ShelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shelf
        fields = '__all__'


class RackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rack
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileLocation
        fields = '__all__'


class FrontCoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrontCover
        fields = '__all__'


class PublicWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicWorker
        fields = '__all__'
