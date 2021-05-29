import numpy as np 

def function(x):

	j0 = x
	s0 = x
	paths = []
	try:
		if s0 >= 5:
			x = x+6
			x = x+x
			j0 = j0/s0
			paths.append(1)
		else:
			s0 = s0-j0
			paths.append(2)
		if j0 <= 8:
			x = 7/x
			x = x/3
			paths.append(3)
		else:
			j0 = 9+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))