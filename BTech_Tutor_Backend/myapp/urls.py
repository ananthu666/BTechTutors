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
router.register(r'gate_dep', GateDEPViewSet)
router.register(r'gate', GateViewSet)
router.register(r'bundle', BundleViewSet)
router.register(r'interndep', InternDepViewSet)
router.register(r'internship', InternshipViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'democlass', DemoClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
