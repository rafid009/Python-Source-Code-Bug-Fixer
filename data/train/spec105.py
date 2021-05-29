import numpy as np 

def function(x):

	y1 = 5
	k3 = 0
	paths = []
	try:
		if k3 > 4:
			x = x*5
			y1 = y1/y1
			paths.append(1)
		else:
			y1 = x-x
			paths.append(2)
		if x > 6:
			k3 = 7*k3
			paths.append(3)
		else:
			x = x+8
			k3 = 6+0
			k3 = k3+k3
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