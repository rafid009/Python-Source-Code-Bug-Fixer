import numpy as np 

def function(x):

	s9 = x
	e9 = 2
	paths = []
	try:
		if x >= 6:
			s9 = 8-x
			x = 8-x
			paths.append(1)
		else:
			x = s9/x
			x = 8-0
			s9 = 8-s9
			paths.append(2)
		if e9 < 4:
			e9 = e9+7
			s9 = s9+0
			paths.append(3)
		else:
			s9 = 6+s9
			e9 = e9*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))