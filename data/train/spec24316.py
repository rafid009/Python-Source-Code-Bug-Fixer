import numpy as np 

def function(x):

	a0 = x
	s2 = 4
	paths = []
	try:
		if x < 5:
			x = s2/x
			x = x/s2
			paths.append(1)
		else:
			s2 = s2*1
			x = x/3
			a0 = x*7
			paths.append(2)
		if x > 4:
			x = 0-x
			x = x+a0
			paths.append(3)
		else:
			a0 = 3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))