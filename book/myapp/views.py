from django.shortcuts import render, redirect
from .forms import FaculityForm, KafedraForm, SubjectForm, TeacherForm, GroupForm
from .models import Faculity, Kafedra, Subject, Teacher, Group, Student


def home_page(request):
    return render(request, "index.html")


def Faculity_create(request):
    model = Faculity()
    form = FaculityForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("faculity_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculity/form.html", ctx)


def Faculity_list(requset):
    faculities = Faculity.objects.all()
    ctx = {
        "faculities": faculities
    }
    return render(requset, "faculity/list.html", ctx)


def Faculity_edit(request, pk):
    model = Faculity.objects.get(pk=pk)
    form = FaculityForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("faculity_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculity/form.html", ctx)


def Faculity_delete(request, pk):
    model = Faculity.objects.get(pk=pk)
    model.delete()
    return redirect("Faculity_list")


def Kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("kafedra_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "kafedra/form.html", ctx)


def Kafedra_list(requset):
    kafedras = Kafedra.objects.all()
    ctx = {
        "kafedras": kafedras
    }
    return render(requset, "kafedra/list.html", ctx)


def Kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("kafedra_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "kafedra/form.html", ctx)


def Kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect("kafedra_list")


def Subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("subject_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "subject/form.html", ctx)


def Subject_list(requset):
    subject = Subject.objects.all()
    ctx = {
        "subject": subject
    }
    return render(requset, "subject/list.html", ctx)


def Subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("subject_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "subject/form.html", ctx)


def Subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect("subject_list")


def Teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("teacher_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


def Teacher_list(requset):
    teachers = Teacher.objects.all()
    ctx = {
        "teachers": teachers
    }
    return render(requset, "teacher/list.html", ctx)


def Teacher_edit(request, pk):
    teachers = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=teachers)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    ctx = {
        "teachers": teachers,
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


def Teacher_delete(request, pk):
    teachers = Kafedra.objects.get(pk=pk)
    teachers.delete()
    return redirect("teacher_list")


def Group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("group_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


def Group_list(requset):
    groups = Group.objects.all()
    ctx = {
        "groups": groups
    }
    return render(requset, "group/list.html", ctx)


def Group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("group_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


def Group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect("group_list")


def Student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, instance=model)
    if request.POST:
        print("A", form)
        if form.is_valid():
            print("B", form)
            form.save()
            return redirect("student_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "student/form.html", ctx)


def Student_list(requset):
    students = Student.objects.all()
    ctx = {
        "students": students
    }
    return render(requset, "student/list.html", ctx)


def Student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("student_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "student/form.html", ctx)


def Student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect("student_list")
