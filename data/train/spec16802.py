import numpy as np 

def function(x):

	s7 = x
	e6 = x
	paths = []
	try:
		if e6 <= 4:
			x = e6/3
			s7 = s7/8
			paths.append(1)
		else:
			e6 = e6*e6
			e6 = x-e6
			x = s7/9
			paths.append(2)
		if e6 <= 8:
			e6 = e6+8
			paths.append(3)
		else:
			e6 = 9+e6
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