from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class SessionYearModel(models.Model):
     id=models.AutoField(primary_key=True)
     session_start_year=models.DateField()
     session_end_year=models.DateField()
     object = models.Manager()

class CustomUser(AbstractUser):
    user_type_data=((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type=models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


# Para el staff
class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


# Para los cursos
class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255, unique=True, blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


# Para las materias de los cursos
class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


# Estudiantes
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField(null=True, blank=True)
    address=models.TextField()
    course_id=models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    session_year_id=models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


# Para la asistencia 
class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    session_year_id=models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    objects=models.Manager()

# para los reportes de asistencias
class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

# para cuando el estudiante se va
class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


# para cuando el staff se retira
class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


# modelo de feedback para el estudiante
class FeedBackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

# modelo de feedback para el staff
class FeedBackStaffs(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class NotificationStaffs(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

# Signals o señales
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(admin=instance)
        if instance.user_type==3:
            Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), 
                                    session_year_id=SessionYearModel.object.get(id=1), address="", profile_pic="", gender="")

@receiver(post_save, sender=CustomUser)    
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
            instance.adminhod.save()
    if instance.user_type==2:
            instance.staffs.save()
    if instance.user_type==3:
            instance.students.save()
            