import socket
from convo20.scripts import ResponseInterpreter
import re

'''
This is a Python API to communicate with CasparCG Server using AMCP.
Currently, for the 20th convocation, we are only implementing some rudimentary functions here.
In future, we will work to clean this up, and build an amazing Python API for CasparCG.
'''
class CasparServer:
	def __init__(self, ip, port, timeout=3):
		self.ip = ip
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.settimeout(timeout)
		self.socket.connect((self.ip,self.port))

	def send(self,command): 
		self.socket.sendall(command)

	def _read_until(self,delimiter):
		msg = ""
		while not msg.endswith(delimiter):
			msg += self.socket.recv(1).decode('utf-8')
		lines = msg.splitlines()
		ret = []
		for l in lines:
			if len(l):
				ret.append(l)
		return ret

	def read(self):
		response = self._read_until("\r\n")
		# ResponseInterpreter lets us know how to proceed
		# Caspar's way of sending information is a bit vague
		# It does not have a delimiter to indicate the end of the server's response
		to_do = ResponseInterpreter.interpret_response(response)
		if to_do[1]:
			response.extend(self._read_until(to_do[2]))
		return response

	'''
	Play's the given animation
	template_name is relative to the template-path defined in Caspar CG Config file.
	data is a dict of key-value pairs.
	'''
	def cgplay(self,template_name,data):
		flat_data = []
		for key,value in data.items():
			flat_data.extend([key,value])
		
		cg_add_cmd = 'CG 1-10 ADD 1 "'+template_name+'" 1 '
		cg_add_cmd += '''
			"
			<templateData>
				<componentData id=\\\"{0}\\\">
					<data id=\\\"text\\\" value=\\\"{1}\\\"/>
				</componentData>
				<componentData id=\\\"{2}\\\">
					<data id=\\\"text\\\" value=\\\"{3}\\\"/>
				</componentData>
			</templateData>
			"
			'''.format(*flat_data)
		cg_add_cmd = re.sub('(\n|\t)','',cg_add_cmd) # Remove \n and \t - they confuse the CasparCG Server
		cg_add_cmd += '\r\n'
		
		self.send(cg_add_cmd.encode('utf-8'))
		response = self.read()
		
		return(cg_add_cmd,response)

	'''
	Stops the current animation. 
	This is different from remove,
		in that it gives a chance for animation to play 'outro' before being removed
	'''
	def cgstop(self):
		cg_stop_cmd = 'CG 1-10 STOP 1\r\n'
		
		self.send(cg_stop_cmd.encode('utf-8'))
		response = self.read()
		
		return(cg_stop_cmd,response)
			
	'''
	Clears the video channel
	'''
	def cgclear(self):
		cg_clear_cmd = 'CLEAR 1\r\n'

		self.send(cg_clear_cmd.encode('utf-8'))
		response = self.read()
		
		return(cg_clear_cmd,response)