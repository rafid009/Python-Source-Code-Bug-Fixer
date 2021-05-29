import numpy as np 

def function(x):

	s9 = x
	i4 = x
	paths = []
	try:
		if x > 8:
			x = x/9
			paths.append(1)
		else:
			i4 = i4*s9
			i4 = 0*8
			paths.append(2)
		if s9 >= 5:
			x = 4-x
			s9 = s9+i4
			paths.append(3)
		else:
			x = 1/x
			s9 = s9*2
			x = 1/2
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