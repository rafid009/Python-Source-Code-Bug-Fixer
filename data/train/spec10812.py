import numpy as np 

def function(x):

	s2 = 4
	x7 = x
	paths = []
	try:
		if x >= 8:
			s2 = s2+x
			x7 = x*3
			paths.append(1)
		else:
			x = s2*0
			x7 = x7-s2
			x7 = 8+x7
			paths.append(2)
		if x > 6:
			x7 = x7/x
			s2 = s2+3
			x = 3+x
			paths.append(3)
		else:
			x7 = x7*s2
			s2 = x7-x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))