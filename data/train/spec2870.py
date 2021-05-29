import numpy as np 

def function(x):

	s5 = x
	a5 = 2
	paths = []
	try:
		if x < 6:
			a5 = a5*5
			x = a5*x
			paths.append(1)
		else:
			a5 = a5/x
			s5 = 2-2
			paths.append(2)
		if s5 >= 9:
			x = x-a5
			paths.append(3)
		else:
			x = x*a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))