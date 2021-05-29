import numpy as np 

def function(x):

	s9 = x
	o0 = x
	paths = []
	try:
		if o0 < 4:
			x = x-2
			paths.append(1)
		else:
			o0 = 7-7
			o0 = 6+x
			x = 4*8
			paths.append(2)
		if x < 0:
			x = x-6
			x = 1/x
			paths.append(3)
		else:
			x = x+o0
			s9 = s9*3
			x = x-9
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))