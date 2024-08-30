from django.shortcuts import render
from django.db.models import F
from django.db.models import Prefetch
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



class GetSubjectViewSet(viewsets.ModelViewSet):
    queryset = DepSubRel.objects.all()
    serializer_class = DepSubRelSerializer
    
    def get_queryset(self):
        
        # depname = self.request.query_params.get('depname')
        # semnum = self.request.query_params.get('semnum')
        # scheme=self.request.query_params.get('scheme')
        depname = self.request.data['depname']
        semnum = self.request.data['semnum']
        scheme=self.request.data['scheme']
        
        
        # depid=1
        # semnum=1
        # scheme=2019
        
        queryset = DepSubRel.objects.filter(
            semnum=semnum,
            depid__name=depname,
            depid__btech_id=scheme
        ).annotate(
            subject_name=F('subjectid__name')  
        )
        
        
        
        return queryset
        

class GetContentsViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        # subid = self.request.query_params.get('subid')
        subid = self.request.data["subid"]

        queryset = Subject.objects.filter(id=subid).prefetch_related(
            'syllabusfile_id',
            Prefetch(
                'questionpaper_set',
                queryset=QuestionPaper.objects.select_related('file_id')
            )
        )

        return queryset

class GetNotesViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer


    def get_queryset(self):
        # subid = self.request.query_params.get('subid')
        subname = self.request.data["subname"]
        module = self.request.data["module"]


        subid = Subject.objects.filter(name=subname).values_list('id', flat=True).first()
        print("Subid", subid)
        fileids = Notes.objects.filter(subid=subid, module=module).values_list('file_id', flat=True)
        for i in fileids:
            print(i)
        queryset = File.objects.filter(id__in=fileids)



        return queryset