from django.contrib import admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import StudentResource, DignitaryResource, MedalResource
from .models import Student, Dignitary, Medal


# Register your models here.

class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
	fields = ('orderno','rollno', 'name', 'programme', 'branch')
	list_display = ('orderno','rollno', 'pretty_name', 'programme', 'branch')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['rollno']
		else:
			return []


class DignitaryAdmin(ImportExportModelAdmin):
	resource_class = DignitaryResource
	fields = ('orderno','name','designation')
	list_display = ('orderno','name','designation')


class MedalAdmin(ImportExportModelAdmin):
	resource_class = MedalResource
	fields = ('orderno','rollno', 'name',  'medal', 'programme', 'branch')
	list_display = ('orderno','rollno', 'pretty_name',  'medal', 'programme', 'branch')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['rollno']
		else:
			return []



admin.site.register(Student, StudentAdmin)
admin.site.register(Dignitary, DignitaryAdmin)
admin.site.register(Medal, MedalAdmin)