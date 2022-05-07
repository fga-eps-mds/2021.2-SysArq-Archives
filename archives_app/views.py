from rest_framework import viewsets, views
from rest_framework.response import Response
from .fields_serializers import BoxAbbreviationsSerializer
from .fields_serializers import (DocumentNameSerializer,
                                 UnitySerializer, RackSerializer, PublicWorkerSerializer, LocationSerializer)
from .fields_serializers import FrontCoverSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, DocumentName
from .fields_models import Unity, Shelf, FrontCover, Rack, PublicWorker, FileLocation
from .documents_models import (BoxArchiving, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet, OriginBoxSubject)
from .documents_serializers import (FrequencySheetSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    BoxArchivingSerializer,
                                    OriginBoxSubjectSerializer)
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

        if BoxArchiving.objects.filter(process_number=request.data['process_number']).exists():
            return Response(status=400)

        for box_n in origin_boxes:
            box = OriginBox.objects.create(
                number=box_n['number'],
                year=box_n['year'],
                box_notes=box_n['box_notes'])

            if box_n['shelf_id'] != '':
                shelf_number_id = Shelf.objects.get(pk=box_n['shelf_id'])
                box.shelf_id = shelf_number_id

            if box_n['rack_id'] != '':
                rack_number_id = Rack.objects.get(pk=box_n['rack_id'])
                box.rack_id = rack_number_id

            if box_n['file_location_id'] != '':
                file_location_id = FileLocation.objects.get(pk=box_n['file_location_id'])
                box.file_location_id = file_location_id

            for subject in box_n['subjects_list']:
                if subject['document_name_id'] != '':
                    document_name_id = DocumentName.objects.get(pk=subject['document_name_id'])
                    sub = OriginBoxSubject.objects.create(document_name_id=document_name_id,
                                                          year=subject['year'],
                                                          month=subject['month'])
                    box.subject.add(sub.id)

            box.save()
            boxes.append(box)

        sender_unity_id = Unity.objects.get(pk=request.data['sender_unity'])


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
                    box_dict['rack_id'] = box_n.rack_id.id
                    box_dict['shelf_id'] = box_n.shelf_id.id
                    box_dict['file_location_id'] = box_n.file_location_id.id

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


class ReportView(views.APIView):
    def get(self, request):
        document_name_id = request.query_params.get("document_name_id")
        initial_date = request.query_params.get("initial_date")
        final_date = request.query_params.get("final_date")
        only_permanents = request.query_params.get("only_permanents")

        frequency_sheet_filter = {}
        administrative_process_filter = {}
        frequecy_relation_filter = {}
        box_archiving_filter = {}

        if document_name_id:
            frequency_sheet_filter["document_name_id"] = document_name_id
            administrative_process_filter["document_name_id"] = document_name_id
            frequecy_relation_filter["document_name_id"] = document_name_id
            box_archiving_filter["document_name_id"] = document_name_id

        if initial_date:
            frequency_sheet_filter["reference_period__gte"] = initial_date
            administrative_process_filter["archiving_date__gte"] = initial_date
            frequecy_relation_filter["received_date__gte"] = initial_date
            box_archiving_filter["originbox__boxarchiving__received_date__gte"] = initial_date

        if final_date:
            frequency_sheet_filter["reference_period__lte"] = final_date
            administrative_process_filter["archiving_date__lte"] = final_date
            frequecy_relation_filter["received_date__lte"] = final_date
            box_archiving_filter["originbox__boxarchiving__received_date__lte"] = final_date

        if only_permanents and only_permanents == "true":
            frequency_sheet_filter["document_name_id__isPerma"] = True
            administrative_process_filter["document_name_id__isPerma"] = True
            frequecy_relation_filter["document_name_id__isPerma"] = True
            box_archiving_filter["document_name_id__isPerma"] = True

        frequency_sheet = FrequencySheet.objects.filter(**frequency_sheet_filter)
        administrative_process = AdministrativeProcess.objects.filter(**administrative_process_filter)
        frequency_relation = FrequencyRelation.objects.filter(**frequecy_relation_filter)
        box_archiving = OriginBoxSubject.objects.filter(**box_archiving_filter)

        response = FrequencySheetSerializer(
            frequency_sheet,
            many=True).data

        response += AdministrativeProcessSerializer(
            administrative_process,
            many=True).data

        response += FrequencyRelationSerializer(
            frequency_relation,
            many=True).data

        response += OriginBoxSubjectSerializer(
            box_archiving,
            many=True).data

        return Response(response, status=200)


class AdministrativeProcessReport(views.APIView):
    def get(self, request):
        sender_unity = request.query_params.get("sender_unity")
        initial_date = request.query_params.get("initial_date")
        final_date = request.query_params.get("final_date")

        filter_dict = {}
        if sender_unity:
            filter_dict["sender_unity"] = sender_unity

        if initial_date:
            filter_dict["archiving_date__gte"] = initial_date

        if final_date:
            filter_dict["archiving_date__lte"] = final_date
        response = AdministrativeProcessSerializer(
            AdministrativeProcess.objects.filter(**filter_dict),
            many=True)

        return Response(response.data, status=200)


class FrequencySheetReport(views.APIView):
    def get(self, request):
        cpf = request.query_params.get("public_worker")

        filter_dict = {}

        if cpf:
            filter_dict["cpf"] = cpf
        response = FrequencySheetSerializer(
            FrequencySheet.objects.filter(**filter_dict),
            many=True)

        return Response(response.data, status=200)


class FrequencyRelationReport(views.APIView):
    def get(self, request):
        sender_unity = request.query_params.get("sender_unity")
        reference_period = request.query_params.get("reference_period")

        filter_dict = {}
        if sender_unity:
            filter_dict["sender_unity"] = sender_unity
        if reference_period:
            reference_period = reference_period.split(",")
            filter_dict["reference_period__overlap"] = reference_period

        response = FrequencyRelationSerializer(
            FrequencyRelation.objects.filter(**filter_dict),
            many=True)

        return Response(response.data, status=200)


class BoxArchivingReport(views.APIView):
    def get(self, request):
        sender_unity = request.query_params.get("sender_unity")

        filter_dict = {}
        if sender_unity:
            filter_dict["originbox__boxarchiving__sender_unity"] = sender_unity

        response = OriginBoxSubjectSerializer(
            OriginBoxSubject.objects.filter(**filter_dict),
            many=True)

        return Response(response.data, status=200)


class StatusReport(views.APIView):
    def get(self, request):
        status = request.query_params.get("status")

        filter_dict = {}

        if status == "arquivado":
            filter_dict["is_filed"] = True
        elif status == "desarquivado":
            filter_dict["is_filed"] = False
        elif status == "eliminado":
            filter_dict["is_eliminated"] = True
        else:
            pass

        response = AdministrativeProcessSerializer(
            AdministrativeProcess.objects.filter(**filter_dict),
            many=True).data

        response += BoxArchivingSerializer(
            BoxArchiving.objects.filter(**filter_dict),
            many=True).data

        return Response(response, status=200)
