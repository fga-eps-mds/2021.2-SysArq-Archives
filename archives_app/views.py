from rest_framework import viewsets, views
from rest_framework.response import Response
from .fields_serializers import BoxAbbreviationsSerializer
from .fields_serializers import (DocumentNameSerializer,
                                 UnitySerializer, RackSerializer, PublicWorkerSerializer, LocationSerializer)
from .fields_serializers import FrontCoverSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, DocumentName
from .fields_models import Unity, Shelf, FrontCover, Rack, PublicWorker, FileLocation
from .documents_models import (BoxArchiving, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet, OriginBoxSubject, DocumentNames, Document)
from .documents_serializers import (FrequencySheetSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    BoxArchivingSerializer)
import json


class DocumentNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows document types to be viewed or edited.
    """
    queryset = DocumentName.objects.all()
    serializer_class = DocumentNameSerializer


class UnityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows unitys to be viewed or edited.
    """
    queryset = Unity.objects.all()
    serializer_class = UnitySerializer


class PublicWorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public workers to be viewed or edited.
    """
    queryset = PublicWorker.objects.all()
    serializer_class = PublicWorkerSerializer


class BoxAbbreviationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abbreviations to be viewed or edited.
    """
    queryset = BoxAbbreviations.objects.all()
    serializer_class = BoxAbbreviationsSerializer


class ShelfViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shelfs to be viewed or edited.
    """
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class RackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows racks to be viewed or edited.
    """
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents location to be viewed or edited.
    """
    queryset = FileLocation.objects.all()
    serializer_class = LocationSerializer


class FrontCoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer


class FrequencyRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency relations document type
    to be viewed or edited.
    """
    queryset = FrequencyRelation.objects.all()
    serializer_class = FrequencyRelationSerializer


class AdministrativeProcessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows administrative process document type
    to be viewed or edited.
    """
    queryset = AdministrativeProcess.objects.all()
    serializer_class = AdministrativeProcessSerializer


class FrequencySheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency sheet document type
    to be viewed or edited.
    """
    queryset = FrequencySheet.objects.all()
    serializer_class = FrequencySheetSerializer


class BoxArchivingView(views.APIView):

    def get(self, request):
        queryset = BoxArchiving.objects.all()
        serializer = BoxArchivingSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        origin_boxes = request.data['origin_boxes']
        boxes = list()

        for box_n in origin_boxes:
            box = OriginBox.objects.create(
                number=box_n['number'],
                year=box_n['year'],
                box_notes=box_n['box_notes'])

            if box_n['shelf_id'] != '':
                shelf_number_id = Shelf.objects.get(pk=box_n['shelf_id'])
                box_archiving.shelf_id = shelf_number_id

            if box_n['rack_id'] != '':
                rack_number_id = Rack.objects.get(pk=box_n['rack_id'])
                box_archiving.rack_id = rack_number_id

            if box_n['file_location_id'] != '':
                file_location_id = FileLocation.objects.get(pk=box_n['file_location_id'])
                box_archiving.file_location_id = file_location_id

            for subject in box_n['subjects_list']:
                if subject['document_name_id'] != '':
                    document_name_id = DocumentName.objects.get(pk=subject['document_name_id'])
                    sub = OriginBoxSubject.objects.create(document_name_id=document_name_id,
                                                          year=subject['year'],
                                                          month=subject['month'])
                    box.subject.add(sub.id)

            boxes.append(box)

        sender_unity_id = Unity.objects.get(pk=request.data['sender_unity'])

        if BoxArchiving.objects.filter(process_number=request.data['process_number']).exists():
            return Response(status=400)

        box_archiving = BoxArchiving.objects.create(
            process_number=request.data['process_number'],
            sender_unity=sender_unity_id,
            notes=request.data['notes'],
            received_date=request.data['received_date'],
            document_url=request.data['document_url'],
            cover_sheet=request.data['cover_sheet'],
            filer_user=request.data['filer_user'],
            is_filed=request.data['is_filed'],
            is_eliminated=request.data['is_eliminated'],
            send_date=request.data['send_date'],
            box_process_number=request.data['box_process_number'],
        )

        for box in boxes:
            box_archiving.origin_boxes.add(box.id)

        if request.data['unity_id'] != '':
            unityId = Unity.objects.get(pk=request.data['unity_id'])
            box_archiving.unity_id = unityId
            box_archiving.save()

        return Response(status=201)


class BoxArchivingDetailsView(views.APIView):

    def delete(self, request, pk):
        try:
            obj = BoxArchiving.objects.get(pk=pk)
            obj.delete()
            return Response(status=204)
        except BoxArchiving.DoesNotExist:
            error_dict = {"detail": "Not found."}
            return Response(error_dict, status=404)

    def get(self, request, pk):
        try:
            queryset = BoxArchiving.objects.get(pk=pk)
            serializer = BoxArchivingSerializer(queryset)

            box_list = serializer.data['origin_boxes']
            boxes = list()
            for box in box_list:
                box_dict = {}
                if box is not None:
                    box_n = OriginBox.objects.get(pk=box)

                    box_dict['number'] = box_n.number
                    box_dict['year'] = box_n.year
                    box_dict['box_notes'] = box_n.box_notes
                    box_dict['rack_id'] = box_n.rack_id
                    box_dict['shelf_id'] = box_n.shelf_id
                    box_dict['file_location_id'] = box_n.file_location_id

                    box_dict['subject_list'] = list()
                    for subject in box_n.subject.all():
                        document_name = DocumentNameSerializer(subject.document_name_id)
                        document_name = document_name.data
                        box_dict['subject_list'].append({
                            'document_name_id': document_name['id'],
                            'document_name': document_name['document_name'],
                            'year': subject.year,
                            'month': subject.month
                        })
                    boxes.append(box_dict)

            final_dict = serializer.data
            final_dict['origin_boxes'] = boxes
            return Response(final_dict, status=200)

        except BoxArchiving.DoesNotExist:
            error_dict = {"detail": "Not found."}
            return Response(error_dict, status=404)


class SearchView(views.APIView):
    box_archiving_fields = [field.name for field in
                            BoxArchiving._meta.get_fields()]
    frequency_relation_fields = [field.name for field in
                                 FrequencyRelation._meta.get_fields()]
    frequency_sheet_fields = [field.name for field in
                              FrequencySheet._meta.get_fields()]
    administrative_process_fields = [field.name for field in
                                     AdministrativeProcess._meta.get_fields()]

    def get(self, request):
        query = request.query_params.get("filter")
        box_archiving = BoxArchiving.objects.all()
        frequency_sheet = FrequencySheet.objects.all()
        administrative_process = AdministrativeProcess.objects.all()
        frequency_relation = FrequencyRelation.objects.all()
        return_dict = {
            "box_archiving": [],
            "frequecy_relation": [],
            "frequency_sheet": [],
            "administrative_process": []
        }

        if query:
            filter_dict = json.loads(query)
            filter_dict_fk = {}

            if (
                'id' in list(filter_dict.keys())[0] or 'sender_unity' in list(
                    filter_dict.keys())[0] or 'sender_user' in list(filter_dict.keys())[0]
            ):
                if 'abbreviation_id' in list(filter_dict.keys())[0]:
                    contains = 'abbreviation_id__name__icontains'
                elif 'document_name_id' in list(filter_dict.keys())[0]:
                    contains = '{}__document_name__icontains'.format(
                        list(filter_dict.keys())[0])
                elif 'sender_unity' in list(filter_dict.keys())[0]:
                    contains = '{}__unity_name__icontains'.format(
                        list(filter_dict.keys())[0])
                elif (
                    'person_id' in list(filter_dict.keys())[0] or 'sender_user' in list(filter_dict.keys())[0]
                ):
                    contains = '{}__name__icontains'.format(
                        list(filter_dict.keys())[0])
                else:
                    contains = '{}__number__icontains'.format(
                        list(filter_dict.keys())[0])
                filter_dict_fk = {
                    contains: list(filter_dict.values())[0]
                }

            if list(filter_dict.keys())[0] in self.box_archiving_fields:
                if not filter_dict_fk:
                    box_archiving = box_archiving.filter(**filter_dict)
                else:
                    box_archiving = box_archiving.filter(**filter_dict_fk)
                return_dict['box_archiving'] = BoxArchivingSerializer(
                    box_archiving, many=True).data

            if 'document_name_id' in list(filter_dict.keys())[0]:
                boxes = []
                for box in box_archiving:
                    doc_names = box.document_names.filter(**filter_dict_fk)
                    if box not in boxes and doc_names:
                        boxes.append(box)
                return_dict['box_archiving'] = BoxArchivingSerializer(
                    boxes, many=True).data

            if 'temporality_date' in list(filter_dict.keys())[0]:
                boxes = []
                for box in box_archiving:
                    doc_names = box.document_names.filter(**filter_dict)
                    if box not in boxes and doc_names:
                        boxes.append(box)
                return_dict['box_archiving'] = BoxArchivingSerializer(
                    boxes, many=True).data

            if list(filter_dict.keys())[0] in self.frequency_relation_fields:
                if not filter_dict_fk:
                    frequency_relation = frequency_relation.filter(**filter_dict)
                else:
                    frequency_relation = frequency_relation.filter(**filter_dict_fk)
                return_dict['frequecy_relation'] = FrequencyRelationSerializer(
                    frequency_relation,
                    many=True).data

            if list(filter_dict.keys())[0] in self.frequency_sheet_fields:
                if not filter_dict_fk:
                    frequency_sheet = frequency_sheet.filter(**filter_dict)
                else:
                    frequency_sheet = frequency_sheet.filter(**filter_dict_fk)
                return_dict['frequency_sheet'] = FrequencySheetSerializer(
                    frequency_sheet,
                    many=True).data

            if list(filter_dict.keys())[0] in self.administrative_process_fields:
                if not filter_dict_fk:
                    administrative_process = administrative_process.filter(**filter_dict)
                else:
                    administrative_process = administrative_process.filter(**filter_dict_fk)
                return_dict['administrative_process'] = AdministrativeProcessSerializer(
                    administrative_process,
                    many=True).data

        return Response(return_dict, status=200)


class YearByAbbreviation(views.APIView):
    def get(self, request, abvt):
        queryset = BoxAbbreviations.objects.filter(
            abbreviation=abvt)
        if not queryset:
            return Response('Nao foi encontrado objeto com este valor', status=204)
        serializer = BoxAbbreviationsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class NumberByYearAndAbbreviation(views.APIView):
    def get(self, request, abvt, year):
        queryset = BoxAbbreviations.objects.filter(
            abbreviation=abvt, year=year)
        if not queryset:
            return Response('Nao foi encontrado objeto com este valor', status=204)
        serializer = BoxAbbreviationsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
