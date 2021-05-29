import numpy as np 

def function(x):

	s2 = x
	e6 = x
	paths = []
	try:
		if x <= 5:
			x = s2*6
			e6 = 3*e6
			paths.append(1)
		else:
			s2 = s2-7
			x = 9/2
			paths.append(2)
		if s2 >= 5:
			x = 8/x
			s2 = 1+8
			x = x-2
			paths.append(3)
		else:
			e6 = e6*1
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))