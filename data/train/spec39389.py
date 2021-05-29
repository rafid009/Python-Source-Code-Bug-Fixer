import numpy as np 

def function(x):

	s4 = 6
	o4 = x
	paths = []
	try:
		if o4 < 0:
			o4 = o4+0
			s4 = s4+9
			o4 = o4-3
			paths.append(1)
		else:
			x = x-2
			s4 = s4*1
			s4 = 8*s4
			paths.append(2)
		if s4 < 0:
			x = x*s4
			paths.append(3)
		else:
			s4 = 1-s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))