from rest_framework.response import Response
from rest_framework.views import APIView

from quotes_api.apps.utils import check_request_param as rp
from .serializers import *
from bson import ObjectId

class QuotesCreateView(APIView):
    def post(self, request):
        data=QuotesCreateSerializer(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            quote = Quote.objects.create_quote(data.validated_data)
            print(quote)
            js = QuoteSerializer(quote)
            return Response(data={'ok': True,
                                  'message': 'quote created successfully',
                                  'quotes': [js.data]
                                  })
        else:
            return Response(data={'ok': False, 'message': data.errors})


class QuotesHomeView(APIView):
    def get(self, request):
        data=QuotesHomeSerializer(data={
            'device_id': rp(request,'device_id'),
            'page': rp(request,'page'),
        })
        if data.is_valid():    
            print(data.validated_data)
            quotes = Quote.objects.home_quotes(
                device_id = data.validated_data['device_id'],
                page = data.validated_data['page']
            )
            
            js = QuoteSerializer(quotes, many=True).data
            return Response(data={'ok':True,
                                'message': 'random quotes', 'quotes': js})
        else:
            return Response(data={'ok':False, 'message':data.errors})
        
        
class QuoteReadView(APIView):
    def get(self, request):
        data=QuoteReadSerializer(data={
            'quote_id': rp(request, 'quote_id'),
            'device_id': rp(request,'device_id'),
        })
        if data.is_valid():
            quote = Quote.objects.read(
                device_id = data.validated_data['device_id'],
                _id=ObjectId(data.validated_data['quote_id']))
            if quote is not None:
                js = QuoteSerializer(quote).data
                return Response(data={'ok': True,
                                      'message': 'a quote from the server',
                                      'quote': js})
            else:
                return Response(data={'ok': False, 'message': 'invalid quote id'})
        else:
            return Response(data={'ok':False, 'message': data.errors})

        
class QuoteVotesUpdateView(APIView):
    def put(self, request):
        data=QuotesVotesSerializer(data={
            'quote_id': rp(request,'quote_id'),
            'device_id': rp(request,'device_id'),
            'positive': rp(request,'positive'),
        })
        if data.is_valid():
            print(data.validated_data)
            quote = Quote.objects.update_votes(
                device_id = data.validated_data['device_id'],
                _id=ObjectId(data.validated_data['quote_id']),
                positive=data.validated_data['positive'])
            if quote is not None:
                return Response(data={'ok': True, 'message': 'quote ups updated successfully'})
            else:
                return Response(data={'ok':False, 'message': 'invalid quote id'})
        else:
            return Response(data={'ok':False, 'message': data.errors})

        
class QuotesSearch(APIView):
    def get(self, request):
        data=QuotesSearchSerializer(data={
            'query': rp(request ,'query'),
            'device_id': rp(request,'device_id'),
            'page': rp(request,'page'),
            'each': rp(request,'each'),
        })
        if data.is_valid():
            print(data.validated_data)
            quotes = Quote.objects.search(
                query=data.validated_data['query'],
                device_id=data.validated_data['device_id'],
                page=data.validated_data['page'],
                each=data.validated_data['each'],
            )
            js = QuoteSerializer(quotes, many=True).data
            return Response(data={'ok':True, 'message': 'quotes searching result',
                                  'quotes': js})
        else:
            return Response(data={'ok':False, 'message': data.errors})
