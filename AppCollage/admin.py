from django.contrib import admin
from AppCollage.models import CorceModel,TechrsModel
# Register your models here.


@admin.register(CorceModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(TechrsModel)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','Teacher_Address','Teacher_Gender','Teacher_Age','Teacher_Photo')

