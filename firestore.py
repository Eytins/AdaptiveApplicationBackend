import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import Client


def db() -> Client:
    cred = credentials.Certificate('rockhopper-tcd-firebase-adminsdk-1twwd-54d810567f.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()


def get_detail_by_barcode(code) -> dict:
    url = 'https://world.openfoodfacts.org/api/v0/product/' + code + '.json'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    client = db()
    col = client.collection('barcode_data')
    barcode_list = [
        '8076800195057',
        '80052760',
        '5411188118121',
        '80176800',
        '8712566328352',
        '4061458061506',
        '8076802085837',
        '7622300489434',
        '4001724818908'
    ]
    for each in barcode_list:
        resp = get_detail_by_barcode(each)
        ref = col.document(each)
        ref.set({
            'name': resp['product']['product_name_en'],
            'carbohydrates': resp['product']['nutriments']['carbohydrates'],
            'carbohydrates_100g': resp['product']['nutriments']['carbohydrates_100g'],
            'energy': resp['product']['nutriments']['energy'],
            'energy-kcal_100g': resp['product']['nutriments']['energy-kcal_100g'],
            'fat': resp['product']['nutriments']['fat'],
            'fat_100g': resp['product']['nutriments']['fat_100g'],
            'fiber': resp['product']['nutriments']['fiber'],
            'fiber_100g': resp['product']['nutriments']['fiber_100g'],
            'proteins': resp['product']['nutriments']['proteins'],
            'proteins_100g': resp['product']['nutriments']['proteins_100g'],
            'sodium': resp['product']['nutriments']['sodium'],
            'sodium_100g': resp['product']['nutriments']['sodium_100g'],
            'sugars': resp['product']['nutriments']['sugars'],
            'sugars_100g': resp['product']['nutriments']['sugars_100g'],
            'nutriscore_grade': resp['product']['nutriscore_grade'],
            'quantity': resp['product']['quantity']
        })
    client.close()
