import numpy as np 

def function(x):

	o0 = 6
	s6 = 1
	paths = []
	try:
		if o0 <= 6:
			o0 = x*s6
			paths.append(1)
		else:
			s6 = s6/3
			s6 = x+s6
			x = 1+x
			paths.append(2)
		if o0 >= 0:
			x = x*o0
			s6 = s6*5
			paths.append(3)
		else:
			s6 = s6*7
			o0 = 0*o0
			o0 = o0+o0
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