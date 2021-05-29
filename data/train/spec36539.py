import numpy as np 

def function(x):

	s9 = x
	b7 = 2
	paths = []
	try:
		if x >= 7:
			x = 6-x
			x = 3/x
			x = 1-s9
			paths.append(1)
		else:
			b7 = b7*s9
			b7 = 6/b7
			s9 = s9-0
			paths.append(2)
		if b7 >= 6:
			x = 1+x
			x = 7/x
			paths.append(3)
		else:
			s9 = s9-9
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