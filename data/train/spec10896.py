import numpy as np 

def function(x):

	s6 = x
	i0 = x
	paths = []
	try:
		if x < 0:
			s6 = s6*1
			s6 = s6*s6
			x = i0+x
			paths.append(1)
		else:
			x = 2+i0
			x = 9*x
			paths.append(2)
		if s6 > 2:
			x = x+8
			i0 = 3+i0
			paths.append(3)
		else:
			i0 = i0*1
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