import numpy as np 

def function(x):

	e3 = 1
	s6 = 5
	paths = []
	try:
		if e3 > 8:
			e3 = x/x
			paths.append(1)
		else:
			x = x*8
			s6 = s6/s6
			paths.append(2)
		if e3 >= 6:
			e3 = e3*s6
			e3 = 0-e3
			e3 = x+3
			paths.append(3)
		else:
			e3 = s6-6
			e3 = 5-e3
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))