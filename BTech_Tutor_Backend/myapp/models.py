from django.db import models

class Userdata(models.Model):
    name = models.CharField(max_length=255)
    phno = models.CharField(max_length=15)

class Btech(models.Model):
    year = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length=255)
    maxsem = models.IntegerField()
    subid = models.ForeignKey('Subject', on_delete=models.CASCADE)
    btech_id = models.ForeignKey(Btech, on_delete=models.CASCADE)

class Subject(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    syllabusfile_id = models.ForeignKey('File', related_name='syllabus_files', on_delete=models.CASCADE)
    fullcourse_id = models.ForeignKey('File', related_name='fullcourse_files', on_delete=models.CASCADE)

class DepSubRel(models.Model):
    type = models.CharField(max_length=255)
    subjectid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    semnum = models.IntegerField()

class File(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()

class Notes(models.Model):
    module = models.IntegerField()
    subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

class QuestionPaper(models.Model):
    module = models.IntegerField()
    subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

# Gate models
class GateDEP(models.Model):
    depname = models.CharField(max_length=255)

class Gate(models.Model):
    depid = models.ForeignKey(GateDEP, on_delete=models.CASCADE)
    brochure_file_id = models.ForeignKey(File, related_name='gate_brochures', on_delete=models.CASCADE)
    contact_file_id = models.ForeignKey(File, related_name='gate_contacts', on_delete=models.CASCADE)
    reg_file_id = models.ForeignKey(File, related_name='gate_regs', on_delete=models.CASCADE)

class Bundle(models.Model):
    depid = models.ForeignKey(GateDEP, on_delete=models.CASCADE)
    brochure_file_id = models.ForeignKey(File, related_name='bundle_brochures', on_delete=models.CASCADE)
    contact_file_id = models.ForeignKey(File, related_name='bundle_contacts', on_delete=models.CASCADE)
    reg_file_id = models.ForeignKey(File, related_name='bundle_regs', on_delete=models.CASCADE)

# Internship models
class InternDep(models.Model):
    depname = models.CharField(max_length=255)

class Internship(models.Model):
    depid = models.ForeignKey(InternDep, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_desc = models.TextField()
    g_from_link = models.URLField()

# Project models
class Project(models.Model):
    depid = models.ForeignKey(InternDep, on_delete=models.CASCADE)
    topicname = models.CharField(max_length=255)
    topic_desc = models.TextField()
    g_from_link = models.URLField()

class Notification(models.Model):
    heading = models.CharField(max_length=255)
    desc = models.TextField()
    files = models.CharField(max_length=255)

class DemoClass(models.Model):
    name = models.CharField(max_length=255)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    link = models.URLField()
