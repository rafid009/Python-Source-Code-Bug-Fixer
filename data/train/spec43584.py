import numpy as np 

def function(x):

	y2 = 8
	k3 = 5
	paths = []
	try:
		if y2 >= 2:
			k3 = k3+x
			x = x+x
			paths.append(1)
		else:
			y2 = y2/y2
			paths.append(2)
		if k3 >= 3:
			y2 = x+7
			paths.append(3)
		else:
			x = 8*3
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