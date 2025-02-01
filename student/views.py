from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import constants as messages
from django.contrib import messages
from .forms import StudentForm
from .models import Student_Info
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
'''def home(request):
    students = Student_Info.objects.all().order_by('sID')

    return render(request, 'student_list.html', {'students' : students} )'''
class StudentListView(ListView):
    model = Student_Info
    template_name = 'student_list.html'
    context_object_name = 'students'
    ordering = ['sID']

"""def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('home')

    else:
        form = StudentForm()

    return render(request, 'add.html',{'form' : form})"""
class AddNew(CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('home')
    template_name = 'add.html'
    context_object_name = 'form'


'''def update(request, sID):
    student = Student_Info.objects.get(sID = sID)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated successfully!")
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update.html', {'form': form})'''
class Update(UpdateView):
    model = Student_Info
    form_class = StudentForm
    pk_url_kwarg = 'sID'
    template_name = 'add.html'
    context_object_name = 'form'

    def form_valid(self, form):
        messages.success(self.request, "Student details updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


'''def delete(request, sID):
    student = Student_Info.objects.get(sID = sID)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('home')'''
class Delete(DeleteView):
    model = Student_Info
    template_name = 'delete.html'  # Confirmation template
    pk_url_kwarg = 'sID'  # To match the sID in the URL
    context_object_name = 'student'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')



'''def search(request):
    query = request.GET.get('query', '')  
    #results = Student_Info.objects.filter(name__icontains=query) 
    results = Student_Info.objects.filter(
    Q(name__icontains=query) | 
    Q(sID__icontains=query) | 
    Q(phone_number__icontains=query) | 
    Q(course__icontains=query)
) 
    return render(request, 'student_list.html', {'students' : results})'''

class Search(ListView):
    model = Student_Info
    template_name = 'student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('query', '')  # Extracts the search term
        if query:
            return Student_Info.objects.filter(
                Q(name__icontains=query) |
                Q(sID__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(course__icontains=query)
            )
        else:
            return Student_Info.objects.all()  # Shows all students if no query

