import numpy as np 

def function(x):

	r5 = x
	s9 = x
	paths = []
	try:
		if x >= 1:
			x = 4-2
			paths.append(1)
		else:
			x = x-9
			r5 = r5+9
			paths.append(2)
		if s9 > 8:
			x = r5/r5
			r5 = r5+7
			s9 = 0/2
			paths.append(3)
		else:
			s9 = s9*9
			s9 = x*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))