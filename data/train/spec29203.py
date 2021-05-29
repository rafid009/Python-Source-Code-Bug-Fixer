import numpy as np 

def function(x):

	s5 = x
	x2 = 1
	x = x
	paths = []
	try:
		if x2 > 5:
			x = x+2
			x2 = 7+x2
			paths.append(1)
		else:
			x2 = x2+x2
			paths.append(2)
		if x >= 2:
			x = 0/3
			paths.append(3)
		else:
			x = x/1
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