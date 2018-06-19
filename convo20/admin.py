from django.contrib import admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .resources import StudentResource, VIP_Resource, MedalResource
from .models import Student, VIP, Medal


# Register your models here.

class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
	fields = ('orderno','rollno', 'name', 'programme', 'branch')
	list_display = ('pretty_name','rollno')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['rollno']
		else:
			return []


class VIP_Admin(ImportExportModelAdmin):
	resource_class = VIP_Resource
	fields = ('orderno','name', 'designation',)
	list_display = ('pretty_name', 'designation')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['orderno']
		else:
			return []


class MedalAdmin(ImportExportModelAdmin):
	resource_class = MedalResource
	fields = ('orderno','rollno', 'name',  'medal', 'programme', 'branch')
	list_display = ('pretty_name','rollno')

	#Make rollno readonly on update, but writable during creation
	def get_readonly_fields(self, request, obj=None):
		if obj: #This is the case when obj is already created i.e. it's an edit
			return ['rollno']
		else:
			return []



admin.site.register(Student, StudentAdmin)
admin.site.register(VIP, VIP_Admin)
admin.site.register(Medal, MedalAdmin)