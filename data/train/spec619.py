import numpy as np 

def function(x):

	x6 = 4
	j0 = x
	paths = []
	try:
		if x <= 7:
			x = x/6
			paths.append(1)
		else:
			x = x+j0
			x = x6+x
			paths.append(2)
		if j0 >= 3:
			x6 = 4*9
			j0 = 8/6
			paths.append(3)
		else:
			x6 = 7+x6
			j0 = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))