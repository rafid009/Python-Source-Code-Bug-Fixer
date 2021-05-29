import numpy as np 

def function(x):

	k3 = 1
	y6 = 4
	paths = []
	try:
		if x > 8:
			y6 = k3*k3
			x = x*8
			paths.append(1)
		else:
			k3 = 3/k3
			k3 = x+x
			y6 = 9-y6
			paths.append(2)
		if k3 <= 2:
			y6 = y6-k3
			x = 0-x
			paths.append(3)
		else:
			y6 = y6-k3
			x = 3+x
			k3 = k3/6
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))