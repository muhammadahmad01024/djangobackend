from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.

REPORTIN = {
    'id': 1,
    'topOffset': None,
    'leftOffset': None,
    'name': "REPORTIN",
    'attributes': {
        "ID": True, "Group": True, "Book": True, "Counterparty": True, "Instr Type": True, "Trade Date": True,
        "Trade": True, "Trade ID": True, "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", "xyz", "1122", True],
        [2, "LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", "xyz", "1122", True],
        [3, "NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", "xyz", "1122", True],
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
        "ID": True, "Date": True, "Issue ID": True, "IDD": True, "Comment": True, "Status": True, "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1234", "ZXC", "*&^*&^&**", "12312313", True],
        [2, "LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
        [3, "NYC Credit", "0011", "ABC", "*&^*&^&**", "12312313", True],
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
        "ID": True, "Regulator": True, "Specification": True, "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1111", True],
        [2, "LDN Credit", "00000", True],
        [3, "NYC Credit", "12121", True],
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
        "ID": True, "Date": True, "News item": True, "Source": True, "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1234", "ABC", True],
        [2, "LDN Credit", "2345", "QWE", True],
        [3, "NYC Credit", "2345", "AAC", True],
        [4, "NYC Credit", "5345", "AAD", True],
        [5, "NYC Credit", "6345", "ABC", True],
        [6, "NYC Credit", "3345", "BAC", True],
    ],
    'checked': True,
    'commentButton': False,
    'exportButton': False,
}
UPCOMING_REGULATIONS = {
    'id': 5,
    'topOffset': None,
    'leftOffset': None,
    'name': "Upcoming Regulations",
    'attributes': {
        "ID": True, "Regulator": True, "Specification": True, "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "12312313", True],
        [2, "LDN Credit", "12312313", True],
        [3, "NYC Credit", "12312313", True],
    ],
    'checked': True,
    'commentButton': False,
    'exportButton': False,
}
Panel_6 = {
    'id': 6,
    'topOffset': None,
    'leftOffset': None,
    'name': "Panel 6",
    'attributes': {
        "ID": True, "Group": True, "Book": True, "Counterparty": True, "TTTTTTTTT": True, "IIIIIIIIII": True,
        "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", True],
        [2, "LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
        [3, "NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", True],
    ],
    'checked': False,
    'commentButton': False,
    'exportButton': False,
}
Panel_7 = {
    'id': 7,
    'topOffset': None,
    'leftOffset': None,
    'name': "Panel 7",
    'attributes': {
        "ID": True, "Group": True, "Book": True, "Counterparty": True, "TTTTTTTTT": True, "IIIIIIIIII": True,
        "Filter": True,
    },
    'records': [
        [1, "LDN Credit", "1234", "ABC", "*&^*&^&**", "12312313", True],
        [2, "LDN Credit", "2345", "QWE", "*&^*&^&**", "12312313", True],
        [3, "NYC Credit", "3456", "ZXC", "*&^*&^&**", "12312313", True],
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


@api_view(['POST'])
def saveComment(request):
    rowid = int(request.data.get('rowid'))
    panel = request.data.get('panel')
    commentText = request.data.get('comment')

    comment = PanelComments(panelName=panel, rowId=rowid, commentText=commentText)
    # from panels.models import *
    # c = PanelComments(panelName="panel111", rowId=1, commentText="commentText111")
    comment.save()
    return Response({'Status': 'Saved'})


@api_view(['POST'])
def getComments(request):
    rowid = int(request.data.get('rowid'))
    panel = request.data.get('panel')
    comments = PanelComments.objects.filter(panelName='panel111', rowId=1)
    comments = [comment.commentText for comment in comments]

    return Response({'Count': len(comments), 'Comments': comments})
