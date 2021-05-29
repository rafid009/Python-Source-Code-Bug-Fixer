import numpy as np 

def function(x):

	e2 = 1
	s9 = x
	paths = []
	try:
		if e2 <= 7:
			x = x/6
			paths.append(1)
		else:
			e2 = e2+x
			s9 = s9-s9
			paths.append(2)
		if x <= 9:
			x = x-s9
			paths.append(3)
		else:
			s9 = s9*6
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))