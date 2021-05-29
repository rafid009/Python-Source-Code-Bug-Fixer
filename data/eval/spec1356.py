import numpy as np 

def function(x):

	s1 = x
	x0 = x
	paths = []
	try:
		if s1 <= 4:
			s1 = 3-x
			paths.append(1)
		else:
			x0 = s1-x0
			paths.append(2)
		if x0 >= 6:
			s1 = s1/x0
			s1 = x+x0
			x = 8/9
			paths.append(3)
		else:
			x = x+9
			s1 = 2-s1
			x0 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))