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



class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

class BundleViewSet(viewsets.ModelViewSet):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer



class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer





class GetSubjectViewSet(viewsets.ModelViewSet):
    queryset = DepSubRel.objects.all()
    serializer_class = DepSubRelSerializer
    
    def get_queryset(self):
        
        depname = self.request.query_params.get('depname')
        semnum = self.request.query_params.get('semnum')
        scheme=self.request.query_params.get('scheme')
        print(self.request.data)
        # depname = self.request.data['depname']
        # semnum = self.request.data['semnum']
        # scheme=self.request.data['scheme']
        
        
        # depname='cse'
        # semnum=2
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
        subid = self.request.query_params.get('subid')
        # subid = self.request.data["subid"]

        queryset = Subject.objects.filter(id=subid)
        # .prefetch_related(
        #     # 'syllabusfile_id',
        #     Prefetch(
        #         'questionpaper_set',
        #         queryset=QuestionPaper.objects.select_related('file_id')
        #     )
        # )

        return queryset

class GetNotesViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer


    def get_queryset(self):
        subid = self.request.query_params.get('subid')
        module = self.request.query_params.get('module')
        # subname = self.request.data["subname"]
        # module = self.request.data["module"]


        subid = Subject.objects.filter(name=subname).values_list('id', flat=True).first()
        print("Subid", subid)
        fileids = Notes.objects.filter(subid=subid, module=module).values_list('file_id', flat=True)
        for i in fileids:
            print(i)
        queryset = File.objects.filter(id__in=fileids)



        return queryset


class GetGateViewSet(viewsets.ModelViewSet):
    serializer_class = GateSerializer
    

    def get_queryset(self):
        depname = self.request.query_params.get('depname')
        # depname = self.request.data["depname"]
        queryset = Gate.objects.filter(depid__name=depname)

        return queryset


class GetBundleViewSet(viewsets.ModelViewSet):
    serializer_class = BundleSerializer

    def get_queryset(self):
        depname = self.request.query_params.get('depname')
        # depname = self.request.data["depname"]
        queryset = Bundle.objects.filter(depid__name=depname)

        return queryset

class GetInternshipViewSet(viewsets.ModelViewSet):
    serializer_class = InternshipSerializer

    def get_queryset(self):
        depname = self.request.query_params.get('depname')
        # depname = self.request.data["depname"]
        queryset = Internship.objects.filter(depid__name=depname)

        return queryset
    
class GetProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        depname = self.request.query_params.get('depname')
        # depname = self.request.data["depname"]
        queryset = Project.objects.filter(depid__name=depname)

        return queryset

class GetNotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    