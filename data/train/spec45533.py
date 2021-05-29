import numpy as np 

def function(x):

	b0 = 1
	s4 = x
	paths = []
	try:
		if x > 8:
			b0 = x*b0
			s4 = 0/s4
			s4 = b0+3
			paths.append(1)
		else:
			b0 = 9-s4
			b0 = b0*8
			b0 = b0+1
			paths.append(2)
		if x >= 5:
			s4 = s4-4
			paths.append(3)
		else:
			s4 = s4+3
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