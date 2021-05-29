import numpy as np 

def function(x):

	x6 = x
	a6 = x
	paths = []
	try:
		if x6 < 9:
			x = 3*5
			x6 = x6-x
			x6 = x+a6
			paths.append(1)
		else:
			x = x*x
			x6 = x6-x6
			a6 = a6/a6
			paths.append(2)
		if x6 < 9:
			x6 = 1-x6
			x6 = 4+x6
			x6 = x6-2
			paths.append(3)
		else:
			x6 = x6*x6
			x = x*5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x6 = a6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))