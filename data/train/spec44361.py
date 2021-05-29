import numpy as np 

def function(x):

	a9 = x
	x5 = x
	paths = []
	try:
		if x > 4:
			x = x/3
			x = x+4
			x5 = x5+7
			paths.append(1)
		else:
			a9 = 3/a9
			x5 = x*x
			paths.append(2)
		if a9 > 5:
			a9 = a9/a9
			a9 = 9*a9
			a9 = a9*8
			paths.append(3)
		else:
			a9 = x5+1
			a9 = x5-5
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