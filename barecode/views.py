from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from pyzbar import pyzbar
# import cv2
from PIL import Image
from barecode import serializers




def barcodefunc(image1,text):
    # import cv2
    # image=cv2.imread(image1)
    #cv2.imshow("image",image)
    img = Image.open(image1)
    barcodes = pyzbar.decode(img)

    barcodeData=0
    for barcode in barcodes:

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type


    if str(text) == barcodeData:
        return '1',barcodeData
    else:
        return '0',barcodeData








class BarcodeViewSet(viewsets.ViewSet):
    '''Test API Viewset'''
    serializer_class = serializers.BarcodeSerializer
    def create(self,request):
        '''Create a new hello message'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            image = serializer.validated_data.get('image')
            text = serializer.validated_data.get('text')
            #g = serializer.validated_data.get('g')
            validation = barcodefunc(image,text)

            return Response({'validation':validation})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
