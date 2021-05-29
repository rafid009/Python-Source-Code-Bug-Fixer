import numpy as np 

def function(x):

	e4 = x
	s9 = x
	paths = []
	try:
		if x <= 3:
			s9 = s9-0
			x = x*e4
			paths.append(1)
		else:
			x = x/6
			e4 = e4*x
			paths.append(2)
		if s9 >= 5:
			e4 = 2-e4
			paths.append(3)
		else:
			e4 = 8+e4
			x = 8+0
			x = x-6
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		s9 = e4**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))