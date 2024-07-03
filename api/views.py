from .models import Student
from .serializaers import StudentSerializer
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# views with separate mixins
# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
# class StudentRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
# class StudentDelete(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# list and create
class LCStudentApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
# retieve,update and delete
class RUDStudentApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
# concrete view class
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRU(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
