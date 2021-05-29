import numpy as np 

def function(x):

	s1 = x
	r7 = 2
	paths = []
	try:
		if x <= 3:
			x = x*6
			r7 = r7-s1
			paths.append(1)
		else:
			r7 = s1*x
			s1 = 6-r7
			paths.append(2)
		if s1 < 6:
			x = 2-7
			paths.append(3)
		else:
			x = x-2
			x = x/r7
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