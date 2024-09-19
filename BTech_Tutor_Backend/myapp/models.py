from django.db import models

class Userdata(models.Model):
    name = models.CharField(max_length=255)
    phno = models.CharField(max_length=15)

class Btech(models.Model):
    # year = models.IntegerField()set it as primary key
    year = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return f"{self.year}"

class Department(models.Model):
    name = models.CharField(max_length=255)
    maxsem = models.IntegerField()
    # subid = models.ForeignKey('Subject', on_delete=models.CASCADE)
    btech_id = models.ForeignKey('Btech', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Subject(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    syllabusfile_id = models.ForeignKey('File', related_name='syllabus_files', on_delete=models.CASCADE)
    # fullcourse_id = models.ForeignKey('File', related_name='fullcourse_files', on_delete=models.CASCADE)
    fullcourse_id = models.CharField(max_length=255)
    # democlasslink = models.ForeignKey('DemoClass', on_delete=models.CASCADE,default='')    
    demolink = models.URLField(default='')
    courselink=models.URLField( default='')


    def __str__(self):
        return self.code + " - " + self.name    

class DepSubRel(models.Model):
    # name = models.CharField(max_length=255)
    subjectid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    semnum = models.IntegerField()
    def __str__(self):
        return self.subjectid.name + " - " + self.depid.name

class File(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    fileblob = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name
    

class Notes(models.Model):
    module = models.IntegerField()
    subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return f"MOD{self.module} " + "- "f"{self.subid}"

class QuestionPaper(models.Model):
    # module = models.IntegerField()
    subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

# Gate models
# class GateDEP(models.Model):
#     depname = models.CharField(max_length=255)

class Gate(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    brochure_file_id = models.ForeignKey(File, related_name='gate_brochures', on_delete=models.CASCADE)
    contact_file_id = models.ForeignKey(File, related_name='gate_contacts', on_delete=models.CASCADE)
    # reg_file_id = models.ForeignKey(File, related_name='gate_regs', on_delete=models.CASCADE)
    reg_file_link= models.URLField(default='')
    def __str__(self):
        return self.depid.name

class Bundle(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    brochure_file_id = models.ForeignKey(File, related_name='bundle_brochures', on_delete=models.CASCADE)
    contact_file_id = models.ForeignKey(File, related_name='bundle_contacts', on_delete=models.CASCADE)
    # reg_file_id = models.ForeignKey(File, related_name='bundle_regs', on_delete=models.CASCADE)
    reg_file_link= models.URLField(default='')
    def __str__(self):
        return self.depid.name
# Internship models
# class InternDep(models.Model):
#     depname = models.CharField(max_length=255)

class Internship(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_desc = models.TextField()
    g_from_link = models.URLField()
    def __str__(self):
        return self.depid.name + self.course_name

# Project models
class Project(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    topicname = models.CharField(max_length=255)
    topic_desc = models.TextField()
    g_from_link = models.URLField()
    def __str__(self):
        return self.depid.name + self.topicname

class Notification(models.Model):
    heading = models.CharField(max_length=255)
    desc = models.TextField()
    files = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.heading

# class DemoClass(models.Model):
    
#     sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
