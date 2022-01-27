from django.shortcuts import render
import typing
from decimal import Decimal
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
from borb.toolkit.location.location_filter import LocationFilter
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch
from django.http import HttpResponse,Http404
from first.serializers import *
from rest_framework import views
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from word2number import w2n
from .models import *

def ext(request):
    d: typing.Optional[Document] = None
    b: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Billing Address :")
    m: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Number :")
    n: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Date :")
    u: RegularExpressionTextExtraction = RegularExpressionTextExtraction("State/UT Code:")
    f: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Amount in Words:")
    rup: RegularExpressionTextExtraction = RegularExpressionTextExtraction("TOTAL:")
    main_dict={}
    main_file=open('am.pdf', "rb")
    legderlist=["Digital Documentation Systems"]
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
    print(main_dict)

    model = ledger.objects.create(
        Buyer_data = fff,
        In = aaa,
        In_date = bbb,
        C = ccc,
        T = ddd,
        G = eee

    )
    
    return HttpResponse("Chal Chal Have")