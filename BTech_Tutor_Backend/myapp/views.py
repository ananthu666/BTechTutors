from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

class UserdataViewSet(viewsets.ModelViewSet):
    queryset = Userdata.objects.all()
    serializer_class = UserdataSerializer

class BtechViewSet(viewsets.ModelViewSet):
    queryset = Btech.objects.all()
    serializer_class = BtechSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class DepSubRelViewSet(viewsets.ModelViewSet):
    queryset = DepSubRel.objects.all()
    serializer_class = DepSubRelSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

class GateDEPViewSet(viewsets.ModelViewSet):
    queryset = GateDEP.objects.all()
    serializer_class = GateDEPSerializer

class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

class BundleViewSet(viewsets.ModelViewSet):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer

class InternDepViewSet(viewsets.ModelViewSet):
    queryset = InternDep.objects.all()
    serializer_class = InternDepSerializer

class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class DemoClassViewSet(viewsets.ModelViewSet):
    queryset = DemoClass.objects.all()
    serializer_class = DemoClassSerializer
