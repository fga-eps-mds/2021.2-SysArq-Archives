from rest_framework import serializers
from archives_app.documents_models import (FrequencyRelation, BoxArchiving,
                                           AdministrativeProcess, OriginBox,
                                           FrequencySheet, DocumentNames)


class FrequencySupport(serializers.ModelSerializer):
    def get_document_name(self, obj):
        if obj.document_name_id is not None:
            return obj.document_name_id.document_name
        return None


class BoxArchivingSerializer(serializers.ModelSerializer):

    def get_shelf_number(self, obj):
        if obj.shelf_id is not None:
            return obj.shelf_id.number
        return None

    def get_rack_number(self, obj):
        if obj.rack_id is not None:
            return obj.rack_id.number
        return None

    def get_abbreviation_name(self, obj):
        if obj.abbreviation_id is not None:
            return obj.abbreviation_id.name
        return ""

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    def get_doc_names(self, obj):
        if obj.document_names is not None:
            doc_names = []
            for obj in obj.document_names.all():
                doc_names.append(obj.document_name_id.document_name)
            return doc_names
        return ""

    def get_temporalities(self, obj):
        if obj.document_names is not None:
            doc_names = []
            for obj in obj.document_names.all():
                doc_names.append(obj.temporality_date)
            return doc_names
        return None

    shelf_number = serializers.SerializerMethodField('get_shelf_number')
    rack_number = serializers.SerializerMethodField('get_rack_number')
    abbreviation_name = serializers.SerializerMethodField('get_abbreviation_name')
    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')
    document_name_name = serializers.SerializerMethodField('get_doc_names')
    temporality_date = serializers.SerializerMethodField('get_temporalities')

    class Meta:
        model = BoxArchiving
        fields = (
            "id",
            "process_number",
            "sender_unity",
            "notes",
            "received_date",
            "document_url",
            "cover_sheet",
            "filer_user",
            "is_filed",
            "is_eliminated",
            "send_date",
            "box_process_number",
            "unity_id",
            "abbreviation_name",
            "shelf_number",
            "rack_number",
            "origin_box_id",
            "abbreviation_id",
            "shelf_id",
            "rack_id",
            "document_names",
            "sender_unity_name",
            "document_name_name",
            "temporality_date"
        )


class FrequencyRelationSerializer(FrequencySupport):

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    def get_sender_name(self, obj):
        if obj.sender_id is not None:
            return obj.sender_id.name
        return ""

    def get_receiver_name(self, obj):
        if obj.receiver_id is not None:
            return obj.receiver_id.name
        return ""

    document_name_name = serializers.SerializerMethodField(
        'get_document_name'
    )
    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')
    sender_name = serializers.SerializerMethodField('get_sender_name')
    receiver_name = serializers.SerializerMethodField('get_receiver_name')

    class Meta:
        model = FrequencyRelation
        fields = (
            "id",
            "sender_id",
            "sender_cpf",
            "sender_name",
            "receiver_id",
            "receiver_cpf",
            "receiver_name",
            "process_number",
            "notes",
            "received_date",
            "temporality_date",
            "reference_period",
            "filer_user",
            "sender_unity",
            "document_name_id",
            "document_name_name",
            "sender_unity_name"
        )


class AdministrativeProcessSerializer(serializers.ModelSerializer):

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    def get_sender_user(self, obj):
        if obj.sender_user is not None:
            return obj.sender_user.name
        return ""

    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')
    sender_user_name = serializers.SerializerMethodField('get_sender_user')

    class Meta:
        model = AdministrativeProcess
        fields = ("id",
                  "process_number",
                  "notes",
                  "filer_user",
                  "notice_date",
                  "interested",
                  "reference_month_year",
                  "sender_user",
                  "sender_user_name",
                  "archiving_date",
                  "is_filed",
                  "is_eliminated",
                  "temporality_date",
                  "send_date",
                  "administrative_process_number",
                  "sender_unity",
                  #   "subject_id",
                  "document_name_id",
                  "administrative_unity_id",
                  #   "document_subject_name",
                  "sender_unity_name"
                  )


class OriginBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginBox
        fields = '__all__'


class DocumentNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentNames
        fields = '__all__'


class FrequencySheetSerializer(FrequencySupport):

    def get_person_name(self, obj):
        if obj.person_id is not None:
            return obj.person_id.name
        return ""

    def get_workplace(self, obj):
        if obj.workplace is not None:
            return obj.workplace.unity_name
        return ""

    document_name_name = serializers.SerializerMethodField(
        'get_document_name'
    )
    person_name = serializers.SerializerMethodField('get_person_name')
    workplace_name = serializers.SerializerMethodField('get_workplace')

    class Meta:
        model = FrequencySheet
        fields = ("id",
                  "person_id",
                  "person_name",
                  "cpf",
                  "role",
                  "category",
                  "workplace",
                  "workplace_name",
                  "municipal_area",
                  "reference_period",
                  "notes",
                  "process_number",
                  "document_name_id",
                  "temporality_date",
                  "document_name_name"
                  )
