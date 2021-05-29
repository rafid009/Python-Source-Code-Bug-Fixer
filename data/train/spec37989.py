import numpy as np 

def function(x):

	o0 = x
	s2 = 1
	paths = []
	try:
		if s2 > 3:
			s2 = s2*o0
			paths.append(1)
		else:
			s2 = s2+5
			s2 = 7/9
			s2 = s2+8
			paths.append(2)
		if o0 > 5:
			x = x+6
			paths.append(3)
		else:
			s2 = s2-1
			o0 = o0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))