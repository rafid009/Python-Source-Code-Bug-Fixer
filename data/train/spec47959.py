import numpy as np 

def function(x):

	s2 = 4
	s5 = x
	paths = []
	try:
		if x < 8:
			s5 = 3+0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x < 4:
			s2 = x-s2
			s2 = s2-5
			s2 = 1+s2
			paths.append(3)
		else:
			x = s5+s5
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