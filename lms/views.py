from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer, CourseLessonSerializer
from users.permissions import IsOwner


class CourseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        """only owners courses list will appear"""
        if self.action in ["retrieve", "list"]:
            return Course.objects.filter(is_public=True)
        else:
            return Course.objects.filter(is_public=False)

    def perform_create(self, serializer):
        """auto adding to course its owner who create course"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_serializer_class(self):
        """if creating then CourseSerializer others(CRUD) CourseLessonSerializer"""
        if self.action == 'post':
            return CourseSerializer
        return CourseLessonSerializer

    def get_permissions(self):
        """setting permission for moders to update and retrieve only, moders cant create or delete"""
        if self.action in ["update", "retrieve", "partial_update"]:
            self.permission_classes = (IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """auto adding to lesson its owner who create lesson"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        """only owners list will appear"""
        user = self.request.user
        return Lesson.objects.filter(owner=user)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
