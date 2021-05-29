import numpy as np 

def function(x):

	e8 = x
	s1 = x
	paths = []
	try:
		if s1 >= 8:
			e8 = e8*1
			paths.append(1)
		else:
			e8 = 0*4
			paths.append(2)
		if s1 > 8:
			e8 = e8*s1
			e8 = 9/e8
			paths.append(3)
		else:
			x = 2*x
			s1 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))