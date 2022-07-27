from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import MortgageSerializer
from .services import get_mortgage_list, save_data, get_filtered_mortgages


class MortgageViewSet(ViewSet):
    def create(self, request):
        serializer = MortgageSerializer(data=request.data)
        if serializer.is_valid():
            initial_fee = int(serializer.validated_data.get("initial_fee"))
            term = int(serializer.validated_data.get("term"))
            bank_name_filter = serializer.validated_data.get("bank_name_filter")
            rate_min_filter = serializer.validated_data.get("rate_min_filter")
            rate_max_filter = serializer.validated_data.get("rate_max_filter")
            mortgage_data = get_mortgage_list(initial_fee=initial_fee, term=term)
            filtered_data = get_filtered_mortgages(
                mortgage_data=mortgage_data,
                bank_name_filter=bank_name_filter,
                rate_min_filter=rate_min_filter,
                rate_max_filter=rate_max_filter
            )
            print(filtered_data)
            save_data(filtered_data)
            return Response({'offers': len(filtered_data), 'data': filtered_data})
        else:
            return Response({'error': 'Data is not valid'})
