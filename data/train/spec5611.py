import numpy as np 

def function(x):

	s7 = x
	r2 = 0
	paths = []
	try:
		if s7 <= 5:
			s7 = s7-7
			r2 = x*3
			x = 0*s7
			paths.append(1)
		else:
			x = 7+x
			x = x*s7
			x = 8+s7
			paths.append(2)
		if x >= 8:
			r2 = 7+r2
			s7 = x/s7
			paths.append(3)
		else:
			x = 6*x
			x = 4+r2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))