import numpy as np 

def function(x):

	s6 = 1
	i6 = 3
	paths = []
	try:
		if s6 < 1:
			i6 = i6-3
			i6 = x*4
			paths.append(1)
		else:
			i6 = s6+8
			i6 = x-8
			paths.append(2)
		if x >= 8:
			x = 9-s6
			x = s6-x
			x = s6-i6
			paths.append(3)
		else:
			i6 = i6+8
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