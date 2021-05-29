import numpy as np 

def function(x):

	g5 = 6
	k4 = 4
	paths = []
	try:
		if k4 >= 3:
			x = x+k4
			x = x*x
			x = 3-2
			paths.append(1)
		else:
			g5 = 6+g5
			k4 = 9-1
			x = 8+3
			paths.append(2)
		if g5 > 2:
			k4 = x+9
			x = x-6
			k4 = 5/k4
			paths.append(3)
		else:
			x = k4-4
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