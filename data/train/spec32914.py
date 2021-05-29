import numpy as np 

def function(x):

	j1 = 4
	k4 = x
	paths = []
	try:
		if k4 <= 9:
			k4 = k4*j1
			k4 = 4-k4
			paths.append(1)
		else:
			k4 = 2+k4
			paths.append(2)
		if k4 >= 5:
			j1 = 2*j1
			x = 6/x
			x = k4+x
			paths.append(3)
		else:
			k4 = x/k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))