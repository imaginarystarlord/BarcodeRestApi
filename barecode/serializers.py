from rest_framework import serializers
# from pyzbar import pyzbar
# import cv2
#
#
#
#
#
# def barcodefunc(image1,text):
#     image=cv2.imread(image1)
#     cv2.imshow("image",image)
#     barcodes = pyzbar.decode(image)
#
#     for barcode in barcodes:
#
#         barcodeData = barcode.data.decode("utf-8")
#         barcodeType = barcode.type
#
#     if text == int(barcodeData):
#         return '1'
#     else:
#         return '0'

class BarcodeSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    text = serializers.IntegerField()
    # g = barcodefunc(image,text)
