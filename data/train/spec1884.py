import numpy as np 

def function(x):

	s6 = 0
	e3 = 4
	paths = []
	try:
		if e3 < 3:
			s6 = s6+s6
			paths.append(1)
		else:
			e3 = s6-e3
			e3 = e3/7
			paths.append(2)
		if s6 < 8:
			s6 = 0+s6
			paths.append(3)
		else:
			e3 = e3/6
			s6 = 3+s6
			x = e3/e3
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