import numpy as np 

def function(x):

	e5 = 3
	s0 = 1
	paths = []
	try:
		if e5 > 6:
			s0 = e5*5
			paths.append(1)
		else:
			s0 = s0-2
			paths.append(2)
		if x < 3:
			e5 = e5+9
			paths.append(3)
		else:
			e5 = e5-x
			x = s0+x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))