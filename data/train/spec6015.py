import numpy as np 

def function(x):

	g0 = x
	s7 = 2
	paths = []
	try:
		if x >= 6:
			x = x-g0
			s7 = s7+0
			paths.append(1)
		else:
			x = g0/x
			s7 = 6*x
			paths.append(2)
		if g0 > 2:
			x = x/5
			paths.append(3)
		else:
			x = x*3
			x = 7/4
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))