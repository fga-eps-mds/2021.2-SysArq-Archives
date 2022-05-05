import pytest
from rest_framework.test import APIClient
from django.test import override_settings
from django.conf import settings

TESTS_MIDDLEWARE = [mc for mc in settings.MIDDLEWARE
                    if mc != 'archives_app.middleware.IsTokenValidMiddleware']


@pytest.mark.django_db(transaction=False)
class TestBoxAbreviationsEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }

        api_client = APIClient()
        response = api_client.post(
            '/box-abbreviation/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/box-abbreviation/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/box-abbreviation/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }
        data4 = {
            "number": 9,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/box-abbreviation/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
class TestDocumentNameEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "subject_name": "",
            "temporality": "",
            "isPerma": "",
        }

        api_client = APIClient()
        response = api_client.post(
            '/document-name/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document-name/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "subject_name": "1",
            "temporality": "",
            "isPerma": "",
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document-name/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/document-name/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "subject_name": "2",
            "temporality": "",
            "isPerma": "true"
        }
        data4 = {
            "subject_name": "3",
            "temporality": "",
            "isPerma": "false",
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/document-name/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/document-name/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "subject_name": "4",
            "temporality": "",
            "isPerma": "false"
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document-name/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/document-name/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestUnityEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "name_of_unity": "1",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/unity/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/unity/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "name_of_unity": "2",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/unity/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "name_of_unity": "3",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }
        data4 = {
            "name_of_unity": "4",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/unity/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "name_of_unity": "5",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/unity/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestshelfEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "number": 0,
        }

        api_client = APIClient()
        response = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/shelf/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data = {
            "number": 0,
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/shelf/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data = {
            "number": 0,
        }
        data_2 = {
            "number": 0,
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/shelf/3/', data=data_2,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data = {
            "number": 0,
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/shelf/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_box_archiving_relation_get():
    api_client = APIClient()
    response = api_client.get('/box-archiving/')
    assert response.status_code == 200


@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def box_archiving():
    api_client = APIClient()

    data_sender = {
        "telephone_number": "",
        "note": "",
        "unity_name": "",
        "unity_abbreviation": "",
        "administrative_bond": "",
        "bond_abbreviation": "",
        "type_of_unity": "",
        "municipality": ""
    }

    response_sender = api_client.post(
        '/unity/', data=data_sender,
        header={"Content-Type": "application/json"})

    assert response_sender.status_code == 201

    data_name = {
        "document_name": "teste",
        "temporality": "1"
    }

    response_name = api_client.post(
        '/document-name/', data=data_name,
        header={"Content-name": "application/json"})
    assert response_name.status_code == 201

    data_shelf = {
        "number": 555,
    }

    response_shelf = api_client.post(
        '/shelf/', data=data_shelf,
        header={"Content-Type": "application/json"})
    assert response_shelf.status_code == 201

    data_rack = {
        "number": 555,
    }

    response_rack = api_client.post(
        '/rack/', data=data_rack,
        header={"Content-Type": "application/json"})
    assert response_rack.status_code == 201

    data_file_location = {
        "file": "local",
    }

    response_file_location = api_client.post(
        '/file-location/', data=data_file_location,
        header={"Content-Type": "application/json"})

    assert response_file_location.status_code == 201


    data = {
        "origin_boxes": [
            {
                "number": "1",
                "year": 2020,
                "rack_id": response_rack.data['id'],
                "shelf_id": response_shelf.data['id'],
                "file_location_id": response_file_location.data['id'],
                "box_notes": "",
                "subjects_list": [
                    {
                        "document_name_id": response_name.data['id'],
                        "year": ["2020"],
                        "month": ["11"],
                    }
                ]
            },
        ],
        "process_number": "1",
        "sender_unity": response_sender.data['id'],
        "notes": "1",
        "received_date": "2020-11-11",
        "document_url": "https://www.t.com/",
        "cover_sheet": "1",
        "filer_user": "1",
        "is_filed": "",
        "is_eliminated": "",
        "send_date": "2020-11-11",
        "box_process_number": "1",
        "unity_id": response_sender.data['id']
    }

    return data


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_box_archiving_relation_get_pk():
    api_client = APIClient()

    data = box_archiving()

    data['process_number'] = "2"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response_box_archiving_get = api_client.get(
        '/box-archiving/')
    assert response_box_archiving_get.status_code == 200

    response = api_client.get('/box-archiving/{}'.format(
        response_box_archiving_get.data[0]['id']))
    assert response.status_code == 200

    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 400


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_box_archiving_relation_get_pk_except():
    api_client = APIClient()

    response = api_client.get('/box-archiving/4000')
    assert response.status_code == 404


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_box_archiving_relation_post():
    api_client = APIClient()

    data = box_archiving()

    data['process_number'] = "3"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

# Testes do relatório
@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/report/?document_name_id=1&initial_date=2022-10-04&final_date=2022-11-04&only_permanents=true')

    assert response_report_get.status_code == 200

@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_status_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/status-report/?status=desarquivado')

    assert response_report_get.status_code == 200

    response_report_get = api_client.get(
        '/status-report/?status=eliminado')

    assert response_report_get.status_code == 200

    response_report_get = api_client.get(
        '/status-report/?status=arquivado')

    assert response_report_get.status_code == 200

@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_administrative_process_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/administrative-process-report/?sender_unity=1&initial_date=2000-05-10&final_date=2022-05-04')

    assert response_report_get.status_code == 200

@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_frequency_sheet_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/frequency-sheet-report/?cpf=12345678910')

    assert response_report_get.status_code == 200

@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_frequency_relation_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/frequency-relation-report/?sender_unity=1&reference_period=05-2022')

    assert response_report_get.status_code == 200

@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_box_archiving_report_get():
    api_client = APIClient()

    response_report_get = api_client.get(
        '/box-archiving-report/?sender_unity=1')

    assert response_report_get.status_code == 200
@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_delete_box_archiving_relation():
    api_client = APIClient()

    data = box_archiving()

    data['process_number'] = "3"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response_box_archiving_get = api_client.get(
        '/box-archiving/')
    assert response_box_archiving_get.status_code == 200

    response = api_client.delete('/box-archiving/{}'.format(
        response_box_archiving_get.data[0]['id']))
    assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_delete_box_archiving_relation_except():
    api_client = APIClient()

    response = api_client.delete('/box-archiving/10000000000')
    assert response.status_code == 404


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search():
    api_client = APIClient()

    data = box_archiving()

    data['process_number'] = "4"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response = api_client.get('/search/?filter={"process_number":"1"}')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search_without_specific_fields_from_box_archiving():

    api_client = APIClient()

    data = box_archiving()

    data_shelf = {
        "number": 123,
    }

    response_shelf = api_client.post(
        '/shelf/', data=data_shelf,
        header={"Content-Type": "application/json"})
    assert response_shelf.status_code == 201

    data['shelf_id'] = response_shelf.data['id']

    data["process_number"] = "5"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response = api_client.get('/search/?filter={"shelf_id":123}')
    assert response.status_code == 200

    data_rack = {
        "number": 123,
    }

    response_rack = api_client.post(
        '/rack/', data=data_rack,
        header={"Content-Type": "application/json"})
    assert response_rack.status_code == 201

    data['rack_id'] = response_rack.data['id']

    data["process_number"] = "6"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response = api_client.get('/search/?filter={"rack_id":123}')
    assert response.status_code == 200

    data_abbreviation = {
        "number": "123",
        "abbreviation": "a",
        "name": "a",
        "year": 2020
    }

    data["process_number"] = "7"
    response_abbreviation = api_client.post(
        '/box-abbreviation/', data=data_abbreviation,
        header={"Content-Type": "application/json"})
    assert response_rack.status_code == 201

    data['abbreviation_id'] = response_abbreviation.data['id']

    data["process_number"] = "8"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response = api_client.get('/search/?filter={"abbreviation_id":"a"}')
    assert response.status_code == 200

    data_unity = {
        "unity_name": "unity1",
        "unity_abbreviation": "u1",
        "administrative_bond": "a",
        "bond_abbreviation": "a",
        "municipality": "test",
        "telephone_number": "a",
        "notes": "1"
    }

    response_unity = api_client.post(
        '/unity/', data=data_unity,
        header={"Content-Type": "application/json"})
    assert response_unity.status_code == 201

    data['sender_unity'] = response_unity.data['id']

    data["process_number"] = "9"
    response_box_archiving = api_client.post(
        '/box-archiving/', data=data,
        format='json')
    assert response_box_archiving.status_code == 201

    response = api_client.get('/search/?filter={"sender_unity":"unity1"}')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search_without_specific_fields_from_admin_process():

    api_client = APIClient()

    data_document_name = {
        "document_name": "name",
        "temporality": 2020
    }

    response_document_name = api_client.post(
        '/document-name/', data=data_document_name,
        header={"Content-Type": "application/json"})
    assert response_document_name.status_code == 201

    data_unity = {
        "unity_name": "unity1",
        "unity_abbreviation": "u1",
        "administrative_bond": "a",
        "bond_abbreviation": "a",
        "municipality": "test",
        "telephone_number": "a",
        "notes": "1"
    }

    response_unity = api_client.post(
        '/unity/', data=data_unity,
        header={"Content-Type": "application/json"})
    assert response_unity.status_code == 201

    data = {
        "process_number": "12345",
        "notes": "1",
        "filer_user": "1",
        "notice_date": "2020-11-11",
        "interested": "1",
        "reference_month_year": "2020-11-11",
        "sender_user": None,
        "archiving_date": "2020-11-11",
        "is_filed": False,
        "is_eliminated": False,
        "temporality_date": 2021,
        "send_date": "2021-11-11",
        "administrative_process_number": "1",
        "document_name_id": None,
        "sender_unity": None
    }

    data['document_name_id'] = response_document_name.data['id']
    data['sender_unity'] = response_unity.data['id']

    response_admin = api_client.post(
        '/administrative-process/', data=data,
        format='json')
    assert response_admin.status_code == 201


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search_without_specific_fields_from_frequency_sheet():

    api_client = APIClient()

    data_unity = {
        "unity_name": "unity1",
        "unity_abbreviation": "u1",
        "administrative_bond": "a",
        "bond_abbreviation": "a",
        "municipality": "test",
        "telephone_number": "a",
        "notes": "1"
    }

    data_name = {
        "document_name": "name",
        "temporality": 2020
    }

    response_name = api_client.post(
        '/document-name/', data=data_name,
        header={"Content-Type": "application/json"})
    assert response_name.status_code == 201

    response_unity = api_client.post(
        '/unity/', data=data_unity,
        header={"Content-Type": "application/json"})
    assert response_unity.status_code == 201

    data_pw = {
        "name": "person1",
        "cpf": "1111111111",
    }

    response_pw = api_client.post(
        '/public-worker/', data=data_pw,
        header={"Content-Type": "application/json"})
    assert response_pw.status_code == 201

    data = {
        "person_id": None,
        "cpf": "1",
        "role": "1",
        "category": "1",
        "workplace": None,
        "municipal_area": "1",
        "reference_period": "2020-11-11",
        "notes": "1",
        "process_number": "1",
        "document_name_id": None,
        "temporality_date": 2021
    }

    data['workplace'] = response_unity.data['id']
    data['document_name_id'] = response_name.data['id']
    data['person_id'] = response_pw.data['id']

    response_sheet = api_client.post(
        '/frequency-sheet/', data=data,
        format='json')
    assert response_sheet.status_code == 201


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_get_year_by_abbreviation():
    api_client = APIClient()

    response = api_client.get('/year-by-abbreviation/a')
    assert response.status_code == 204

    data_box = {
        "number": 1,
        "abbreviation": 'a',
        "name": "abc",
        "year": 2020
    }

    response_box = api_client.post(
        '/box-abbreviation/', data=data_box,
        header={"Content-Type": "application/json"})
    assert response_box.status_code == 201

    response = api_client.get('/year-by-abbreviation/a')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_get_number_by_year_and_abbreviation():
    api_client = APIClient()

    response = api_client.get('/number-by-year-abbrevation/a/2021')
    assert response.status_code == 204

    data_box = {
        "number": 1,
        "abbreviation": 'a',
        "name": "abc",
        "year": 2021
    }

    response_box = api_client.post(
        '/box-abbreviation/', data=data_box,
        header={"Content-Type": "application/json"})
    assert response_box.status_code == 201

    response = api_client.get('/number-by-year-abbrevation/a/2021')
    assert response.status_code == 200
