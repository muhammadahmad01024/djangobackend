from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

REPORTIN = {
    'id': 1,
    'topOffset': None,
    'leftOffset': None,
    'name': "REPORTIN",
    'attributes': {
        "Group": True, "Book": True, "Counterparty": True, "Instr Type": True, "Trade Date": True,
        "Trade": True, "Trade ID": True, "Filter": True,
    },
    'records': [
        ["LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", "xyz", "1122", True],
        ["LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", "xyz", "1122", True],
        ["NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", "xyz", "1122", True],
    ],
    'checked': True,
    'commentButton': True,
    'exportButton': True,
}

ISSUE_LOG = {
    'id': 2,
    'name': "ISSUE LOG",
    'topOffset': None,
    'leftOffset': None,
    'attributes': {
        "Date": True, "Issue ID": True, "ID": True, "Comment": True, "Status": True, "Filter": True,
    },
    'records': [
        ["LDN Credit", "1234", "ZXC", "*&^*&^&**", "12312313", True],
        ["LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
        ["NYC Credit", "0011", "ABC", "*&^*&^&**", "12312313", True],
    ],
    'checked': True,
    'commentButton': True,
    'exportButton': True,
}

FINANCIAL_CRIME = {
    'id': 3,
    'topOffset': None,
    'leftOffset': None,
    'name': "FINANCIAL CRIME",
    'attributes': {
        "Regulator": True, "Specification": True, "Filter": True,
    },
    'records': [
        ["LDN Credit", "1111", True],
        ["LDN Credit", "00000", True],
        ["NYC Credit", "12121", True],
    ],
    'checked': True,
    'commentButton': False,
    'exportButton': False,
}

NEWS = {
           'id': 4,
           'topOffset': None,
           'leftOffset': None,
           'name': "News",
           'attributes': {
               "Date": True, "News item": True, "Source": True, "Filter": True,
           },
           'records': [
               ["LDN Credit", "1234", "ABC", True],
               ["LDN Credit", "2345", "QWE", True],
               ["NYC Credit", "2345", "AAC", True],
               ["NYC Credit", "5345", "AAD", True],
               ["NYC Credit", "6345", "ABC", True],
               ["NYC Credit", "3345", "BAC", True],
           ],
           'checked': True,
           'commentButton': False,
           'exportButton': False,
       },
UPCOMING_REGULATIONS = {
                           'id': 5,
                           'topOffset': None,
                           'leftOffset': None,
                           'name': "Upcoming Regulations",
                           'attributes': {
                               "Regulator": True, "Specification": True, "Filter": True,
                           },
                           'records': [
                               ["LDN Credit", "12312313", True],
                               ["LDN Credit", "12312313", True],
                               ["NYC Credit", "12312313", True],
                           ],
                           'checked': True,
                           'commentButton': False,
                           'exportButton': False,
                       },
Panel_6 = {
              'id': 6,
              'topOffset': None,
              'leftOffset': None,
              'name': "Panel 6",
              'attributes': {
                  "Group": True, "Book": True, "Counterparty": True, "TTTTTTTTT": True, "IIIIIIIIII": True,
                  "Filter": True,
              },
              'records': [
                  ["LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", True],
                  ["LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
                  ["NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", True],
              ],
              'checked': False,
              'commentButton': False,
              'exportButton': False,
          },
Panel_7 = {
    'id': 7,
    'topOffset': None,
    'leftOffset': None,
    'name': "Panel 7",
    'attributes': {
        "Group": True, "Book": True, "Counterparty": True, "TTTTTTTTT": True, "IIIIIIIIII": True,
        "Filter": True,
    },
    'records': [
        ["LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", True],
        ["LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
        ["NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", True],
    ],
    'checked': False,
    'commentButton': False,
    'exportButton': False,
}


@api_view(['POST'])
def getPanels(request):
    state = {
        'panels': [
            {'items': [REPORTIN, ISSUE_LOG, FINANCIAL_CRIME]},
            {'items': [NEWS, UPCOMING_REGULATIONS, Panel_6, Panel_7]}
        ],
        'dragging': False
    }

    # quote_number = request.data['id']
    # q = Quote.objects.get(quote_number=quote_number)
    # q.quoteproduct_set.all().delete()
    # q.quotepartialpayment_set.all().delete()
    # q.delete()

    return Response(state)
