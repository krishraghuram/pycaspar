from django.contrib import admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import StudentResource
from .models import Student


# Register your models here.

class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
	fields = ('rollno', 'name', 'programme', 'branch')
	list_display = ('pretty_name','rollno')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['rollno']
		else:
			return []

admin.site.register(Student, StudentAdmin)