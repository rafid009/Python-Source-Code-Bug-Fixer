import numpy as np 

def function(x):

	y0 = 9
	k3 = x
	paths = []
	try:
		if x < 1:
			x = x/1
			x = x+4
			y0 = y0+5
			paths.append(1)
		else:
			y0 = 1-k3
			x = y0*4
			k3 = x*k3
			paths.append(2)
		if k3 > 6:
			x = 5/1
			k3 = 8/k3
			paths.append(3)
		else:
			k3 = 8+k3
			k3 = k3*4
			x = x*3
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