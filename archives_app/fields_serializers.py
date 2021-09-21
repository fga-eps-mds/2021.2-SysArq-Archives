from rest_framework import serializers
from .fields_models import BoxAbbreviations, FrontCover, DocumentSubject
from .fields_models import DocumentType, Shelf, Status, Unity


class DocumentSubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = DocumentSubject
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
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


class FrontCoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrontCover
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'
