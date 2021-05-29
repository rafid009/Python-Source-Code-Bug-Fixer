import numpy as np 

def function(x):

	s6 = 8
	v8 = x
	paths = []
	try:
		if s6 > 8:
			x = x*2
			v8 = v8*4
			x = v8*x
			paths.append(1)
		else:
			x = x*2
			v8 = s6/5
			paths.append(2)
		if s6 > 5:
			v8 = v8/7
			x = x-0
			paths.append(3)
		else:
			s6 = s6+3
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))