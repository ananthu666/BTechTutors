from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'userdata', UserdataViewSet)
router.register(r'btech', BtechViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'depsubrel', DepSubRelViewSet)
router.register(r'file', FileViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'questionpaper', QuestionPaperViewSet)

router.register(r'gate', GateViewSet)
router.register(r'bundle', BundleViewSet)

router.register(r'internship', InternshipViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'notification', NotificationViewSet)

router.register(r'get_subjects', GetSubjectViewSet,basename='get_subjects')
router.register(r'get_contents', GetContentsViewSet,basename='get_contents')
router.register(r'get_notes', GetNotesViewSet,basename='get_notes')

router.register(r'get_gate', GetGateViewSet,basename='get_gate')
router.register(r'get_bundle', GetBundleViewSet,basename='get_bundle')
router.register(r'get_internship', GetInternshipViewSet,basename='get_internship')
router.register(r'get_project', GetProjectViewSet,basename='get_project')
router.register(r'get_notification', GetNotificationViewSet,basename='get_notification')

urlpatterns = [
    path('', include(router.urls)),
]
