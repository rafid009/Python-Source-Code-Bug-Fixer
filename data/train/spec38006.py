import numpy as np 

def function(x):

	a6 = 4
	x6 = x
	paths = []
	try:
		if x6 >= 3:
			x6 = x6-x
			x6 = a6*0
			paths.append(1)
		else:
			a6 = 4+a6
			x = 0+x
			x6 = 0-x6
			paths.append(2)
		if x6 > 8:
			x6 = 3/8
			x6 = 3*x6
			x6 = 7+a6
			paths.append(3)
		else:
			a6 = x6-a6
			x6 = 8-x6
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