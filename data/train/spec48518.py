import numpy as np 

def function(x):

	a1 = x
	x9 = 0
	x = x
	paths = []
	try:
		if a1 >= 5:
			x = x+x
			paths.append(1)
		else:
			a1 = 7+2
			paths.append(2)
		if x9 < 9:
			x9 = 4*x9
			x9 = x9-6
			x = x+x9
			paths.append(3)
		else:
			x9 = x9/a1
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))