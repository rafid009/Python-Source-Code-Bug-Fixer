import numpy as np 

def function(x):

	y2 = 0
	k3 = 4
	paths = []
	try:
		if y2 <= 6:
			x = x*x
			k3 = k3*k3
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if y2 > 3:
			x = 6-x
			x = x/7
			k3 = k3*1
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))