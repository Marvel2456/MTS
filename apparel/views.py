from django.shortcuts import render
from django.http import Http404
from . models import Customer, Male, Female, Staff, Tailor, RegisterIn, RegisterOut, Entry, Appointments, Clothes, Style
from . serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

# Create your views here.

class CustomerList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MaleList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        male = Male.objects.all()
        serializer = MaleSerializer(male, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MaleDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Male.objects.get(pk=pk)
        except Male.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        male = self.get_object(pk)
        serializer = MaleSerializer(male)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        male = self.get_object(pk)
        serializer = MaleSerializer(male, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        male = self.get_object(pk)
        male.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FemaleList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        female = Female.objects.all()
        serializer = FemaleSerializer(female, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FemaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FemaleDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Female.objects.get(pk=pk)
        except Female.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        female = self.get_object(pk)
        serializer = FemaleSerializer(female)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        female = self.get_object(pk)
        serializer = FemaleSerializer(female, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        female = self.get_object(pk)
        female.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StaffList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StaffDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        staff = self.get_object(pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TailorList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        tailor = Tailor.objects.all()
        serializer = TailorSerializer(tailor, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TailorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TailorDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Tailor.objects.get(pk=pk)
        except Tailor.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        tailor = self.get_object(pk)
        serializer = TailorSerializer(tailor)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        tailor = self.get_object(pk)
        serializer = TailorSerializer(tailor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        tailor = self.get_object(pk)
        tailor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AppointmentList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        appointment = Appointments.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AppointmentDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Appointments.objects.get(pk=pk)
        except Appointments.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ClotheList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        clothe = Clothes.objects.all()
        serializer = ClotheSerializer(clothe, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClotheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ClotheDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Clothes.objects.get(pk=pk)
        except Clothes.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        clothe = self.get_object(pk)
        serializer = ClotheSerializer(clothe)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        clothe = self.get_object(pk)
        serializer = ClotheSerializer(clothe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        clothe = self.get_object(pk)
        clothe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StyleList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        style = Style.objects.all()
        serializer = StyleSerializer(style, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClotheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StyleDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Style.objects.get(pk=pk)
        except Style.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        style = self.get_object(pk)
        style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterInList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        regin = RegisterIn.objects.all()
        serializer = RegisterInSerializer(regin, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegisterInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegisterInDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return  RegisterIn.objects.get(pk=pk)
        except RegisterIn.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        regin = self.get_object(pk)
        serializer = RegisterInSerializer(regin)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        regin = self.get_object(pk)
        serializer = RegisterInSerializer(regin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        regin = self.get_object(pk)
        regin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterOutList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        regout = RegisterOut.objects.all()
        serializer = RegisterOutSerializer(regout, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegisterOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegisterOutDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return RegisterOut.objects.get(pk=pk)
        except RegisterOut.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        regout = self.get_object(pk)
        serializer = RegisterOutSerializer(regout)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        regout = self.get_object(pk)
        serializer = RegisterOutSerializer(regout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        regout = self.get_object(pk)
        regout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EntryList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        entry = Entry.objects.all()
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EntryDetail(APIView):
    
    permission_classes = [IsAdminUser]
    
    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    

        
    
        
