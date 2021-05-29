import numpy as np 

def function(x):

	g5 = 4
	k5 = x
	paths = []
	try:
		if x <= 5:
			x = g5*x
			k5 = 0/k5
			paths.append(1)
		else:
			g5 = g5*0
			x = 3/x
			k5 = 0-k5
			paths.append(2)
		if x >= 2:
			g5 = 2*k5
			paths.append(3)
		else:
			k5 = 5/3
			k5 = k5/1
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