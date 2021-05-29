import numpy as np 

def function(x):

	o6 = 9
	s1 = x
	paths = []
	try:
		if s1 < 6:
			o6 = 6*o6
			s1 = s1-0
			paths.append(1)
		else:
			x = s1+x
			o6 = s1-2
			o6 = o6/2
			paths.append(2)
		if o6 < 5:
			o6 = x-o6
			o6 = o6-7
			s1 = s1-x
			paths.append(3)
		else:
			s1 = s1-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))