import numpy as np 

def function(x):

	a0 = x
	s8 = x
	paths = []
	try:
		if x >= 5:
			s8 = a0+a0
			x = 5/s8
			paths.append(1)
		else:
			s8 = a0/s8
			a0 = 2*6
			x = x*7
			paths.append(2)
		if a0 < 7:
			x = x+1
			x = x/1
			paths.append(3)
		else:
			x = x+x
			a0 = a0+8
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