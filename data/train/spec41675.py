import numpy as np 

def function(x):

	s1 = 3
	u0 = x
	paths = []
	try:
		if s1 <= 6:
			x = x-6
			paths.append(1)
		else:
			u0 = 7-u0
			paths.append(2)
		if x >= 8:
			s1 = s1-9
			x = x*7
			paths.append(3)
		else:
			s1 = 1*1
			x = x*1
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))