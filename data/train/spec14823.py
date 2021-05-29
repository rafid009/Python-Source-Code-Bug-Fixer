import numpy as np 

def function(x):

	s6 = 6
	e6 = x
	paths = []
	try:
		if s6 >= 7:
			x = 9/x
			paths.append(1)
		else:
			s6 = e6+e6
			paths.append(2)
		if e6 <= 5:
			s6 = 6+s6
			paths.append(3)
		else:
			x = 1-e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))