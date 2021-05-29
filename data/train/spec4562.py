import numpy as np 

def function(x):

	a1 = x
	s8 = 1
	x = x
	paths = []
	try:
		if x >= 3:
			a1 = 3+5
			a1 = x*3
			s8 = 3*2
			paths.append(1)
		else:
			x = 7+4
			paths.append(2)
		if x >= 3:
			x = a1+8
			s8 = s8/2
			paths.append(3)
		else:
			a1 = 3*a1
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))