from import_export import resources, fields
from .models import Student

class StudentResource(resources.ModelResource):
	rollno 				= fields.Field(attribute = 'rollno', column_name = 'Roll Number') #Ensure rollno cannot be imported
	name 				= fields.Field(attribute = 'name', column_name = 'Name')
	programme 			= fields.Field(attribute = 'programme', column_name = 'Programme')
	branch 				= fields.Field(attribute = 'branch', column_name = 'Branch')

	class Meta:
		model = Student
		skip_unchanged = True #Dont import unchanged fields
		fields = ('rollno', 'name', 'programme', 'branch') #Whitelist fields to be import/exported
		export_order = ('rollno', 'name', 'programme', 'branch') #Needed because we are using column_name(s)
		import_id_fields = ('rollno',) #Use rollno as primary key while importing
