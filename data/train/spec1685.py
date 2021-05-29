import numpy as np 

def function(x):

	x9 = 7
	a6 = x
	paths = []
	try:
		if a6 < 1:
			a6 = a6*5
			x = x*4
			x9 = x9+4
			paths.append(1)
		else:
			x9 = a6+a6
			a6 = a6*a6
			paths.append(2)
		if x9 >= 3:
			x9 = x9-9
			paths.append(3)
		else:
			a6 = a6/7
			a6 = 0*2
			x = x/3
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))