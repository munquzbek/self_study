from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer, CourseLessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

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


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """auto adding to lesson its owner who create lesson"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
