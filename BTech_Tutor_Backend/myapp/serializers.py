from rest_framework import serializers
from .models import *

class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__'

class BtechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Btech
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    filelink = FileSerializer(source='file_id')
    class Meta:
        model = QuestionPaper
        fields = '__all__'



class SubjectSerializer(serializers.ModelSerializer):
    syllabus = FileSerializer(source='syllabusfile_id')
    question_papers = QuestionPaperSerializer(source='questionpaper_set', many=True)
    

    class Meta:
        model = Subject
        fields = ['id', 'code', 'name', 'syllabus','question_papers','demolink','courselink']

class DepSubRelSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField()
    
    class Meta:
        model = DepSubRel
        fields = '__all__'
     # Assuming the subject name field is 'name'


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = '__all__'



class GateSerializer(serializers.ModelSerializer):
    brochure=FileSerializer(source='brochure_file_id')
    contact=FileSerializer(source='contact_file_id')

    class Meta:
        model = Gate
        fields = ['contact',  'brochure', 'reg_file_link'] 

class BundleSerializer(serializers.ModelSerializer):
    brochure=FileSerializer(source='brochure_file_id')
    contact=FileSerializer(source='contact_file_id')
    class Meta:
        model = Bundle
        fields = ['contact', 'brochure', 'reg_file_link']



class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

# class DemoClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DemoClass
#         fields = '__all__'
