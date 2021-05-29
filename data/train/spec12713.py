import numpy as np 

def function(x):

	o5 = x
	s0 = 0
	paths = []
	try:
		if s0 <= 9:
			o5 = s0+o5
			paths.append(1)
		else:
			x = x/3
			o5 = 0/6
			s0 = s0*3
			paths.append(2)
		if s0 >= 4:
			s0 = s0-7
			x = x/3
			paths.append(3)
		else:
			x = 2+x
			o5 = o5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))