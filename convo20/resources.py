from import_export import resources, fields
from .models import Student

class StudentResource(resources.ModelResource):
	orderno 			= fields.Field(attribute = 'orderno', column_name = 'Order Number') #Ensure rollno cannot be imported
	rollno 				= fields.Field(attribute = 'rollno', column_name = 'Roll Number') #Ensure rollno cannot be imported
	name 				= fields.Field(attribute = 'name', column_name = 'Name')
	programme 			= fields.Field(attribute = 'programme', column_name = 'Programme')
	branch 				= fields.Field(attribute = 'branch', column_name = 'Branch')

	class Meta:
		model = Student
		skip_unchanged = True #Dont import unchanged fields
		fields = ('orderno','rollno', 'name', 'programme', 'branch') #Whitelist fields to be import/exported
		export_order = ('orderno','rollno', 'name', 'programme', 'branch') #Needed because we are using column_name(s)
		import_id_fields = ('rollno',) #Use rollno as primary key while importing
