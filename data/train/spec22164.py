import numpy as np 

def function(x):

	k6 = 8
	s4 = 7
	paths = []
	try:
		if s4 > 3:
			k6 = 6+k6
			k6 = k6/4
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x > 0:
			x = x*2
			paths.append(3)
		else:
			k6 = k6+6
			x = x/2
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