import numpy as np 

def function(x):

	b4 = 3
	s9 = x
	paths = []
	try:
		if x >= 2:
			x = 1+2
			b4 = 3/x
			s9 = s9+s9
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x <= 9:
			s9 = s9/2
			x = b4*s9
			paths.append(3)
		else:
			s9 = s9*b4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))