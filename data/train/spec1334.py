import numpy as np 

def function(x):

	s9 = x
	e2 = 8
	paths = []
	try:
		if e2 < 0:
			x = x/s9
			e2 = 3-7
			x = e2-5
			paths.append(1)
		else:
			e2 = s9+e2
			x = x+e2
			s9 = 1-s9
			paths.append(2)
		if s9 >= 3:
			s9 = s9+5
			s9 = s9+e2
			x = x+x
			paths.append(3)
		else:
			s9 = x-4
			s9 = x-5
			s9 = 2/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))