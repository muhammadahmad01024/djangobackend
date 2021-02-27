from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.

commonAttributes = {
    'id': 1,
    'topOffset': None,
    'leftOffset': None,
    'name': "",
    'checked': True,
    'commentButton': True,
    'exportButton': True,
}

@api_view(['POST'])
def getPanels(request):
    headers = Headers.objects.all()

    reporting = commonAttributes.copy()
    reporting['id'], reporting['name'] = 1, 'REPORTIN'
    reporting['records'] = [row.data for row in Reporting.objects.all()[:15]]
    reporting['attributes'] = [header.data for header in headers if 'reporting' in header.data][0]

    issueLog = commonAttributes.copy()
    issueLog['id'], issueLog['name'] = 2, 'ISSUE LOG'
    issueLog['records'] = [row.data for row in IssueLog.objects.all()[:10]]
    issueLog['attributes'] = [header.data for header in headers if 'issuelog' in header.data][0]

    financialCrime = commonAttributes.copy()
    financialCrime['id'], financialCrime['name'] = 3, 'FINANCIAL CRIME'
    financialCrime['records'] = [row.data for row in FinancialCrime.objects.all()[:10]]
    financialCrime['attributes'] = [header.data for header in headers if 'financialcrime' in header.data][0]

    news = commonAttributes.copy()
    news['id'], news['name'] = 4, 'News'
    news['records'] = [row.data for row in News.objects.all()[:10]]
    news['attributes'] = [header.data for header in headers if 'news' in header.data][0]

    upcomingRegulations = commonAttributes.copy()
    upcomingRegulations['id'], upcomingRegulations['name'] = 4, 'Upcoming Regulations'
    upcomingRegulations['records'] = [row.data for row in News.objects.all()[:10]]
    upcomingRegulations['attributes'] = [header.data for header in headers if 'upcomingregulations' in header.data][0]

    state = {
        'panels': [
            {'items': [reporting, issueLog, financialCrime]},
            {'items': [news, upcomingRegulations]}
        ],
        'dragging': False
    }

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
    comments = PanelComments.objects.filter(panelName=panel, rowId=rowid)
    comments = [{'comment': comment.commentText, 'id': comment.id} for comment in comments]

    return Response({'Count': len(comments), 'Comments': comments})


@api_view(['POST'])
def deleteComment(request):
    id = int(request.data.get('id'))
    comment = PanelComments.objects.get(id=id)
    comment.delete()
    return Response({'Status': 'Delete'})


@api_view(['POST','GET'])
def getPDF(request):
    # id = int(request.data.get('id'))
    pdf = open('MuhammadAhmad_Resume.pdf', 'rb')
    response = HttpResponse(FileWrapper(pdf), content_type='application/pdf')
    return response
