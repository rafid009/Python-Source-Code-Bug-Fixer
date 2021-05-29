import numpy as np 

def function(x):

	i3 = 6
	x9 = 7
	paths = []
	try:
		if x9 >= 4:
			x9 = x9/x
			i3 = i3-5
			x9 = x9+i3
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if x9 > 0:
			x = 8*x
			x9 = 3*7
			x9 = 4+x9
			paths.append(3)
		else:
			x9 = x9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))