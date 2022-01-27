from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv
from first.models import *
from django.http import HttpResponse,Http404,response
from first.serializers import *
from rest_framework import views
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.conf import settings
from difflib import SequenceMatcher
from pdf2image import convert_from_path
from PIL import Image
import ocrmypdf 
import datetime
import netifaces
import cv2
import numpy as np


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from word2number import w2n
from .models import *
import typing
from decimal import Decimal
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
from borb.toolkit.location.location_filter import LocationFilter
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch


# Create your views here.
class Demoview(APIView):
    serializer_class = NewSerializer
    def get(self, request):
        queryset = Plo.objects.all()
        print(queryset)
        serializer = DemoSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self,  request):
        
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()
        serializer.save()
        try:
            value=serializer.data['file']
            value1 = str(settings.BASE_DIR)+value
            print(value1)
            

            d: typing.Optional[Document] = None
            b: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Billing Address :")
            m: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Number :")
            n: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Date :")
            u: RegularExpressionTextExtraction = RegularExpressionTextExtraction("State/UT Code:")
            f: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Amount in Words:")
            rup: RegularExpressionTextExtraction = RegularExpressionTextExtraction("TOTAL:")
            main_dict={}
            main_file=open(value1, "rb")
            legderlist=["Digital Documentation Systems", "Elayers Interactive Pvt. Ltd."]
            # mod=ladgernamedata.objects.all()
            # for a in mod:
            #     legderlist.append(a.ledeger_name)
            try:
                if b:
                    d = PDF.loads(main_file, [b])
                    assert d is not None
                    matches: typing.List[PDFMatch] = b.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(180),
                                                data.get_y() - Decimal(100),
                                                Decimal(400),
                                                Decimal(100))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)
                    d = PDF.loads(main_file, [l0])
                    assert d is not None
                    y=l1.get_text_for_page(0)
                    print(y)
                    data=''
                    for leg in legderlist:
                        if leg[:4] in y:
                            data=leg
                fff = main_dict['Buyer Data']=data
                print(data)
            except:
                pass
            try:
                if m:
                    d = PDF.loads(main_file, [m])
                    assert d is not None
                    matches: typing.List[PDFMatch] = m.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                            data.get_y() - Decimal(5),
                                            Decimal(400),
                                            Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])
                    assert d is not None
                    y=l1.get_text_for_page(0)
                aaa = main_dict['Invoice Number']=y.replace('Invoice Number :', '')
            except:
                pass
            try:
                if n:
                    d = PDF.loads(main_file, [n])
                    assert d is not None
                    matches: typing.List[PDFMatch] = n.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                            data.get_y() - Decimal(5),
                                            Decimal(400),
                                            Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    z=l1.get_text_for_page(0)
                bbb =main_dict['Invoice Date']=z.replace('Invoice Date :', '')
            except:
                pass
        

            try:
                if u:
                    d = PDF.loads(main_file, [u])
                    assert d is not None
                    matches: typing.List[PDFMatch] = u.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                        data.get_y() - Decimal(5),
                                        Decimal(400),
                                        Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                ccc = main_dict['Code']=l1.get_text_for_page(0).replace('State/UT Code:', '')
                

            except:
                pass
            try:
                if f:
                    d = PDF.loads(main_file, [f])
                    assert d is not None
                    matches: typing.List[PDFMatch] = f.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(100),
                                    data.get_y() - Decimal(20),
                                    Decimal(400),
                                    Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    y=l1.get_text_for_page(0)
                    try:
                        main_total=w2n.word_to_num(y)
                    except Exception as e:
                        nex_txt=''
                        for i,letter in enumerate(y):
                            if i and letter.isupper():
                                nex_txt+=' '
                            nex_txt+=letter
                        main_total=w2n.word_to_num(nex_txt)
                ddd =main_dict['Total']=str(main_total)
            except:
                pass
            try:
                if rup:
                    d = PDF.loads(main_file, [rup])
                    assert d is not None
                    matches: typing.List[PDFMatch] = rup.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(100),
                                    data.get_y() - Decimal(10),
                                    Decimal(575),
                                    Decimal(20))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    z=l1.get_text_for_page(0)
                    new=z.replace('�','')
                eee = main_dict['GST Total']=new.replace('TOTAL:', '')
            except:
                pass

            interface = netifaces.interfaces()
            print(interface)
            int = interface[1]
            addrs = netifaces.ifaddresses(int)
            x = addrs.get(10)
            global_add = x[0].get('addr')
            print(global_add)
            link_local = x[2].get('addr')
            link_local = link_local.replace("%enp8s0","" )
            print(link_local)
            final_add = global_add +":"+ link_local


            inv=Plo.objects.latest('id')
            inv.Buyer_data=fff
            inv.In=aaa
            inv.In_date=bbb
            inv.C=ccc
            inv.T = ddd
            inv.G=eee
            inv.ipp = final_add
            inv.save()

        except:
            inv=Plo.objects.latest('id')
            inv.delete()



        print(main_dict)

        

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Demoview_one(APIView):
    def get_object(self, id):
        try:
            return Plo.objects.get(id=id)
        except Plo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet)
        return Response(serializer.data)

class Update(APIView):

    def get_object(self, id):
        try:
            return Plo.objects.get(id=id)
        except Plo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, id):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):

    def get_object(self, id):
        try:
            return Plo.objects.get(id=id)
        except Plo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, id):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Put(APIView):

    def get_object(self, id):
        try:
            return Plo.objects.get(id=id)
        except Plo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = DemoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def savecsv(self):
    with open('Alag.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader: # to access rows from csv
            p = row.get('paisa')
            print(type(p))
            v = row.get('vastu')
            print(v)
            x = data()        
            # conditions for null values in csv
            try:
                data.objects.get(Vastu=v) 
                continue   
            except:
                model = data.objects.create(
                Paisa= p or None, 
                Vastu= v 
                )
                model.save()
                # if p == '' and v == '':
                #     print('final')
                #     x.Paisa = 0
                #     x.Vastu = "Not Given"
                #     x.save()
                # elif p == '':
                #     x.Paisa = 0
                #     x.Vastu = v
                #     x.save()
                # elif v == '':
                #     x.Paisa = p
                #     x.Vastu = "Not Given"
                #     x.save()
                # else:
                #     x.Paisa = p
                #     x.Vastu = v
                #     x.save()
    return HttpResponse("Thai Gayu")
     

                
                

            
            

class ModelFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(lookup_expr='icontains')
    # Name = django_filters.CharFilter(queryset=Plo.objects.all())

    
    class Meta:
        model = Plo
        fields = ['Name']


class Mfilter(generics.ListAPIView):
    queryset=Plo.objects.all()
    serializer_class=DemoSerializer    
    filter_backends1 = (DjangoFilterBackend)
    filterset_fields = [ 'Name']    
    filter_class = ModelFilter
                
            


class Tallyview(APIView):
    serializer_class = AlagSerializer
    def get(self, request):
        queryset = Tally.objects.all()
        print(queryset)
        serializer = tallySerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self,  request):
        
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()
        serializer.save()
        value=serializer.data['file']
        value1 = str(settings.BASE_DIR)+value
        print(value1)


        images = convert_from_path(value1, dpi = 250)
        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save('khanak.jpg', 'JPEG')


        img_for_box_extraction_path='khanak.jpg'
        img = cv2.imread(img_for_box_extraction_path, 0)
        # Thresholding the image
        (thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|     
        cv2.THRESH_OTSU)
        # Invert the image
        img_bin = ~img_bin
        cv2.imwrite("Image_bin.jpg",img_bin)
        bw = cv2.adaptiveThreshold(img_bin, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 15, -2)
        horizontal = np.copy(bw)
        vertical = np.copy(bw)
        # Defining a kernel length for horizontal and vertical 
        cols = horizontal.shape[1]
        horizontal_size = int(cols)
        horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, 
        (horizontal_size, 1))
        # Apply morphology operations
        horizontal = cv2.erode(horizontal, horizontalStructure)
        horizontal = cv2.dilate(horizontal, horizontalStructure)
        rows = vertical.shape[0]
        verticalsize = int(rows)
        # Create structure element for extracting verticaimg_for_box_extraction_path='ttt0.png'
        img = cv2.imread(img_for_box_extraction_path, 0)
        # Thresholding the image
        (thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|     
        cv2.THRESH_OTSU)
        # Invert the image
        img_bin = ~img_bin
        cv2.imwrite("Image_bin.jpg",img_bin)
        bw = cv2.adaptiveThreshold(img_bin, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 15, -2)
        horizontal = np.copy(bw)
        vertical = np.copy(bw)
        # Defining a kernel length for horizontal and vertical 
        cols = horizontal.shape[1]
        horizontal_size = int(cols)
        horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, 
        (horizontal_size, 1))
        # Apply morphology operations
        horizontal = cv2.erode(horizontal, horizontalStructure)
        horizontal = cv2.dilate(horizontal, horizontalStructure)
        rows = vertical.shape[0]
        verticalsize = int(rows)
        # Create structure element for extracting vertical lines through morphology 
        # operations
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 
        verticalsize))
        # Apply morphology operations
        vertical = cv2.erode(vertical, verticalStructure)
        vertical = cv2.dilate(vertical, verticalStructure)
        #kernel_length = np.array(img).shape[1]//80
        #kernel_length = 7
        # A verticle kernel of (1 X kernel_length =6), which will detect all the 
        # verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 7))
        # A horizontal kernel of (kernel_length=7 X 1), which will help to detect 
        # all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 1))
        # A kernel of (3 X 3) ones.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=6)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=6)
        cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=4)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=4)
        cv2.imwrite("horizontal_lines.jpg",verticle_lines_img)
        res = verticle_lines_img + horizontal_lines_img
        #fin = cv2.bitwise_and(img_bin, img_bin, mask = cv2.bitwise_not(res))
        exp = img_bin - res
        exp = ~exp
        cv2.imwrite("final.jpg",exp)
        vertical = cv2.dilate(vertical, verticalStructure)
        #kernel_length = np.array(img).shape[1]//80
        #kernel_length = 7
        # A verticle kernel of (1 X kernel_length =6), which will detect all the 
        # verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 7))
        # A horizontal kernel of (kernel_length=7 X 1), which will help to detect 
        # all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 1))
        # A kernel of (3 X 3) ones.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=6)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=6)
        cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=4)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=4)
        cv2.imwrite("horizontal_lines.jpg",verticle_lines_img)
        res = verticle_lines_img + horizontal_lines_img
        #fin = cv2.bitwise_and(img_bin, img_bin, mask = cv2.bitwise_not(res))
        exp = img_bin - res
        exp = ~exp
        cv2.imwrite("khanakfinal.jpg",exp)


        image1 = Image.open('khanakfinal.jpg')
        im1 = image1.convert('RGB')
        im1.save(r'khanakdifferent.pdf')


        def ocr(file_path, save_path):
            ocrmypdf.ocr(file_path, save_path,skip_text=True)
        ocr('khanakdifferent.pdf','khanakfinal22.pdf')
        l: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Buyer")
        m: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice No.")
        n: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Dated")
        u: RegularExpressionTextExtraction = RegularExpressionTextExtraction("SGST")
        f: RegularExpressionTextExtraction = RegularExpressionTextExtraction("CGST")
        rup: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Total")
        main_dict = {}
        legderlist=['DIGITAL DOCUMENTATION SYSTEMS','Neel Industries','Digital Documentation Systems Pvt Ltd','Neel Enterprise', 'Dharmendar Systems', 'Digital']
        main_file=open("khanakfinal22.pdf", "rb")
        try:
            if l:
                d = PDF.loads(main_file, [l])
                assert d is not None
                matches: typing.List[PDFMatch] = l.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                            data.get_y() - Decimal(65),
                                            Decimal(600),
                                            Decimal(40))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)
                d = PDF.loads(main_file, [l0])
                assert d is not None
                y=l1.get_text_for_page(0)
                print(y)
                score = []
                for i in (legderlist):
                    my_seq = SequenceMatcher(a=i,b=y)
                    score.append(my_seq.ratio())
                    print(my_seq.ratio())        
                dif=score.index(max(score))
                print(legderlist[dif],'index=',dif)
                new = legderlist[dif]
            main_dict['Buyer Data']=new.replace('Buyer' , '')
            print(main_dict)
        except:
            pass
        try:
            if m:
                d = PDF.loads(main_file, [m])
                assert d is not None
                matches: typing.List[PDFMatch] = m.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                        data.get_y() - Decimal(45),
                                        Decimal(200),
                                        Decimal(50))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)

                d = PDF.loads(main_file, [l0])
                assert d is not None
                y=l1.get_text_for_page(0)
            main_dict['Invoice Number']=y.replace('Invoice No.' , '')
            print(main_dict)
        except:
            pass
        try:
            if n:
                d = PDF.loads(main_file, [n])
                assert d is not None
                matches: typing.List[PDFMatch] = n.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                        data.get_y() - Decimal(70),
                                        Decimal(1200),
                                        Decimal(50))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)

                d = PDF.loads(main_file, [l0])

                assert d is not None
                
                z=l1.get_text_for_page(0)
                print(z)
            main_dict['Dated']=z.replace('Dated\n', '')
            print(main_dict)
        except:
            pass
        try:
            if u:
                d = PDF.loads(main_file, [u])
                assert d is not None
                matches: typing.List[PDFMatch] = u.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                    data.get_y() - Decimal(30),
                                    Decimal(1200),
                                    Decimal(50))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)

                d = PDF.loads(main_file, [l0])

                assert d is not None
            r = l1.get_text_for_page(0) 
            main_dict['SGST']=r.replace('SGST' , '')

        except:
            pass
        try:
            if f:
                d = PDF.loads(main_file, [f])
                assert d is not None
                matches: typing.List[PDFMatch] = f.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                    data.get_y() - Decimal(30),
                                    Decimal(1200),
                                    Decimal(50))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)

                d = PDF.loads(main_file, [l0])

                assert d is not None
            r = l1.get_text_for_page(0)     
            main_dict['CGST']=r.replace('CGST' , '')

        except:
            pass
        try:
            if rup:
                d = PDF.loads(main_file, [rup])
                assert d is not None
                matches: typing.List[PDFMatch] = rup.get_matches_for_page(0)
                assert len(matches) >= 0
                data=matches[0].get_bounding_boxes()[0]
                r: Rectangle = Rectangle(data.get_x() - Decimal(-700),
                                data.get_y() - Decimal(30),
                                Decimal(400),
                                Decimal(50))
                l0: LocationFilter = LocationFilter(r)
                l1: SimpleTextExtraction = SimpleTextExtraction()
                l0.add_listener(l1)

                d = PDF.loads(main_file, [l0])

                assert d is not None
                y=l1.get_text_for_page(0)
                print(y)
                nnn = y.replace('= ', '')
            main_dict['Total']=nnn.replace('z', '')
        except:
            pass
        inv=Tally.objects.latest('id')
        inv.Buyer_data= main_dict.get('Buyer Data','')
        inv.In=main_dict.get('Invoice Number','')
      

        date_list=['%d-%m-%y','%d-%m-%Y','%d/%m/%y','%d/%m/%Y','%d-%b-%Y','%d-%B-%Y','%d-%b-%y','%d-%B-%y','%d/%b/%Y','%d/%B/%Y','%d/%b/%y','%d/%B/%y','%d %b %Y','%d.%m.%Y']
        
        for i in date_list:
            try:
                main_date=datetime.datetime.strptime(main_dict['Dated'], i).date()
                inv.date = main_date
            except:
                pass
        print(main_dict)
        inv.S = main_dict.get('SGST', '')
        inv.C =main_dict.get('CGST', '')
        inv.T = main_dict.get('Total', '')        
        inv.save()

        


        return Response(serializer.data, status=status.HTTP_201_CREATED)                
                
            
class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response


            