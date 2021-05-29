import numpy as np 

def function(x):

	s5 = 9
	f6 = x
	paths = []
	try:
		if x < 0:
			f6 = 8/x
			s5 = s5/9
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if s5 < 3:
			s5 = x/s5
			x = 8*x
			paths.append(3)
		else:
			x = x*4
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