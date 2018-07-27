a = 10
b = 20

def outside():
	global a
	global b

	def inside():
		global a
		global b
		a = 1
		b = 2

		print "inside :", a, b

		return a+b

	inside()

	print "outside :", a, b

	return a+b
	
print outside()
