import socket
import ResponseInterpreter

'''
This is a Python API to communicate with CasparCG Server using AMCP.
Currently, for the 20th convocation, we are only implementing some rudimentary functions here.
In future, we will work to clean this up, and build an amazing Python API for CasparCG.
'''
class CasparServer:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.ip,self.port))

	def send(command): 
		s.sendall(command)

	def _read_until(delimiter):
		msg = ""
		while not msg.endswith(delimiter):
			msg += s.recv(1).decode('utf-8')
		lines = msg.splitlines()
		ret = []
		for l in lines:
			if len(l):
				ret.append(l)
		return ret

	def read():
		response = read_until("\r\n")
		# ResponseInterpreter lets us know how to proceed
		# Caspar's way of sending information is a bit vague
		# It does not have a delimiter to indicate the end of the server's response
		to_do = ResponseInterpreter.interpret_response(response)
		if to_do[1]:
			response.extend(read_until(to_do[2]))
		return response

	'''
	Play's the given animation
	template_name is relative to the template-path defined in Caspar CG Config file.
	data is a dict of key-value pairs.
	'''
	def cgplay(template_name,data):
		cg_add_cmd = 'CG 1-10 ADD 10 "'+template_name+'" 1 '
		cg_add_cmd = '''
			<templateData>
				<componentData id=\\\"{0}\\\">
					<data id=\\\"text\\\" value=\\\"{1}\\\"/>
				</componentData>
				<componentData id=\\\"{2}\\\">
					<data id=\\\"text\\\" value=\\\"{3}\\\"/>
				</componentData>
			</templateData> 
			'''.format('Name',data{'name'},'Degree',data{'degree'})
		cg_add_cmd += '\r\n'
		send(socket, cg_add_cmd.encode('utf-8'))
		response = read(socket)
		return(cg_add_cmd,response)

	'''
	Stop's the current animation. 
	This is different from remove,
		in that it gives a chance for animation to play 'outro' before being removed
	'''
	def cgstop():
		cg_stop_cmd = 'CG 1-10 STOP 10'
		send(socket, cg_add_cmd.encode('utf-8'))
		response = read(socket)
		return(cg_add_cmd,response)
			



