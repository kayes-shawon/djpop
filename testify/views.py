from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import pandas as pd


class HeadAPIView(APIView):
    def get(self, request: Request) -> Response:
        pop_df = pd.read_csv('https://raw.githubusercontent.com/FazlyRabbiBD/PublicAnalytics/main/bangladesh_population_2100.csv')
        head = pop_df.head()
        return Response(head)

