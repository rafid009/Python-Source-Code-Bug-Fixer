import numpy as np 

def function(x):

	g5 = x
	k6 = x
	paths = []
	try:
		if x > 0:
			k6 = 9-k6
			k6 = x-g5
			paths.append(1)
		else:
			k6 = 5/g5
			x = x-7
			paths.append(2)
		if g5 <= 6:
			g5 = g5/9
			k6 = 6+9
			paths.append(3)
		else:
			k6 = k6-6
			x = 9/2
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))